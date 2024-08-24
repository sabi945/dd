import pandas as pd

# Sample data
data = {
    'PhoneNumber': ['123-456-7890', '456-789-0123', '789-012-3456', '0852-4260-0500'],
    'City': ['New York', 'London', 'Paris','makassar']
}
df = pd.DataFrame(data)

# Function to track cities using phone numbers
def track_cities(phone_number):
    # Convert phone number to a string
    phone_number = str(phone_number)

    # Search for the phone number in the DataFrame
    result = df[df['PhoneNumber'] == phone_number]

    # Return the city of the matching row
    if result.shape[0] > 0:
        return df['City'][0]
    else:
        return None

# Example usage
phone_number = '+6285242600500'
city = track_cities(phone_number)

# Print the result
print(city)  # Output: New York