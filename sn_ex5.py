alphabet = " abcdefghijklmnopqrstuvwxyz"
alphabet_size = len(alphabet)
shift = int(input("Enter shift: "))
phrase = input("Enter phrase: ").lower()
cipher_text = []
for char in phrase:
    if char in alphabet:
        current_index = alphabet.index(char)
        new_index = (current_index + shift) % alphabet_size
        cipher_text.append(alphabet[new_index])
    else:
        cipher_text.append(char)
print("".join(cipher_text))