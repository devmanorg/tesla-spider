def clean_price(text):
    digits = [symbol for symbol in text if symbol.isdigit()]
    cleaned_text = ''.join(digits)
    if not cleaned_text:
        return None
    return int(cleaned_text)
