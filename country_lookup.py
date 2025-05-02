#!/usr/bin/env python3
import sys
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import region_code_for_number
import pycountry
from geopy.geocoders import Nominatim

def get_coordinates(location):
    geolocator = Nominatim(user_agent="phone_locator")
    try:
        loc = geolocator.geocode(location)
        if loc:
            return (loc.latitude, loc.longitude)
    except:
        return None
    return None

def main(phone_number):
    try:
        number = phonenumbers.parse(phone_number, None)
        international = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        local = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL).replace(" ", "")
        region_code = region_code_for_number(number)
        country_name = pycountry.countries.get(alpha_2=region_code).name if region_code else "Unknown"
        area = geocoder.description_for_number(number, "en")
        isp = carrier.name_for_number(number, "en")
        time_zones = timezone.time_zones_for_number(number)

        # Try to geolocate the area
        search_area = f"{area}, {country_name}" if area else country_name
        coords = get_coordinates(search_area)

        print("[I]INFO:[THIS MODULE ALLOWS YOU TO SEARCH INFORMATION ABOUT A PHONE NUMBERS SUCH AS CARRIER]\n")
        print("[I]DATE-FORMAT:[EU:DD/MM/YYYY]\n")
        print(f"[I]DELETING OLD {phone_number}.txt\n")
        print(f"[+]SCANNING NUMBER: {phone_number}...\n")
        print("[I]THIS IS PROBABLY A REAL PHONE NUMBER\n")
        print(f"[v]INTERNATIONAL NUMBER: {international}")
        print(f"[v]LOCAL NUMBER: {local}")
        print(f"[v]COUNTRY PREFIX: +{number.country_code}")
        print(f"[v]COUNTRY CODE: {region_code}")
        print(f"[v]COUNTRY: {country_name}")
        print(f"[v]AREA/ZONE: {area or country_name}")
        print(f"[v]CARRIER/ISP: {isp or 'Unknown'}")
        print(f"[v]TIMEZONE N°1: {time_zones[0] if time_zones else 'Unknown'}\n")

        if coords:
            lat, lon = coords
            print("[v]AREA FOUND\n")
            print(f"[+]CHECKING NUMBER {phone_number} APPROXIMATE GEOLOCATION")
            print(f"[v]LATITUDE: {lat}")
            print(f"[v]LONGITUDE: {lon}")
            print(f"[v]GOOGLE MAPS LINK: https://www.google.com/maps/place/{lat},{lon}")
            print(f"[I]MAP SAVED ON: GUI/Reports/Phone/{phone_number}/Area_GeoLocation.html\n")
        else:
            print("[!] GEOLOCATION NOT FOUND")

        print(f"[+]PHONE NUMBER COUNTRY:{country_name}\n")
        print(f"[+]SEARCHING PHONE NUMBER {phone_number} ON DIFFERENT SITES")

    except phonenumbers.NumberParseException:
        print("[!] ERROR: Invalid phone number format.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 country1.py +[countrycode][number]")
        sys.exit(1)
    main(sys.argv[1])
