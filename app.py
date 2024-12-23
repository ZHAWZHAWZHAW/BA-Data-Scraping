from flask import Flask, render_template, request
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

# Scraping function using Selenium
def scrape_jobs():
    url = "https://www.jobs.ch/de/stellenangebote/?term=data%20science"

    # Selenium setup
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get(url)

    # Warte, bis die Seite geladen ist
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".search-results"))
        )
    except Exception as e:
        print(f"Error waiting for job listings: {e}")
        print(driver.page_source)
        driver.quit()
        return []

    jobs = []

    # Neue Selektoren verwenden
    job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-box")
    for job in job_listings:
        try:
            title = job.find_element(By.CSS_SELECTOR, "h2.job-title").text.strip()
        except:
            title = "N/A"

        try:
            company = job.find_element(By.CSS_SELECTOR, "div.company-name").text.strip()
        except:
            company = "N/A"

        try:
            location = job.find_element(By.CSS_SELECTOR, "span.job-location").text.strip()
        except:
            location = "N/A"

        try:
            description = job.find_element(By.CSS_SELECTOR, "div.job-description").text.strip()
        except:
            description = "N/A"

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "description": description
        })

    driver.quit()
    return jobs

# Save data to CSV
def save_to_csv(jobs, filename="jobs.csv"):
    keys = jobs[0].keys() if jobs else []
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(jobs)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    jobs = scrape_jobs()
    save_to_csv(jobs)
    return render_template("index.html", message="Jobs scraped and saved to CSV successfully!" if jobs else "No jobs were scraped. Please try again.")

if __name__ == "__main__":
    app.run(debug=True)