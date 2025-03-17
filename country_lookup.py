#!/usr/bin/env python3
import sys
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number

def get_country(phone_number):
    """Find the country of a given phone number."""
    try:
        number = phonenumbers.parse(phone_number, None)
        country = region_code_for_number(number)
        if country:
            print(f"Country: {country}")
        else:
            print("Country not found.")
    except phonenumbers.NumberParseException:
        print("Invalid phone number format.")

def print_help():
    """Display help information."""
    help_text = """
Usage: country_lookup [PHONE_NUMBER]

Find the country associated with a given phone number.

Arguments:
  PHONE_NUMBER    A phone number in international format (e.g., +30xxxxxxxxx)

Options:
  --help          Show this help message and exit.

Example:
  country_lookup +14155552671  # Returns country code (e.g., 'US')
"""
    print(help_text)

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] in ["--help", "-h"]:
        print_help()
    else:
        get_country(sys.argv[1])
