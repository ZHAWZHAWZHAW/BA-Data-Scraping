# 🚀 Job Web-Scraper Application

<p align="center">
  <img src="https://github.com/user-attachments/assets/393ca6f9-d086-4828-a3c6-af89b54a126d" alt="Job Web-Scraper Application" width="80%">
</p>

---

This application is a preparatory task for my Bachelor's thesis (submission May 2025) in the Bachelor of Business Information Technology program at ZHAW School of Management and Law with a major in Data Science. It aims to collect the latest data on jobs in the field of Data Science to later analyze the requirements of the "Data Science" job profile as part of the Bachelor's thesis.

This project is a Flask-based web application that scrapes job listings from a specific website and provides an interface to view the scraped data. The application also saves the job data into a CSV file for further analysis.

## 📖 Table of Contents

1. 🛠️ [Features](#1-features)
2. ⚙️ [Installation](#2-installation) 
3. 🌐 [Application Endpoints](#3-application-endpoints)
4. 🧹 [Data Cleaning](#4-data-cleaning)
5. 📂 [Folder Structure](#5-folder-structure)
6. 📸 [Sneak Peek](#6-sneak-peek)
7. ✉️ [Contact](#7-contact)

## 1. Features

- Scrapes job listings from [JobScout24](https://www.jobscout24.ch/)
- Saves scraped job data into CSV file
- Built with Flask and BeautifulSoup
- Tries to remove duplicate entries

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

## 4. Data Cleaning

The data cleaning process ensures the integrity and consistency of the scraped job listings. It includes the following steps:

1. **Normalization**: Text data in key columns (`company`, `location`, and `description`) is normalized by trimming whitespace and converting text to lowercase, improving duplicate detection.

2. **Duplicate Removal**: Duplicates are identified and removed based on a combination of `company`, `location`, and `description`.

3. **Column Cleanup**: If an `id` column exists in the raw data, it is removed to avoid conflicts.

4. **New Sequential IDs**: A new `id` column is added with sequential numbering, starting from 1.

5. **File Output**: The cleaned data is saved to `data/jobs_cleaned.csv` for subsequent analysis.

This process significantly reduces redundancy and prepares the dataset for more accurate analysis. Run the cleaning script after scraping to ensure high-quality data.

## 5. Folder Structure

```
project-root/
│
├── data/                 # Folder to store scraped & cleaned CSV files
│   ├─── raw/
│   │    └── jobs.csv
│   ├── cleanData.html
│   └── jobs_cleaned.csv
├── templates/            # HTML template for the web interface
│   └── index.html
├── .gitignore            # Git ignore CSV file
├── app.py                # Main Flask application
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## 6. Sneak Peek

<details>
<summary>Screenshot 1: Build application</summary>
<img width="850" alt="Bildschirmfoto 2024-12-28 um 18 52 23" src="https://github.com/user-attachments/assets/95d9b761-4714-4891-a895-552685e7cf45" />
</details>

<details>
<summary>Screenshot 2: Start application</summary>
<img width="661" alt="Bildschirmfoto 2024-12-28 um 14 22 39" src="https://github.com/user-attachments/assets/6b7a69cc-3e46-4c59-bb32-1b3a49eadd87" />
</details>

<details>
<summary>Screenshot 3: Start scraping</summary>
<img width="661" alt="Bildschirmfoto 2024-12-28 um 14 22 45" src="https://github.com/user-attachments/assets/62833753-3072-4aa1-9397-56008052b096" />
</details>

<details>
<summary>Screenshot 4: Successful scraping</summary>
<img width="661" alt="Bildschirmfoto 2024-12-28 um 14 26 38" src="https://github.com/user-attachments/assets/b331b1bd-1aaf-463d-bd24-82f9ee3fd0fb" />
</details>

## 7. Contact

If you have any questions or need further assistance, feel free to contact me at:

- **Email:** schneli3@students.zhaw.ch
- **GitHub:** [ZHAWZHAWZHAW](https://github.com/ZHAWZHAWZHAW)
