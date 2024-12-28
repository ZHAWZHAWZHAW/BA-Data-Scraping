# 🚀 Job Scraper Application

This application is a preparatory task for my Bachelor's thesis (submission May 2025) in the Bachelor of Business Information Technology program at ZHAW School of Management and Law with a major in Data Science. It aims to collect the latest data on jobs in the field of "Data Science" to later analyze the requirements of the "Data Science" job profile as part of the Bachelor's thesis.

This project is a Flask-based web application that scrapes job listings from a specific website and provides an interface to view the scraped data. The application also saves the job data into CSV files for further analysis.

![Python](https://img.shields.io/badge/python-3.9%2B-blue) 
![Docker](https://img.shields.io/badge/docker-supported-brightgreen) 


---

## 📖 Table of Contents

1. 🛠️ [Features](#1-features)
2. 📋 [Prerequisites](#2-prerequisites)
3. ⚙️ [Installation](#3-installation) 
4. 🌐 [Application Endpoints](#4-application-endpoints)
5. 📂 [Folder Structure](#5-folder-structure)
6. 📸 [Sneak Peek](#6-sneak-peek)
7. ✉️ [Contact](#7-contact)

---

## 1. Features

- Scrapes job listings from [JobScout24](https://www.jobscout24.ch/)
- Saves scraped job data into CSV files
- Provides an endpoint to list the generated CSV files
- Built with Flask and BeautifulSoup
- Automatically removes duplicate entries in job data

---

## 2. Prerequisites

- Python 3.9 or higher
- Docker (if you want to run the application using Docker)

---

## 3. Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ZHAWZHAWZHAW/BA-Data-Scraping.git
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 4. Application Endpoints

- **Home Page:** `/`
  - Displays the main index page.

- **Scrape Jobs:** `/scrape`
  - Scrapes job data and saves it into a CSV file. 

---

## 5. Folder Structure

```
project-root/
│
├── data/                 # Folder to store scraped CSV files
├── templates/            # HTML templates for the web interface
│   └── index.html
├── .gitignore            # Git ignore file
├── app.py                # Main Flask application
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

---

## 6. Sneak Peek

<details>
<summary>Screenshot 1: Build application</summary>
<img width="1206" alt="Bildschirmfoto 2024-12-28 um 14 22 12" src="https://github.com/user-attachments/assets/82fbe379-1323-4cc4-b991-8de6d0a979f6" />
</details>

<details>
<summary>Screenshot 2: Start application</summary>
<img width="661" alt="Bildschirmfoto 2024-12-28 um 14 22 39" src="https://github.com/user-attachments/assets/1d1a0ed0-101d-4a12-b611-9b9b8ec9cd45" />
</details>

<details>
<summary>Screenshot 3: Start scraping</summary>
<img width="661" alt="Bildschirmfoto 2024-12-28 um 14 22 45" src="https://github.com/user-attachments/assets/607d948f-fb16-491b-920b-c961d37d92c5" />
</details>

<details>
<summary>Screenshot 4: Successful scraping</summary>
<img width="661" alt="Bildschirmfoto 2024-12-28 um 14 26 38" src="https://github.com/user-attachments/assets/b331b1bd-1aaf-463d-bd24-82f9ee3fd0fb" />
</details>

---

## 7. Contact

If you have any questions or need further assistance, feel free to contact me at:

- **Email:** schneli3@students.zhaw.ch
- **GitHub:** [ZHAWZHAWZHAW](https://github.com/ZHAWZHAWZHAW)
