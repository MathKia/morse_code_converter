
class Morse:

    def __init__(self):

        self.morse = []
        self.morse_sentence = ''

    def to_morse(self, letter_key_morse_value):
        text = input('Enter text for morse translation: ').upper()
        for letter in text:
            self.morse.append(letter_key_morse_value[letter])
            self.morse_sentence = ' '.join(self.morse)
        return self.morse


