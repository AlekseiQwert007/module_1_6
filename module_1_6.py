pho_book = {'Mama':123, 'Papa':456, 'Ded':789}#Создал словарь
print(pho_book)#Вывел весь словарь
print(pho_book['Papa'])# Вывел значение для ключа Papa
pho_book['Papa'] = 9999#Заменил значение для ключа Papa
print(pho_book)#Вывел весь словарь
print(pho_book.get('Vala'))# Вывод на экран несуществующего значения
pho_book['Baba'] = 88888#Добавил в словарь значение и ключ Baba/88888
print(pho_book)#Вывел весь словарь
pho_book.update({'Ant' : 44554455, 'Bum': 55885588})#Добавил пары Ант/4455... и Бум//5588...
print(pho_book)#Вывел весь словарь
del pho_book['Ded']# Удалил деда
print(pho_book)#Вывел весь словарь
print(pho_book.get('Ded'))# Вывод на экран несуществующего значения
print(pho_book)#Вывел весь словарь
#
my_set_ = {1,2,5,'Set',888,555,78,True,'Set',8,5,2,1,'Set'}#Создал множество
print(my_set_)#Вывел на экран
my_set_.update ({'A',38, 1,2,3,4})#Добавил во множество
print(my_set_)#Вывел на экран
my_set_.discard( 5 )#Удалил 5
print(my_set_)#Вывел на экран
my_set_.remove( 77 )#Удалил несуществующее 77
print(my_set_)#Вывел на экран
