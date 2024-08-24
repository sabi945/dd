import phonenumbers
from phonenumbers import geocoder, carrier

def process_phone_number(phone_number_str):
    parsed_number = phonenumbers.parse(phone_number_str, None)
    
    if not phonenumbers.is_valid_number(parsed_number):
        return "Nomor telepon tidak valid."
    
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_national = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    location = geocoder.description_for_number(parsed_number, "en")
    operator = carrier.name_for_number(parsed_number, "en")
    region_code = phonenumbers.region_code_for_number(parsed_number)
    
    return {
        "formatted_number": formatted_number,
        "formatted_number_national": formatted_number_national,
        "location": location,
        "operator": operator,
        "region_code": region_code
    }

# Contoh penggunaan
phone_number = "+14155552671"
result = process_phone_number(phone_number)
print(result)
