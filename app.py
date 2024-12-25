from flask import Flask, render_template, redirect, url_for, jsonify
import requests
from bs4 import BeautifulSoup
import csv
import os

app = Flask(__name__)

# Ordner für die Speicherung der CSV-Dateien
DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)

# URL der Jobseite
base_url = "https://www.jobscout24.ch/de/jobs/Data%20Science/?page={page}"

# Funktion zum Abrufen der Seite
def get_page_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Bei Fehlern eine Ausnahme auslösen
    return response.text

# Funktion zum Scrapen der Jobdaten
def scrape_jobs(base_url, max_pages=10):
    jobs = []

    for page in range(1, max_pages + 1):
        url = base_url.format(page=page)
        html_content = get_page_content(url)
        soup = BeautifulSoup(html_content, "html.parser")

        # Suche nach Job-Elementen
        job_articles = soup.find_all("article", class_="job-details")
        for job in job_articles:
            try:
                title = job.find("h2", class_="header-title").get_text(strip=True)
            except AttributeError:
                title = "N/A"

            try:
                company = job.find("h2", class_="company-title").get_text(strip=True)
            except AttributeError:
                company = "N/A"

            try:
                location = job.find("a", class_="company-location").get_text(strip=True)
            except AttributeError:
                location = "N/A"

            try:
                description = job.find("div", class_="job-description").get_text(strip=True)
            except AttributeError:
                description = "N/A"

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "description": description
            })

        print(f"Seite {page} verarbeitet.")

    return jobs

# Funktion zum Speichern in eine CSV
def save_to_csv(jobs, filename="jobs.csv"):
    if not jobs:
        print("Keine Jobs gefunden.")
        return

    # Überprüfe, ob die Datei existiert, und finde einen neuen Namen
    base_filename, extension = os.path.splitext(filename)
    filename = os.path.join(DATA_FOLDER, filename)
    counter = 1
    while os.path.exists(filename):
        filename = os.path.join(DATA_FOLDER, f"{base_filename}{counter}{extension}")
        counter += 1

    keys = jobs[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(jobs)

    print(f"Jobs wurden in {filename} gespeichert.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    jobs = scrape_jobs(base_url, max_pages=10)
    save_to_csv(jobs)
    return redirect(url_for("index"))

@app.route("/files")
def files():
    files = [f for f in os.listdir(DATA_FOLDER) if f.startswith("jobs") and f.endswith(".csv")]
    return jsonify(files)

if __name__ == "__main__":
    app.run(debug=True)