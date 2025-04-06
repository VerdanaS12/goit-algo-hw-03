import re

def normalize_phone(phone_number):
   
    cleaned = re.sub(r'[^\d+]', '', phone_number)

    if cleaned.count('+') > 1 or (cleaned and cleaned[0] != '+' and '+' in cleaned):
        cleaned = cleaned.replace('+', '')

    if cleaned.startswith('+'):
        return cleaned
    elif cleaned.startswith('380'):
        return '+' + cleaned
    else:
        return '+38' + cleaned
