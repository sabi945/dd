import phonenumbers
from phonenumbers import geocoder, carrier

def process_phone_number(phone_number_str):
    try:
        # Parsing nomor telepon
        parsed_number = phonenumbers.parse(phone_number_str, None)
        
        # Validasi nomor telepon
        if not phonenumbers.is_valid_number(parsed_number):
            return "Nomor telepon tidak valid."
        
        # Memformat nomor telepon
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_national = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        
        # Mendapatkan deskripsi lokasi
        location = geocoder.description_for_number(parsed_number, "en")
        
        # Mendapatkan nama operator
        operator = carrier.name_for_number(parsed_number, "en")
        
        # Mendapatkan kode wilayah
        region_code = phonenumbers.region_code_for_number(parsed_number)
        
        return {
            "formatted_number": formatted_number,
            "formatted_number_national": formatted_number_national,
            "location": location,
            "operator": operator,
            "region_code": region_code
        }
    except phonenumbers.NumberParseException:
        return "Nomor telepon tidak dapat diparsing."

# Contoh penggunaan

phone_number = "+6285242600500"
result = process_phone_number(phone_number)
print(result)

# Contoh penggunaan

