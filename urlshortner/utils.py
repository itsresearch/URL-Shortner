"""Simple short-code generator."""

import random
import string


ALPHABET = string.ascii_letters + string.digits


def generate_short_code(model_class, length=6):
    """Generate a unique short code using random characters."""
    while True:
        code = "".join(random.choices(ALPHABET, k=length))
        if not model_class.objects.filter(short_code=code).exists():
            return code
