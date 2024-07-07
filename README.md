# Currency Exchange Automation
This program automates the process of converting currencies using the Minfin currency converter website. It utilizes the Selenium WebDriver to interact with the webpage and perform currency conversions.

## Currency Codes
Below are some commonly used currency codes:
- United States Dollar: USD
- Euro: EUR
- Ukrainian Hryvnia: UAH
- Polish Zloty: PLN
- British Pound: GBP
- Russian Ruble: RUB
- Japanese Yen: JPY
- Swiss Franc: CHF
- Chinese Yuan: CNY
- Canadian Dollar: CAD
- Australian Dollar: AUD

## How the Program Works
1. Setup and Initialization:
  - The program uses the Selenium WebDriver to open the Minfin currency converter website.
  - A Currency class is defined, which takes two currencies: the currency you have (curFrom) and the currency you want to convert to (curTo).
2. Setting the Currencies:
  - The set_currency method selects the specified currencies on the website by clicking through the options available.
  - The page is scrolled to ensure all currency options are visible for selection.
  - The program selects the currencies based on the provided input (curFrom and curTo).
3. Performing the Exchange:
  - The exchange method inputs a specified value into the currency converter.
  - The method retrieves and returns the converted value.
4. Executing the Conversion:
  - The program initializes the Currency class with different currency pairs and performs conversions for given amounts.

## Requirements
- Python
- Selenium
- Firefox WebDriver

## Installation
1. Install Selenium:
```
pip install selenium
```
2. Download and install the Firefox WebDriver

## Notes
1. Ensure the web page is fully loaded before interacting with it to avoid any unexpected behavior.
2. The script uses a hard-coded delay (time.sleep(3)) to wait for the page to load. Adjust this value if needed based on your internet speed.
3. The script may require adjustments if the structure or class names of the Minfin website change.
