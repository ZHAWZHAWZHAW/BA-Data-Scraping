# 🚀 Job Scraper Application

This application is a preparatory task for my Bachelor's thesis (submission May 2025) in the Bachelor of Business Information Technology program at ZHAW School of Management and Law with a major in Data Science. It aims to collect the latest data on jobs in the field of "Data Science" to later analyze the requirements of the "Data Science" job profile as part of the Bachelor's thesis.

This project is a Flask-based web application that scrapes job listings from a specific website and provides an interface to view the scraped data. The application also saves the job data into CSV files for further analysis.

---

## 📖 Table of Contents

1. 🛠️ [Features](#%F0%9F%9B%A0%EF%B8%8F-1-features)
2. 📋 [Prerequisites](#%F0%9F%93%8B-2-prerequisites)
3. ⚙️ [Installation](#%E2%9A%99%EF%B8%8F-3-installation)
4. 🐳 [Running with Docker](#%F0%9F%90%B3-4-running-with-docker)   
   4.1. 🔧 [Running Locally](#%F0%9F%94%A7-41-running-locally)
5. 🌐 [Application Endpoints](#%F0%9F%8C%90-5-application-endpoints)
6. 📂 [Folder Structure](#%F0%9F%93%82-6-folder-structure)
7. ✉️ [Contact](#%E2%9C%89%EF%B8%8F-7-contact)

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
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🐳 4. Running with Docker

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


### 🔧 4.1 Running Locally

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8080
   ```

---

## 🌐 5. Application Endpoints

- **Home Page:** `/`
  - Displays the main index page.

- **Scrape Jobs:** `/scrape`
  - Scrapes job data and saves it into a CSV file. 

---

## 📂 6. Folder Structure

```
project-root/
│
├── data/                 # Folder to store scraped CSV files
├── templates/            # HTML templates for the web interface
│   └── index.html
├── .gitignore            # Git ignore file
├── app.py                # Main Flask application
├── Dockerfile            # Docker configuration
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

---

## ✉️ 7. Contact

If you have any questions or need further assistance, feel free to contact me at:

- **Email:** schneli3@students.zhaw.ch
- **GitHub:** [ZHAWZHAWZHAW](https://github.com/ZHAWZHAWZHAW)
