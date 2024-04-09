import requests
import time
from bs4 import BeautifulSoup

# URL of the website containing the table
url = "https://www.worldometers.info/coronavirus/#main_table"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
# wait 5 seconds
# time.sleep(5)
# Find the table by its ID
table = soup.find("table", {"id": "main_table_countries_today"})

# Iterate over the rows of the table
for row in table.find_all("tr"):
    # Find the table cells (td) in the current row
    row_class = row.get("class")
    if row_class and ("total_row_world" in row_class or "total_row" in row_class):
        # Skip this row
        continue

    cells = row.find_all("td")

    # Check if the row contains data (not the header row)
    if cells:
        # Extract the data from each cell
        country = cells[1].text.strip()
        total_cases = cells[2].text.strip()
        new_cases = cells[3].text.strip()
        total_deaths = cells[4].text.strip()
        new_deaths = cells[5].text.strip()
        total_recovered = cells[6].text.strip()
        new_recovered = cells[7].text.strip()
        active_cases = cells[8].text.strip()
        serious_critical = cells[9].text.strip()
        total_cases_per_million = cells[10].text.strip()
        deaths_per_million = cells[11].text.strip()
        total_tests = cells[12].text.strip()
        tests_per_million = cells[13].text.strip()
        population = cells[14].text.strip()

        # Print or process the extracted data as needed
        # if country != "Total:":
        print(f"Country: {country}, Total Cases: {total_cases}, New Cases: {new_cases}")