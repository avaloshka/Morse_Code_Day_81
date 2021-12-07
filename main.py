from tkinter import *


CODE = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'}


space_between_letters = '   '

CODE_REVERSED = {v: k for k, v in CODE.items()}


def to_morse_code():
    inp = text_enter.get()
    message = inp.upper()
    print(message)
    morse_code = ''
    for char in message:
        if char == ' ':
            morse_code += '       '
        if char not in CODE:
            continue

        morse_code += CODE[char]
        morse_code += space_between_letters
    print(morse_code)
    morse_code_display_label.configure(text=morse_code)

    with open('code.txt', 'w') as file:
        file.write(morse_code)


window = Tk()
window.title('Morse Code Converter')
window.config(padx=50, pady=50)
window.configure(bg='#A0EEE7')
window.geometry('710x450')


text_label = Label(text="Enter text", font=8, bg='#A0EEE7')
text_label.grid(row=0, column=0)

text_enter = Entry()
text_enter.focus()
text_enter.grid(row=0, column=1, padx=10)

convert_button = Button(text='Convert!', command=to_morse_code, bg='#FA8072')
convert_button.grid(row=0, column=2)


# display
morse_code_display_label = Label(text='', font=("Helvetica", 6))
morse_code_display_label.grid(row=8, column=0)


window.mainloop()

