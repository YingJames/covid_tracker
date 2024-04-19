# Coronavirus Web Scraper

This project is a web scraper built in Python that extracts and stores daily coronavirus case data for countries around the world. The data is scraped from [Worldometers](https://www.worldometers.info/coronavirus/) and stored in a SQLite database.

## Features

- Scrapes the latest coronavirus case data, including total cases, new cases, total deaths, new deaths, recoveries, active cases, and more.
- Stores the data in a SQLite database for easy access and analysis.
- Automatically updates the database with the latest data every time the scraper is run.

## Prerequisites

Before running the scraper, make sure you have the following dependencies installed:

- Python 3.x
- requests
- BeautifulSoup4
- sqlite3 (included in Python's standard library)

The scraper will fetch the latest coronavirus case data from Worldometers and store it in a SQLite database named `coronavirus.db` in the project directory.

## Database Schema

The `coronavirus.db` database contains a single table named `coronavirus_data` with the following columns:

- `country` (TEXT)
- `total_cases` (INTEGER)
- `new_cases` (INTEGER)
- `total_deaths` (INTEGER)
- `new_deaths` (INTEGER)
- `total_recovered` (INTEGER)
- `new_recovered` (INTEGER)
- `active_cases` (INTEGER)
- `serious_critical` (INTEGER)
- `total_cases_per_million` (REAL)
- `deaths_per_million` (REAL)
- `total_tests` (INTEGER)
- `tests_per_million` (REAL)
- `population` (INTEGER)
- `date` (TEXT)

Each row in the table represents the coronavirus case data for a specific country on a given date.
