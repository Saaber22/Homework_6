"""
* XOR шифрование/расшифрование. На входе файл с текстом и ключ шифрования (строка), 
# на выходе преобразованное (зашифрованное/расшифрованное) сообщение в файле.
"""

from pathlib import Path

"""
Исходные данные:
Два файла: inp.txt - Входные данные
           out.txt - Выходные данные 
"""
int_f = open('inp.txt', 'r', encoding='utf-8')
out_f = open('out.txt', 'w', encoding='utf-8')
data = str(int_f.read())

x = list(map(str, data.split()))
data = (x[0])
key = (x[1])
print('Исходная строка:',data)
print('Ключ:',key)

#Переводим строку и ключ в двоичный код
data_2 = ''.join(format(y,'08b') for y in bytearray(data,'utf-8'))
key_2 = ''.join(format(y,'08b') for y in bytearray(key,'utf-8'))

def enc_XOR(data, key):
    return "".join([chr(ord(c1)^ord(c2)) for (c1,c2) in zip(data,key)])

enc_text = enc_XOR(data_2,key_2)
dec_text = enc_XOR(enc_text,key_2)
print('Исходная строка в двоичном формате:',data_2)
print('Зашифрованный текст',enc_text)
print('Расшифрованный текст в двоичном формате',dec_text)

Path('out.txt').write_text(f'{enc_text} \n {dec_text}')

int_f.close
out_f.close
