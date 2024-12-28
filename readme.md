# 🚀 Flask Job Scraper Application

This project is a Flask-based web application that scrapes job listings from a specific website and provides an interface to view the scraped data. The application also saves the job data into CSV files for further analysis.

## 1. Table of Contents

1. [Features](#2-features)
2. [Prerequisites](#3-prerequisites)
3. [Installation](#4-installation)
4. [Running Locally](#5-running-locally)
5. [Running with Docker](#6-running-with-docker)
6. [Application Endpoints](#7-application-endpoints)
7. [Folder Structure](#8-folder-structure)
8. [License](#9-license)

## 2. Features

- Scrapes job listings from [JobScout24](https://www.jobscout24.ch/)
- Saves scraped job data into CSV files
- Provides an endpoint to list the generated CSV files
- Built with Flask and BeautifulSoup
- Automatically removes duplicate entries in job data

## 3. Prerequisites

- Python 3.9 or higher
- Docker (if you want to run the application using Docker)

## 4. Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create the `data` directory:
   ```bash
   mkdir data
   ```

## 5. Running Locally

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8080
   ```

## 6. Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t flask-job-scraper .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8080:8080 flask-job-scraper
   ```

3. Access the application in your browser:
   ```
   http://localhost:8080
   ```

## 7. Application Endpoints

- **Home Page:** `/`
  - Displays the main index page.

- **Scrape Jobs:** `/scrape`
  - Scrapes job data and saves it into a CSV file.

- **List Files:** `/files`
  - Returns a JSON list of all saved CSV files.

## 8. Folder Structure

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