import os

path = "C:\\Users\\Avijit Samanta\\Desktop\\Nunito"

for file_name in os.listdir(path):
    # print(file_name)
    new_file_name = ""
    for letter in file_name:
        if letter.isupper():
            new_file_name = new_file_name + letter.lower()
        elif letter == "-":
            new_file_name = new_file_name + "_"
        else:
            new_file_name = new_file_name + letter
    print(new_file_name)
    src = path + "\\" + file_name
    dest = path + "\\" + new_file_name
    os.rename(src, dest)
