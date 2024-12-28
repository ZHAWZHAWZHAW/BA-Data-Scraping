from flask import Flask, render_template, redirect, url_for, jsonify
import requests
from bs4 import BeautifulSoup
import csv
import os
import time

app = Flask(__name__)

# Path to the data folder
DATA_FOLDER = "data"

# Ensure the data folder exists
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# Base URL for the job site
base_url = "https://www.jobscout24.ch/de/jobs/Data%20Science/?page={page}"

# Function: Fetches the content of a page
def get_page_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise exception for HTTP errors
    return response.text

# Function: Scrapes job listings
def scrape_jobs(base_url, max_pages=100):
    jobs = []

    for page in range(1, max_pages + 1):
        url = base_url.format(page=page)
        try:
            html_content = get_page_content(url)
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            break

        soup = BeautifulSoup(html_content, "html.parser")

        # Search for job elements
        job_articles = soup.find_all("article", class_="job-details")
        if not job_articles:
            print(f"No more job articles found on page {page}. Stopping search.")
            break

        for job in job_articles:
            job_data = {}

            # Extract company name
            company_tag = job.find("h2", class_="company-title")
            job_data["company"] = company_tag.get_text(strip=True) if company_tag else "N/A"

            # Extract location
            location_tag = job.find("a", class_="company-location")
            job_data["location"] = location_tag.get_text(strip=True) if location_tag else "N/A"

            # Extract job description
            description_tag = job.find("div", class_="job-description")
            job_data["description"] = description_tag.get_text(strip=True) if description_tag else "N/A"

            jobs.append(job_data)

        print(f"Processed page {page}.")
        time.sleep(2)  # Wait 2 seconds to avoid rate limits

    # Remove duplicates
    jobs = [dict(t) for t in {tuple(d.items()) for d in jobs}]

    return jobs

# Function: Save or update the CSV file
def save_to_csv(jobs, filename="jobs.csv"):
    if not jobs:
        print("No jobs found.")
        return

    # Full path to the file
    filepath = os.path.join(DATA_FOLDER, filename)

    # Load existing data if the file exists
    existing_jobs = []
    if os.path.exists(filepath):
        with open(filepath, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            existing_jobs = list(reader)

    # Create a set of existing jobs for quick lookup
    existing_jobs_set = {tuple(job.items()) for job in existing_jobs}

    # Add new jobs if they don't already exist
    new_jobs = [job for job in jobs if tuple(job.items()) not in existing_jobs_set]

    if new_jobs:
        print(f"{len(new_jobs)} new jobs found and added.")
        with open(filepath, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["company", "location", "description"])
            if not existing_jobs:  # Write header if file is newly created
                writer.writeheader()
            writer.writerows(new_jobs)
    else:
        print("No new jobs to add.")

# Flask route: Home page
@app.route("/")
def index():
    return render_template("index.html")

# Flask route: Scrape jobs and save to CSV
@app.route("/scrape")
def scrape():
    jobs = scrape_jobs(base_url, max_pages=50)  # Higher limit for more pages
    save_to_csv(jobs)
    return redirect(url_for("index"))

# Entry point for running the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)