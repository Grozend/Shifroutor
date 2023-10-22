from tkinter import *
from tkinter import ttk

win = Tk()

MORSE_CODE = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.', 'Ж': '...-',
              'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
              'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
              'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
              'Ю': '..--', 'Я': '.-.-', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/', '.': '......',
              ',': '.-.-.-', ':': '---...', ';': '-.-.-.', "'": '.----.', '"': '.-..-.',
              '-': '-....-', '/': '-..-.', '_': '..--.-', '?': '..--..', '!': '--..--', '+': '.-.-.', '@': '.--.-.',
              '|': '-...-'}

MORSE_DECODE = {'.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д', '.': 'Е', '...-': 'Ж', '--..': 'З',
                '..': 'И', '.---': 'Й', '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О', '.--.': 'П',
                '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У', '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч',
                '----': 'Ш', '--.-': 'Щ', '--.--': "Ъ", '-.--': 'Ы', '-..-': 'Ь', '..-..': 'Э', '..--': 'Ю',
                '.-.-': 'Я', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' ', '......': '.', '.-.-.-': ',',
                '---...': ':', '-.-.-.': ';', '.----.': "'", '.-..-.': '"', '-....-': '-', '-..-.': '/', '..--.-': '_',
                '..--..': '?', '--..--': '!', '.-.-.': '+', '.--.-.': '@', '-...-': '|'}


def give_info():
    info = Tk()

    giv_info_label1 = Label(info,
                            text='1. Для того, чтобы зашифровать Ваш текст, введите его в поле'
                                 ' "Введенный текст для шифрации" и нажмите кнопку "Зашифровать".', font='8',
                            background='#c8bea5')
    giv_info_label1.grid(row=1, column=0, padx=5, pady=5, stick=W)

    giv_info_label2 = Label(info, text='2. Для того, чтобы расшифровать Ваш текст, введите его с пробелами'
                                       ' в поле "Введенный текст для расшифровки" и нажмите кнопку "Дешифровать".',
                            font='8', background='#c8bea5')
    giv_info_label2.grid(row=2, column=0, padx=5, pady=5, stick=W)

    giv_info_label3 = Label(info, text='3. Также вы можете нажать кнопку "Копировать" и зашифрованный ранее текст'
                                       ' скопируется в поле "Введенный текст для расшифровки".', font='8',
                            background='#c8bea5')
    giv_info_label3.grid(row=3, column=0, padx=5, pady=5, stick=W)

    giv_info_label4 = Label(info, text='4. Для шифра цезаря необходимо указать сдвиг в поле "Сдвиг" (цифрой)'
                                       ' для шифрации и дешифрации введенного текста.', font='8',
                            background='#c8bea5')
    giv_info_label4.grid(row=4, column=0, padx=5, pady=5, stick=W)

    giv_info_label5 = Label(info, text='5. Ввод слов осуществляется вручную, поля не копируются,'
                                       ' символы в строке пишутся раздельно(через пробел).', font='8',
                            background='#c8bea5')
    giv_info_label5.grid(row=5, column=0, padx=5, pady=5, stick=W)

    giv_info_label6 = Label(info, text='6. Не использовать enter в азбуке морзе т.к. это приведет к некорректной работе'
                                       ' шифратора.', font='8',
                            background='#c8bea5')
    giv_info_label6.grid(row=6, column=0, padx=5, pady=5, stick=W)

    info.title("Инструкция")
    info['bg'] = '#c8bea5'
    info.geometry("1260x200")


