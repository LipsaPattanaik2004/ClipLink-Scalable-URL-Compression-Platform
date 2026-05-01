import string

BASE62 = string.ascii_letters + string.digits

def encode(num):
    base = len(BASE62)
    encoded = []
    while num:
        num, rem = divmod(num, base)
        encoded.append(BASE62[rem])
    return ''.join(reversed(encoded)) or "0"
