from morse_code import morse_dict, ascii_art

# Takes user input and returns morse code
def translate_to_morse(text_input, encryption):
    text_input = text_input.upper()
    code_list = [encryption[letter] for letter in text_input]
    code_text = " ".join(code_list)
    return code_text


def introduction():
    print("Morse Code Generator. Enter your text below")
    print("To exit the program type ----------> 'exit'")

# Helps format the console for better visibility
print(ascii_art)
introduction()

converting = True
while converting:
    print('-------------------------------------------')
    text = input('Text to convert: ')

    if text == "EXIT":
        converting = False
        print('Successfully exited.')
        break

    try:
        morse = translate_to_morse(text, morse_dict)
    except KeyError:
        print(f"Detected unwanted special characters inside: {text}. Make sure your text contains only letters A-Z and numbers 0-9")
    else:
        print(f"Converted text: {morse}\n")