def click1():
    window = Tk()

    def copy_comand():
        input_entry.delete("1.0", "end")
        input_entry.insert('1.0', morse_output.get("1.0", "end-1c"))

    # Шифрация морзе
    def convert_text_to_morse():
        text = input_text.get("1.0", "end-1c")
        morse_text = ""
        for char in text:
            if char.upper() in MORSE_CODE:
                morse_char = MORSE_CODE[char.upper()]
                morse_text += morse_char + " "
        morse_output.delete("1.0", "end")
        morse_output.insert("1.0", morse_text)

    first_label = Label(window, text="Шифратор", font='26', justify=CENTER, relief='solid')
    first_label.grid(row=0, column=0, padx=5, pady=5)

    input_label = Label(window, text="Введенный текст для шифрации:", relief='solid')
    input_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

    input_text = Text(window, height=5, width=100, wrap='word')
    input_text.grid(row=2, column=0, padx=5, pady=5, sticky=W)

    ys1 = ttk.Scrollbar(window, orient="vertical", command=input_text.yview, cursor='hand2')
    ys1.grid(row=2, column=1, sticky=NS)
    input_text["yscrollcommand"] = ys1.set

    convert_button = Button(window, text="Зашифровать", background='#7777FF',
                            command=convert_text_to_morse, cursor='hand2')
    convert_button.grid(row=3, column=0, padx=5, pady=5, sticky=W)

    output_label = Label(window, text="Зашифрованный текст:", relief='solid')
    output_label.grid(row=4, column=0, padx=5, pady=5, stick=W)

    morse_output = Text(window, height=5, width=100, wrap='word')
    morse_output.grid(row=5, column=0, padx=5, pady=5, sticky=W)

    ys2 = ttk.Scrollbar(window, orient="vertical", command=morse_output.yview, cursor='hand2')
    ys2.grid(row=5, column=1, sticky=NS)
    morse_output["yscrollcommand"] = ys2.set

    def decode_morse():
        morse_code = input_entry.get("1.0", "end-1c")
        message = ""
        morse_code_list = morse_code.split(" ")
        for code in morse_code_list:
            if code in MORSE_DECODE:
                message += MORSE_DECODE[code]
        output_text.delete("1.0", "end")
        output_text.insert("1.0", message)

    second_label = Label(window, text="Дешифратор", font='26', justify=CENTER, relief='solid')
    second_label.grid(row=6, column=0, padx=5, pady=5)

    input_label = Label(window, text="Введенный текст для расшифровки:", relief='solid')
    input_label.grid(row=7, column=0, padx=5, pady=5, stick=W)

    input_entry = Text(window, height=5, width=100, wrap='word')
    input_entry.grid(row=8, column=0, padx=5, pady=5, sticky=W)

    ysn1 = ttk.Scrollbar(window, orient="vertical", command=input_entry.yview, cursor='hand2')
    ysn1.grid(row=8, column=1, sticky=NS)
    input_entry["yscrollcommand"] = ysn1.set

    decode_button = Button(window, text="Дешифровать", background='#7777FF', command=decode_morse, cursor='hand2')
    decode_button.grid(row=9, column=0, padx=5, pady=5, stick=W)

    test_button = Button(window, text='Копировать', background='#009B00', command=copy_comand, cursor='hand2')
    test_button.grid(row=9, column=0, padx=105, pady=5, stick=W)

    input_label_mor = Label(window, text="Расшифрованный текст:", relief='solid')
    input_label_mor.grid(row=10, column=0, padx=5, pady=5, stick=W)

    output_text = Text(window, height=5, width=100, wrap='word')
    output_text.grid(row=11, column=0, padx=5, pady=5, sticky=W)

    ysn2 = ttk.Scrollbar(window, orient="vertical", command=output_text.yview, cursor='hand2')
    ysn2.grid(row=11, column=1, sticky=NS)
    output_text["yscrollcommand"] = ysn2.set

    window.title("Морзе")
    window['bg'] = '#c8bea5'
    window.geometry("900x680")


