# 🚀 Flask Job Scraper Application

This project is a Flask-based web application that scrapes job listings from a specific website and provides an interface to view the scraped data. The application also saves the job data into CSV files for further analysis.

---

## 📖 Table of Contents

1. [Features](#1-features)
2. [Prerequisites](#2-prerequisites)
3. [Installation](#3-installation)
4. [Running Locally](#4-running-locally)
5. [Running with Docker](#5-running-with-docker)
6. [Application Endpoints](#6-application-endpoints)
7. [Folder Structure](#7-folder-structure)

---

## 🛠️ 1. Features

- Scrapes job listings from [JobScout24](https://www.jobscout24.ch/)
- Saves scraped job data into CSV files
- Provides an endpoint to list the generated CSV files
- Built with Flask and BeautifulSoup
- Automatically removes duplicate entries in job data

---

## 📋 2. Prerequisites

- Python 3.9 or higher
- Docker (if you want to run the application using Docker)

---

## ⚙️ 3. Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ZHAWZHAWZHAW/BA-Data-Scraping.git
   cd your-repo
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ 4. Running Locally

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8080
   ```

---

## 🐳 5. Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t job-scraper .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8080:8080 job-scraper
   ```

3. Access the application in your browser:
   ```
   http://localhost:8080
   ```

---

## 🌐 6. Application Endpoints

- **Home Page:** `/`
  - Displays the main index page.

- **Scrape Jobs:** `/scrape`
  - Scrapes job data and saves it into a CSV file.

- **List Files:** `/files`
  - Returns a JSON list of all saved CSV files.


---

## 📂 7. Folder Structure

```
project-root/
│
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── data/                 # Folder to store scraped CSV files
├── templates/            # HTML templates for the web interface
└── README.md             # Project documentation
```