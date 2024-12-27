from flask import Flask, render_template, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
import requests
from bs4 import BeautifulSoup
import csv
import os
import time

app = Flask(__name__)
socketio = SocketIO(app)

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
def scrape_jobs(base_url, max_pages=100):
    jobs = []

    for page in range(1, max_pages + 1):
        url = base_url.format(page=page)
        try:
            html_content = get_page_content(url)
        except Exception as e:
            print(f"Fehler beim Abrufen von Seite {page}: {e}")
            break

        soup = BeautifulSoup(html_content, "html.parser")

        # Suche nach Job-Elementen
        job_articles = soup.find_all("article", class_="job-details")
        if not job_articles:
            print(f"Keine weiteren Jobartikel auf Seite {page} gefunden. Beende die Suche.")
            break

        for job in job_articles:
            job_data = {}

            # Firma
            company_tag = job.find("h2", class_="company-title")
            job_data["company"] = company_tag.get_text(strip=True) if company_tag else "N/A"

            # Standort
            location_tag = job.find("a", class_="company-location")
            job_data["location"] = location_tag.get_text(strip=True) if location_tag else "N/A"

            # Beschreibung
            description_tag = job.find("div", class_="job-description")
            job_data["description"] = description_tag.get_text(strip=True) if description_tag else "N/A"

            jobs.append(job_data)

        print(f"Seite {page} verarbeitet.")
        socketio.emit('update', {'message': f"Seite {page} verarbeitet."})
        time.sleep(2)  # Warte 2 Sekunden, um Rate Limits zu vermeiden

    # Entferne doppelte Einträge
    jobs = [dict(t) for t in {tuple(d.items()) for d in jobs}]

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

    # Speichere nur die gewünschten Felder
    keys = ["company", "location", "description"]
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(jobs)

    print(f"Jobs wurden in {filename} gespeichert.")
    socketio.emit('update', {'message': f"Jobs wurden in {filename} gespeichert."})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    jobs = scrape_jobs(base_url, max_pages=10)  # Höheres Limit für mehr Seiten
    save_to_csv(jobs)
    return redirect(url_for("index"))

@app.route("/files")
def files():
    files = [f for f in os.listdir(DATA_FOLDER) if f.startswith("jobs") and f.endswith(".csv")]
    return jsonify(files)

if __name__ == "__main__":
    socketio.run(app, debug=True)