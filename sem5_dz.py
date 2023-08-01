"""
def fibinacci (args):
    first_num, second_num = 1, 1
    result = 1
    for i in range(args):
        yield first_num
        result = first_num + second_num
        first_num = second_num
        second_num = result



reps = int(input('Сколько чисел вывести?\n'))

for item in fibinacci(reps):
    print(item, end=' ')
"""
"""
names = ['Leonid', 'Igor', 'Artur']
payments = [120, 50, 300]
percents = ['22%', '9.8%', '12%']

print({names[i]: payments[i] * 0.01 * float(percents[i].replace('%', '')) for i in range(len(names))})
"""
"""
import os.path

path = 'C:\Шо то для учебы\Статья.txt'
print(os.path.split(path))

def path_spliter (path):
    *_, file = path.split("\\")
    part_of_path = path[:path.rfind("\\") + 1]
    file_name, file_type = file.split('.')
    res = (part_of_path, file_name, file_type)
    return (res)

print(path_spliter(path))
"""
