from django.utils.crypto import get_random_string

ALLOWED_NUMBERS = '1234567890'


def generate_unique_code(length: int = 10) -> str:
    code = get_random_string(length=length, allowed_chars=ALLOWED_NUMBERS)
    if code.startswith('0'):
        return generate_unique_code()
    return code
