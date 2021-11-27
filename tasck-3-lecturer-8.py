from pprint import pprint
import os

directory_file_list = os.listdir()

def concat_files (file_names):
    dictionary_files = {}
    for file_name in file_names:
        if file_name.endswith(".txt"):
            txt_file_names = file_name
            path = os.path.join(os.getcwd(), txt_file_names)
            with open(path, encoding = 'utf-8') as file:
                data = file.readlines()
                dictionary_files[txt_file_names] = (len(data), data)
        else:
            continue
        x = sorted(dictionary_files.items(), key=lambda y: y[1][0])
    file = open('result.txt', 'w', encoding='utf-8')
    for i in x:
        file.write(str(i[0])+'\n')
        file.write(str(i[1][0]) + '\n')
        for j in i[1][1]:
            file.write(j.strip()+'\n')
    file.close()

concat_files (directory_file_list)
