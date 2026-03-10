# 🌍 Multi-Currency to ILS Scraper & API

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)
![BeautifulSoup](https://img.shields.io/badge/Library-BeautifulSoup4-orange.svg)

A high-performance **FastAPI** interface that provides real-time exchange rates for any currency against the Israeli Shekel (ILS). The data is dynamically fetched using a custom web scraper from Investing.com.

## 🚀 Key Features

* **Real-time Scraping:** Fetches live data directly from the web.
* **User-Agent Rotation:** Built-in mechanism to rotate browser identities to prevent IP blocking.
* **FastAPI Powered:** Extremely fast server with automatic Swagger UI documentation.
* **Structured Data:** Returns clean JSON responses including a full timestamp and floating-point rates.
* **AI Ready:** Designed to serve as a data source for AI models and financial bots.

## 🛠 Tech Stack

- **Backend:** FastAPI
- **Web Scraping:** BeautifulSoup4, Requests, LXML
- **Data Handling:** Datetime, Random (for UA rotation)

## 📋 Getting Started

### 1. Install Dependencies
Ensure you have Python 3.9+ installed, then run:
```bash
pip install fastapi uvicorn beautifulsoup4 requests lxml
```
### 2. Run the Server

Launch the API using the following command:

```bash
fastapi dev main.py
```
### 3. Usage


Access the interactive documentation at: http://127.0.0.1:8000/docs

Sample Request:
http://127.0.0.1:8000/get_cur/usd

Sample Response:

JSON
{
  "Year": 2026,
  "Month": 3,
  "Day": 10,
  "Hour": 19,
  "Min": 30,
  "Sec": 45,
  "Cur in ILS": 3.62
}




⚠️ Disclaimer
This project was built for educational purposes and as an infrastructure for feeding data into AI models. Please use responsibly and in accordance with the source website's terms of service.

Created with ❤️ by Ech012
