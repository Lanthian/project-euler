""" XOR Decryption

Each character on a computer is assigned a unique code and the preferred 
  standard is ASCII (American Standard Code for Information Interchange). For 
  example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
A modern encryption method is to take a text file, convert the bytes to ASCII, 
  then XOR each byte with a given value, taken from a secret key. The advantage 
  with the XOR function is that using the same encryption key on the cipher 
  text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 
  65.
For unbreakable encryption, the key is the same length as the plain text 
  message, and the key is made up of random bytes. The user would keep the 
  encrypted message and the encryption key in different locations, and without 
  both "halves", it is impossible to decrypt the message.
Unfortunately, this method is impractical for most users, so the modified method
  is to use a password as a key. If the password is shorter than the message, 
  which is likely, the key is repeated cyclically throughout the message. The 
  balance for this method is using a sufficiently long password key for 
  security, but short enough to be memorable.
Your task has been made easy, as the encryption key consists of three lower case
  characters. Using <0059_cipher.txt> a file containing the encrypted ASCII 
  codes, and the knowledge that the plain text must contain common English 
  words, decrypt the message and find the sum of the ASCII values in the 
  original text.
https://projecteuler.net/problem=59
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.files import easy_open

# --- Conditions of the problem ---
FILE = "0059cipher.txt"
DELIM = ","
KEY_RANGE = ('a', 'z')  # Inclusive


def selection_gen(options, length: int):
    """Takes an iterable `options` and returns a generator for all combinations
    of length `length`, considering different orders as different instances."""
    # Base case
    if length == 0: yield []

    # Recursive step
    else: 
        # Append each options to all possible suffixes
        for i in options:
            for s in  selection_gen(options, length-1):
                yield [i] + s

def xor_cycle(key: str, text: str) -> str:
    """Decrypts a cipher `text` by cycling a passcode `key` across it, XOR-ing
    each value by the respective character in key that lines up. Returns this
    decrypted text. Text and key should be in chr form, not ASCII numerals."""
    out_text = ""

    # Cycle variables
    cycle_length = len(key)
    i = 0

    # Iterate over characters
    for t in text: 
        out_text += chr(ord(key[i]) ^ ord(t))
        i = (i+1) % cycle_length
    return out_text


# --- Calculation ---
def main():
    # Read in data
    with easy_open(__file__, FILE) as fp:
        # Prepare text and key options
        cipher_text = [chr(int(d)) for d in fp.readline().split(DELIM)]
        k_range = [chr(d) for d in range(ord(KEY_RANGE[0]),ord(KEY_RANGE[1])+1)]

        # Iterate through possible keys
        for key in selection_gen(k_range, 3):
            decrypt = xor_cycle(key, cipher_text)

            # Check if valid decryption found
            if ' the ' in decrypt: 
                total = sum([ord(c) for c in decrypt])
                break


    # --- Output ---
    print(total) # 129,448
    return
