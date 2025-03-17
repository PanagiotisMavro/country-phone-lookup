# Country Phone Lookup

A simple Python script to find the country of a given international phone number.

## Features
- Accepts phone numbers in international format (e.g., `+14155552671`).
- Returns the corresponding country code (e.g., `US` for the United States).
- Supports the `--help` option for guidance.

## Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/PanagiotisMavro/country-phone-lookup.git
cd country-phone-lookup
pip install phonenumbers
chmod +x country_lookup.py
python3 country_lookup.py +14155552671

(Optional) Make it a Global Command

sudo mv country_lookup.py /usr/local/bin/country_lookup
country_lookup +447911123456
country_lookup --help
