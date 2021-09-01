import re

input_filename = "input.txt"
result_filename = "result.txt"

inputfile = open(input_filename, "r")
resultfile = open(result_filename, "w")

#читаем файл 
mytext = inputfile.read()
# [\w.-]+ пропускает все буквенные символы, включая точку и черту 
# (?!intel\.com) обработка исключения, эта строка выводиться не будет 
# [A-Za-z]+ любой буквенный символ 
# \.[\w.]+ экранированная точка и любой буквенный символ с точкой после 
lookfor = r"[\w.-]+@(?!intel\.com)[A-Za-z]+\.[\w.]+"

results = re.findall(lookfor, mytext)

for key in results:
    print(key)
    resultfile.write(key + "\n")