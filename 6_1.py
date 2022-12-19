#Написать функцию преобразующую список строк, в список байт кодов. Написать обратную функцию.
string1 = ['Привет','Linux','Python']
print ('Заданная строки в списке: ',string1)
def modern_string (str):
    x = []
    for i in range(len(str)):
        x.append(str[i].encode('utf-8'))      
    return x

def reverse_string (str):
    y = []
    for i in range(len(str)):
        y.append(str[i].decode('utf-8')) 
    return y

mod = modern_string(string1)
print('Результат преобразованного списка строк в список байт кодов: ',mod)

rev = reverse_string(mod)
print('Результат обратного преобразования байт кодов в список строк: ',rev)