def click2():
    window2 = Tk()

    def copy_comand2():
        input_de_text.delete("1.0", "end")
        input_de_text.insert('1.0', output_text.get("1.0", "end-1c"))

    # Шифратор цезаря
    def caesar_cipher(text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    ascii_offset = ord('а')
                else:
                    ascii_offset = ord('А')
                encrypted_text += chr((ord(char) - ascii_offset + shift) % 32 + ascii_offset)
            else:
                encrypted_text += char
        return encrypted_text

    def encrypt_text():
        text = input_text.get("1.0", "end-1c")
        shift = int(shift_entry.get())
        encrypted_text = caesar_cipher(text, shift)
        output_text.delete("1.0", "end")
        output_text.insert("1.0", encrypted_text)

    third_label = Label(window2, text="Шифратор", font='26', justify=CENTER, relief='solid')
    third_label.grid(row=0, column=0, padx=5, pady=5)

    input_label = Label(window2, text="Введенный текст для шифрации:", relief='solid')
    input_label.grid(row=1, column=0, padx=5, pady=5, stick=W)

    input_text = Text(window2, height=5, width=100, wrap='word')
    input_text.grid(row=2, column=0, padx=5, pady=5, stick=W)

    ys3 = ttk.Scrollbar(window2, orient="vertical", command=input_text.yview, cursor='hand2')
    ys3.grid(row=2, column=1, sticky=NS)
    input_text["yscrollcommand"] = ys3.set

    shift_label = Label(window2, text="Сдвиг:", relief='solid')
    shift_label.grid(row=3, column=0, padx=5, pady=5, stick=W)

    shift_entry = Entry(window2)
    shift_entry.grid(row=4, column=0, padx=5, pady=5, stick=W)

    encrypt_button = Button(window2, text="Зашифровать", background='#7777FF', command=encrypt_text, cursor='hand2')
    encrypt_button.grid(row=5, column=0, padx=5, pady=5, stick=W)

    output_label = Label(window2, text="Зашифрованный текст:", relief='solid')
    output_label.grid(row=6, column=0, padx=5, pady=5, stick=W)

    output_text = Text(window2, height=5, width=100, wrap='word')
    output_text.grid(row=7, column=0, padx=5, pady=5, stick=W)

    ys4 = ttk.Scrollbar(window2, orient="vertical", command=output_text.yview, cursor='hand2')
    ys4.grid(row=7, column=1, sticky=NS)
    output_text["yscrollcommand"] = ys4.set

    # Дешифратор цезаря
    def caesar_decipher(text, shift):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    ascii_offset = ord('а')
                else:
                    ascii_offset = ord('А')
                decrypted_text += chr((ord(char) - ascii_offset - shift) % 32 + ascii_offset)
            else:
                decrypted_text += char
        return decrypted_text

    def decrypt_text():
        text = input_de_text.get("1.0", "end-1c")
        shift = int(shift_de_entry.get())
        decrypted_text = caesar_decipher(text, shift)
        output_de_text.delete("1.0", "end")
        output_de_text.insert("1.0", decrypted_text)

    fourth_label = Label(window2, text="Дешифратор", font='26', justify=CENTER, relief='solid')
    fourth_label.grid(row=8, column=0, padx=5, pady=5)

    input_delabel = Label(window2, text="Введенный текст для расшифровки:", relief='solid')
    input_delabel.grid(row=9, column=0, padx=5, pady=5, stick=W)

    input_de_text = Text(window2, height=5, width=100, wrap='word')
    input_de_text.grid(row=10, column=0, padx=5, pady=5, stick=W)

    ysn3 = ttk.Scrollbar(window2, orient="vertical", command=input_de_text.yview, cursor='hand2')
    ysn3.grid(row=10, column=1, sticky=NS)
    input_de_text["yscrollcommand"] = ysn3.set

    shift_de_label = Label(window2, text="Сдвиг:", relief='solid')
    shift_de_label.grid(row=11, column=0, padx=5, pady=5, stick=W)

    shift_de_entry = Entry(window2)
    shift_de_entry.grid(row=12, column=0, padx=5, pady=5, stick=W)

    decrypt_button = Button(window2, text="Дешифровать", background='#7777FF', command=decrypt_text, cursor='hand2')
    decrypt_button.grid(row=13, column=0, padx=5, pady=5, stick=W)

    test_button = Button(window2, text='Копировать', background='#009B00', command=copy_comand2, cursor='hand2')
    test_button.grid(row=13, column=0, padx=105, pady=5, stick=W)

    output_de_label = Label(window2, text="Расшифрованный текст:", relief='solid')
    output_de_label.grid(row=14, column=0, padx=5, pady=5, stick=W)

    output_de_text = Text(window2, height=5, width=100, wrap='word')
    output_de_text.grid(row=15, column=0, padx=5, pady=5, stick=W)

    ysn4 = ttk.Scrollbar(window2, orient="vertical", command=output_de_text.yview, cursor='hand2')
    ysn4.grid(row=15, column=1, sticky=NS)
    output_de_text["yscrollcommand"] = ysn4.set

    window2.title("Цезарь")
    window2['bg'] = '#c8bea5'
    window2.geometry("900x800")


def click3():
    window3 = Tk()

    def copy_comand3():
        bin_cod_entry.delete("1.0", "end")
        bin_cod_entry.insert('1.0', encrypted_text_entry.get("1.0", "end-1c"))
        bin_cod_entry.delete('end-2c')

    # Бинарный кодер
    def convert_text_to_double_cod():
        original_text = original_text_entry.get("1.0", "end-1c")
        encrypted_text = ""
        for char in original_text:
            binary_code = bin(ord(char))[2:]
            binary_code = binary_code.zfill(8)
            encrypted_text += binary_code + ' '
        encrypted_text_entry.delete("1.0", "end")
        encrypted_text_entry.insert("1.0", encrypted_text)

    fifth_label = Label(window3, text="Шифратор", font='26', justify=CENTER, relief='solid')
    fifth_label.grid(row=0, column=0, padx=5, pady=5)

    original_text_label = Label(window3, text="Введенный текст для шифрации:", relief='solid')
    original_text_label.grid(row=1, column=0, padx=5, pady=5, stick=W)

    original_text_entry = Text(window3, height=5, width=100, wrap='word')
    original_text_entry.grid(row=2, column=0, padx=5, pady=5, stick=W)

    ys5 = ttk.Scrollbar(window3, orient="vertical", command=original_text_entry.yview, cursor='hand2')
    ys5.grid(row=2, column=1, sticky=NS)
    original_text_entry["yscrollcommand"] = ys5.set

    encrypt_button = Button(window3, text="Зашифровать", background='#7777FF', command=convert_text_to_double_cod,
                            cursor='hand2')
    encrypt_button.grid(row=3, column=0, padx=5, pady=5, stick=W)

    encrypted_text_label = Label(window3, text="Зашифрованный текст:", relief='solid')
    encrypted_text_label.grid(row=4, column=0, padx=5, pady=5, stick=W)

    encrypted_text_entry = Text(window3, height=5, width=100)
    encrypted_text_entry.grid(row=5, column=0, padx=5, pady=5, stick=W)

    ys6 = ttk.Scrollbar(window3, orient="vertical", command=encrypted_text_entry.yview, cursor='hand2')
    ys6.grid(row=5, column=1, sticky=NS)
    encrypted_text_entry["yscrollcommand"] = ys6.set

    # Бинарный декодер
    def binary_decode():
        binary_code = bin_cod_entry.get("1.0", "end-1c")
        bin_decod = ""
        binary_code_list = binary_code.split(" ")
        for code in binary_code_list:
            decimal = int(code, 2)
            character = chr(decimal)
            bin_decod += character
        bin_decod_output.delete("1.0", "end")
        bin_decod_output.insert("1.0", bin_decod)

    sixth_label = Label(window3, text="Дешифратор", font='26', justify=CENTER, relief='solid')
    sixth_label.grid(row=6, column=0, padx=5, pady=5)

    binari_cod = Label(window3, text="Введенный текст для расшифровки:", relief='solid')
    binari_cod.grid(row=7, column=0, padx=5, pady=5, stick=W)

    bin_cod_entry = Text(window3, height=5, width=100)
    bin_cod_entry.grid(row=8, column=0, padx=5, pady=5, stick=W)

    ysn5 = ttk.Scrollbar(window3, orient="vertical", command=bin_cod_entry.yview, cursor='hand2')
    ysn5.grid(row=8, column=1, sticky=NS)
    bin_cod_entry["yscrollcommand"] = ysn5.set

    bin_decod_but = Button(window3, text="Дешифровать", background='#7777FF', command=binary_decode, cursor='hand2')
    bin_decod_but.grid(row=9, column=0, padx=5, pady=5, stick=W)

    test_button = Button(window3, text='Копировать', background='#009B00', command=copy_comand3, cursor='hand2')
    test_button.grid(row=9, column=0, padx=105, pady=5, stick=W)

    binari_decod = Label(window3, text="Расшифрованный текст:", relief='solid')
    binari_decod.grid(row=10, column=0, padx=5, pady=5, stick=W)

    bin_decod_output = Text(window3, height=5, width=100, wrap='word')
    bin_decod_output.grid(row=11, column=0, padx=5, pady=5, stick=W)

    ysn6 = ttk.Scrollbar(window3, orient="vertical", command=bin_decod_output.yview, cursor='hand2')
    ysn6.grid(row=11, column=1, sticky=NS)
    bin_decod_output["yscrollcommand"] = ysn6.set

    window3.title("Двоичный код")
    window3['bg'] = '#c8bea5'
    window3.geometry("900x700")


info_main_label = Label(text="Здравствуйте!",
                        font='Arial 11 normal roman', justify=CENTER, background='#c8bea5')
info_main_label.grid(row=0, column=0, padx=5, pady=5)

info_main_label1 = Label(text="Вы в программе для шифрации и дешифрации текста.",
                         font='Arial 11 normal roman', justify=CENTER, background='#c8bea5')
info_main_label1.grid(row=1, column=0, padx=5, pady=5)

info_main_label2 = Label(text="Выберите один из способов, представленных ниже.",
                         font='Arial 11 normal roman', justify=CENTER, background='#c8bea5')
info_main_label2.grid(row=2, column=0, padx=5, pady=5)

button3 = Button(text="Двоичный код", background='#7777FF', command=click3, height=1, width=68, cursor='hand2')
button3.grid(row=3, column=0, padx=5, pady=5, stick=W)

button2 = Button(text="Цезарь", background='#7777FF', command=click2, height=1, width=68, cursor='hand2')
button2.grid(row=4, column=0, padx=5, pady=5, stick=W)

button = Button(text="Морзе", background='#7777FF', command=click1, height=1, width=68, cursor='hand2')
button.grid(row=5, column=0, padx=5, pady=5, stick=W)

info_button = Button(text="Инструкция по работе", background='#FF5555', command=give_info, height=1, width=68,
                     cursor='hand2')
info_button.grid(row=6, column=0, padx=5, pady=5, stick=W)
if __name__ == "__main__":
    win['bg'] = '#c8bea5'
    win.title("Шифраторы")
    win.geometry("500x250")
    win.mainloop()
