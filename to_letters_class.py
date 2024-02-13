def check_morse(morse, morse_value_letter_key):

    for value in morse:
        if value not in morse_value_letter_key:
            return False
    return True

class Letters:

    def __init__(self):
        self.text_sentence = ''

    def to_english(self, morse_value_letter_key):
        morse = input('Enter morse for text translation: ')

        is_morse = check_morse(morse, morse_value_letter_key)

        if is_morse:
            morse_list = morse.split(' ')
            print(morse_list)
            for value in morse_list:
                if value == '':
                    self.text_sentence += ' '
                else:
                    self.text_sentence += morse_value_letter_key[value]
            return self.text_sentence

        else:
            print("This is not morse code")
            return self.to_english(morse_value_letter_key)

