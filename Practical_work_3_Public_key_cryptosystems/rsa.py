import random
import sys
from sympy import isprime, mod_inverse

def generate_prime_candidate(length):
    # Generate a random odd integer of specified bit length
    p = random.getrandbits(length)
    # Apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length):
    p = 4
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_keypair(bit_length):
    p = generate_prime_number(bit_length)
    q = generate_prime_number(bit_length)
    while q == p:
        q = generate_prime_number(bit_length)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def write_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)

def main():
    print("RSA Encryption/Decryption")
    print("1. Generate key pair")
    print("2. Encrypt a message")
    print("3. Decrypt a message")
    choice = input("Choose an option: ")
    
    if choice == '1':
        bit_length = int(input("Enter bit length for keys: "))
        public, private = generate_keypair(bit_length)
        print("Public key:", public)
        print("Private key:", private)
        write_file("public_key.txt", f"{public[0]},{public[1]}")
        write_file("private_key.txt", f"{private[0]},{private[1]}")
        print("Keys have been saved to 'public_key.txt' and 'private_key.txt'")
    
    elif choice == '2':
        filepath = input("Enter the file path of the plaintext: ")
        plaintext = read_file(filepath)
        public_key = input("Enter the public key (e,n) separated by a comma: ")
        e, n = map(int, public_key.split(','))
        public = (e, n)
        encrypted_msg = encrypt(public, plaintext)
        write_file("encrypted_message.txt", ','.join(map(str, encrypted_msg)))
        print("Encrypted message saved to 'encrypted_message.txt'")
    
    elif choice == '3':
        filepath = input("Enter the file path of the ciphertext: ")
        ciphertext = read_file(filepath)
        ciphertext = list(map(int, ciphertext.split(',')))
        private_key = input("Enter the private key (d,n) separated by a comma: ")
        d, n = map(int, private_key.split(','))
        private = (d, n)
        decrypted_msg = decrypt(private, ciphertext)
        write_file("decrypted_message.txt", decrypted_msg)
        print("Decrypted message saved to 'decrypted_message.txt'")
    
    else:
        print("Invalid option selected!")

if __name__ == "__main__":
    main()
