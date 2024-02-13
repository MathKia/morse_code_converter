from to_morse_class import Morse
from to_letters_class import Letters

letter_key_morse_value = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' '
}

morse_value_letter_key = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
                          '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
                          '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
                          '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
                          '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
                          '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',',
                          '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
                          '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-',
                          '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', ' ': ' '
                          }


def start():
    user_choice = input("Type 'T' to translate or 'E' to exit: ")
    if user_choice == 'T':

        morse_or_text = input("Type 'M' for text into Morse or 'T' for Morse into text: ")
        if morse_or_text == 'M':
            morse_instance = Morse()
            morse_instance.to_morse(letter_key_morse_value=letter_key_morse_value)
            print(morse_instance.morse_sentence)
        elif morse_or_text == 'T':
            letters_instance = Letters()
            english_text = letters_instance.to_english(morse_value_letter_key=morse_value_letter_key)
            print(english_text)
        else:
            print('That is not a valid option')
        start()

    elif user_choice == 'E':
        print('Program Ended')

    else:
        print('That is not a valid option')
        start()


start()
