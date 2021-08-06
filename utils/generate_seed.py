import random
import string


def generate_seed(length: int = 20) -> str:
    s = string.ascii_letters + string.punctuation + string.digits
    r = ''.join(random.choice(s) for i in range(length))
    return r
