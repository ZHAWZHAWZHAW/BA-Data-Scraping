# 🚀 Job Web-Scraper Application

<p align="center">
  <img src="https://github.com/user-attachments/assets/721e6854-a4ee-44b7-9837-c114ef1ec3a9" alt="Job Web-Scraper Application" width="80%">
</p>

---

This application is a preparatory task for my Bachelor's thesis (submission May 2025) in the Bachelor of Business Information Technology program at ZHAW School of Management and Law with a major in Data Science. It aims to collect the latest data on jobs in the field of Data Science to later analyze the requirements of the "Data Science" job profile as part of the Bachelor's thesis.

This project is a Flask-based web application that scrapes job listings from a specific website and provides an interface to view the scraped data. The application also saves the job data into a CSV file for further analysis.

## 📖 Table of Contents

1. 🛠️ [Features](#1-features)
2. ⚙️ [Installation](#2-installation) 
3. 🌐 [Application Endpoints](#3-application-endpoints)
4. 📂 [Folder Structure](#4-folder-structure)
5. 📸 [Sneak Peek](#5-sneak-peek)
6. ✉️ [Contact](#6-contact)

## 1. Features

- Scrapes job listings from [JobScout24](https://www.jobscout24.ch/)
- Saves scraped job data into CSV file
- Built with Flask and BeautifulSoup
- Tries to remove duplicate entries
- Displays all the jobs scraped on the frontend

## 2. Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ZHAWZHAWZHAW/BA-Data-Scraping.git
   ```

2. Create and activate a virtual environment:
   - for macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
   - for Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3. Verify the Python version inside the virtual environment:
   ```bash
   python --version
   ```

4. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the Flask application:
   ```bash
   python app.py
   ```


## 3. Application Endpoints

- **Home Page:** `/`
  - Displays the main index page.

- **Scrape Jobs:** `/scrape`
  - Scrapes job data and saves it into a CSV file. 

## 4. Folder Structure

```
project-root/
│
├── data/                 # Folder to store scraped CSV file
├── templates/            # HTML template for the web interface
│   └── index.html
├── .gitignore            # Git ignore CSV file
├── app.py                # Main Flask application
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## 5. Sneak Peek

<details>
<summary>Screenshot 1: Build application</summary>
<img width="846" alt="Bildschirmfoto 2024-12-28 um 16 22 14" src="https://github.com/user-attachments/assets/b461cd1e-4617-4260-bbfe-19db33fcf2c1" />
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

## 6. Contact

If you have any questions or need further assistance, feel free to contact me at:

- **Email:** schneli3@students.zhaw.ch
- **GitHub:** [ZHAWZHAWZHAW](https://github.com/ZHAWZHAWZHAW)
