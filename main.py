import base64


def encrypt_string(key, string):
    encrypted = []
    for i, c in enumerate(string):
        num_key = ord(key[i % len(key)])
        num_str = ord(c)
        encrypted.append(chr((num_str + num_key) % 2048))
    result = ''.join(encrypted)
    return str(base64.standard_b64encode(result.encode("utf-8")), "utf-8")


def decrypt_string(key, string):
    decrypted = []
    decoded = str(base64.standard_b64decode(string), "utf-8")
    for i, c in enumerate(decoded):
        num_key = ord(key[i % len(key)])
        num_str = ord(c)
        decrypted.append(chr((num_str - num_key) % 2048))
    return ''.join(decrypted)


if __name__ == '__main__':
    enc_key = input("Enter encryption key:")
    enc_str = input("Enter string to encrypt:")
    enc = encrypt_string(enc_key, enc_str)
    print("Encrypted string: " + enc)
    print("Decrypted string: " + decrypt_string(enc_key, enc))
