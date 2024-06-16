import os
from azure.communication.phonenumbers import PhoneNumbersClient

def get_purchased_numbers(connection_string, found_numbers_file, failed_keys_file):
    try:
        print('Azure Communication Services - Get Purchased Phone Numbers')

        # Initializing phone number client
        phone_numbers_client = PhoneNumbersClient.from_connection_string(connection_string)

        # Get all purchased phone numbers
        purchased_phone_numbers = phone_numbers_client.list_purchased_phone_numbers()
        print('Purchased phone numbers:')
        found_numbers = []
        for purchased_phone_number in purchased_phone_numbers:
            found_numbers.append(purchased_phone_number.phone_number)
            print(purchased_phone_number.phone_number)

        if found_numbers:
            with open(found_numbers_file, 'a') as found_file:
                for number in found_numbers:
                    found_file.write(f'{connection_string}: {number}\n')
        else:
            with open(failed_keys_file, 'a') as failed_file:
                failed_file.write(f'{connection_string}\n')

    except Exception as ex:
        print('Exception:')
        print(ex)

def execute_requests(access_keys_file, found_numbers_file, failed_keys_file):
    with open(access_keys_file, 'r') as file:
        for line in file:
            connection_string = line.strip()
            get_purchased_numbers(connection_string, found_numbers_file, failed_keys_file)

if __name__ == "__main__":
    access_keys_file = 'access_keys.txt'  # Path to your access keys file
    found_numbers_file = 'found_numbers.txt'  # Path to store found numbers
    failed_keys_file = 'failed_keys.txt'  # Path to store failed keys
    execute_requests(access_keys_file, found_numbers_file, failed_keys_file)
