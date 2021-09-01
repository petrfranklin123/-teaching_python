import re

mytext = "Lorem ipsum dolor, sit amet consectetur 1907 adipisicing yandex elit. Fugiat perferendis vel inventore. Ducimus, repudiandae! Voluptatum dolorem quasi, asperiores, nesciunt modi maiores, ex facere quas id cupiditate alias sunt distinctio architecto." \
    "Repudiandae vero hic in, provident exercitationem error non a perspiciatis officia officiis libero vel id excepturi quo debitis eligendi facilis blanditiis magni. Facere minima deserunt repellendus culpa molestias, quasi obcaecati?" \
    "Maiores quas laboriosam  petrfranklin123@gmail.com sunt commodi unde non, 1707 assumenda ducimus yandex aut a voluptatibus vel aperiam ratione animi, aspernatur quia hic ab expedita est tempora nulla repudiandae eius. Voluptates nihil delectus explicabo!" \
    "Ullam animi adipisci quia nemo maiores laborum? Amet earum beatae yandex tempore harum quis tenetur doloremque quo repellendus. Vel temporibus, sed dolorem cumque distinctio ipsa quasi. Rem veniam nam commodi quo." \
    "Assumenda ipsam culpa ad distinctio quam. Porro 1927 distinctio velit, officiis numquam possimus voluptatum eos atque sunt soluta, et iste eum laudantium architecto harum. Sequi at non ab earum harum repudiandae?" 

'''
\d = любая цифра 
\D = любой сивол, но не цифра 
\w = любой алфавит  [A-Z a-z]
\W = любой символ, но не алфавитные символы 
\s = пробел 
\S = что угодно, но не пробелы
'''


# делаем паттерн, который и является регулярным выражением 
#textLookfor = r"yandex"

# ищем числа, в которых три цифры
#textLookfor = r"[0-9]{3}"

# ищем слова, в которых 6 буквенных символа
#textLookfor = r"\w{6}"

# ищем слова, в которых 6 буквенных символа c пробелом в конце
#textLookfor = r"\w{6}\s"

# ищем слова, которые начинаются с большой буквы и до бесконечности, пока есть маленькие буквенные символы
# дублируемость последнего выражения обеспечивает +
#textLookfor = r"[A-Z][a-z]+"

# ищем доменные имена
#textLookfor = r"@\w+\.\w+"

# ищем email
textLookfor = r"\S+\@\w+\.\w+"

# следующим действием мы вызываем функцию re и ф-ю findall, которая выведет все совпадени 
# в качестве параметров мы передаем паттерн и переменную, где сохранен текст 
allresult = re.findall(textLookfor, mytext)

print(allresult)

