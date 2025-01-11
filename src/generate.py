import requests
from bs4 import BeautifulSoup
import csv

def scrape_whiskygospel():
    # URL of the target webpage
    url = "https://whiskygospel.com/smws-codes/"

    # Send a GET request to fetch the webpage content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the webpage: {response.status_code}")
        return

    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the first table on the page
    tables = soup.find_all("table")

    if not tables:
        print("No tables found on the webpage.")
        return

    # Prepare data for CSV
    csv_data = []
    headers = ["SMWS Code", "Distillery", "Region/Country"]
    csv_data.append(headers)

    for table in tables:
        rows = table.find_all("tr")
        for row in rows[1:]:  # Skip header row for each table
            cols = row.find_all("td")
            data = [col.get_text(strip=True) for col in cols]

            # Only process rows with the expected number of columns
            if len(data) == 3:
                # Set "N/A" for missing distillery
                if not data[1]:
                    data[1] = "N/A"
                # NOTE: There is bug in data "133;Westland (Washington, USA);133"
                #       Lets fix it to "133;Westland;Washington, USA"
                elif data[0] == data[2] == "133":
                    data[1] = "Westland"
                    data[2] = "Washington, USA"
                csv_data.append(data)

    # Write to CSV
    output_file = "data/smws_codes.csv"
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(csv_data)

    print(f"{len(csv_data)} rows successfully exported to {output_file}")

# Run the scraper
scrape_whiskygospel()
