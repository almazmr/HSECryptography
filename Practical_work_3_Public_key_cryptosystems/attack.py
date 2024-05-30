import sympy

def factorize_rsa(N):
    p, q = sympy.factorint(N)
    return p, q

def decrypt_rsa(ciphertext, p, q, e):
    phi = (p - 1) * (q - 1)
    d = sympy.mod_inverse(e, phi)
    plaintext = pow(ciphertext, d, p * q)
    return plaintext

N = 589
e = 17
ciphertext = 123
p, q = factorize_rsa(N)
plaintext = decrypt_rsa(ciphertext, p, q, e)
print("Расшифрованный текст:", plaintext)