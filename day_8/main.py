# Cesar Cipher
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]


def caeser(start_text, shift_ammount, cipher_direction):
    output_text = ''
    shift_ammount = shift_ammount % 26
    for char in start_text:
        if char in alphabet:
            old_index = alphabet.index(char)
            
            if cipher_direction == 'encode':
                new_index = (old_index + shift_ammount) % len(alphabet)
            elif cipher_direction == 'decode':
                new_index = (old_index - shift_ammount) % len(alphabet)
            output_text += alphabet[new_index]
        else:
            output_text += char
    print(f"The {cipher_direction}d text is {output_text}")

        
print(art.logo)
run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)

    run_again = input("Contine? 'Y' or 'N'\n").lower()  
    if run_again == 'n':
        run = False
        print('Bye')  
    



