# SMWS Codes CSV Generator

This project extracts Scotch Malt Whisky Society (SMWS) codes from the webpage [https://whiskygospel.com/smws-codes/](https://whiskygospel.com/smws-codes/) and consolidates them into a semicolon separated CSV file.

## Prerequisites

Make sure you have Python 3.7+ installed on your system. You can download Python from [https://www.python.org/](https://www.python.org/).

## Setting Up the Environment

1. Clone this repository:
   `git clone https://github.com/jarkkojarvinen/smws-codes-csv-generator.git`
   `cd smws-codes-csv-generator`

2. Create a virtual environment:
   `python -m venv venv`

3. Activate the virtual environment:
   - On Windows:
     `.\venv\Scripts\activate`
   - On macOS/Linux:
     `source venv/bin/activate`

4. Install the required packages:
    `pip install -r requirements.txt`

5. Deactivate the virtual environment when you're done:
   `deactivate`

## Running the Script

To generate the smws_codes.csv file:

1. Ensure the environment is activated (see Step 3 above).
2. Run the script:
   - On Windows:
      `python src\generate.py`
   - On macOS/Linux:
      `python src/generate.py`
3. The CSV file `smws_codes.csv` is generated under the data folder

## SMWS Codes

Generated CSV file example:

```csv
SMWS Code;Distillery;Region/Country
1;Glenfarclas;Speyside
2;Glenlivet;Speyside
...
```

## Project Structure

```plaintext
smws-codes-csv-generator
│
├── .vscode
│   ├── launch.json     # VS Code debug settings file
│   └── settings.json   # VS Code settings file
├── src
│   └── generate.py     # Script to scrape and generate the CSV file
├── .gitignore          # Ignore file to keep project clean
├── LICENCE             # Licence
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

## Dependencies

The required Python libraries are listed in requirements.txt. These will be installed automatically when you run `pip install -r requirements.txt`.

## Notes

Ensure you have a stable internet connection while running the script as it fetches data from the web. If the webpage structure changes, the script may require adjustments to handle the new structure.
