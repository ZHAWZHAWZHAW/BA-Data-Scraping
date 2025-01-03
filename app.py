from flask import Flask, render_template, redirect, url_for, jsonify
import requests
from bs4 import BeautifulSoup
import csv
import os
import time
import hashlib

app = Flask(__name__)

# Path to the data folder
DATA_FOLDER = "data/raw"

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

# Function: Generates a unique hash for a job
def hash_job(job):
    """Erzeugt einen eindeutigen Hash für ein Job-Dictionary."""
    job_str = f"{job['description']}|{job['company']}|{job['location']}"
    return hashlib.sha256(job_str.encode('utf-8')).hexdigest()

# Function: Removes duplicate jobs
def remove_duplicates(jobs):
    """Entfernt Duplikate basierend auf Hashes."""
    seen_hashes = set()
    unique_jobs = []
    for job in jobs:
        job_hash = hash_job(job)
        if job_hash not in seen_hashes:
            seen_hashes.add(job_hash)
            unique_jobs.append(job)
    return unique_jobs

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
        job_articles = soup.find_all("li", class_="job-list-item")
        if not job_articles:
            print(f"No more job articles found on page {page}. Stopping search.")
            break

        for job in job_articles:
            job_data = {}

            # Extract job title as description
            description_tag = job.find("a", class_="job-link-detail job-title")
            job_data["description"] = description_tag.get_text(strip=True) if description_tag else "N/A"

            # Extract company name
            company_tag = job.find("p", class_="job-attributes").find("span")
            job_data["company"] = company_tag.get_text(strip=True) if company_tag else "N/A"

            # Extract location
            location_tag = company_tag.find_next_sibling("span") if company_tag else None
            job_data["location"] = location_tag.get_text(strip=True) if location_tag else "N/A"

            # Extract detailed job description (if available)
            detail_url = description_tag["href"] if description_tag else None
            if detail_url:
                detail_page_url = f"https://www.jobscout24.ch{detail_url}"
                try:
                    detail_page_content = get_page_content(detail_page_url)
                    detail_soup = BeautifulSoup(detail_page_content, "html.parser")
                    detail_description_tag = detail_soup.find("div", class_="job-description")
                    if detail_description_tag:
                        detailed_description = detail_description_tag.get_text(strip=True)
                        job_data["description"] += f"\n{detailed_description}"
                except Exception as e:
                    print(f"Error fetching job details from {detail_page_url}: {e}")

            jobs.append(job_data)

        print(f"Processed page {page}. Found {len(job_articles)} jobs.")
        time.sleep(2)  # Wait 2 seconds to avoid rate limits

    # Remove duplicates
    jobs = remove_duplicates(jobs)

    return jobs

# Function: Save or update the CSV file
def save_to_csv(jobs, filename="jobs.csv"):
    if not jobs:
        print("No jobs found.")
        return

    # Full path to the file
    filepath = os.path.join(DATA_FOLDER, filename)

    # Load existing data if the file exists
    existing_hashes = set()
    if os.path.exists(filepath):
        with open(filepath, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            existing_hashes = {hash_job(row) for row in reader}

    # Add new jobs if they don't already exist
    new_jobs = [job for job in jobs if hash_job(job) not in existing_hashes]

    # Add a unique identifier for each job
    for idx, job in enumerate(new_jobs, start=1):
        job["id"] = idx

    if new_jobs:
        print(f"{len(new_jobs)} new jobs found and added.")
        with open(filepath, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "company", "location", "description"])
            if not os.path.exists(filepath) or os.stat(filepath).st_size == 0:  # Write header if file is newly created
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