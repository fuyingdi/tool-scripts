import os
import shutil


if __name__ == "__main__":
    name_str = set()
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            # print(os.path.join('', name))
            if not str(name).startswith('.'):
                name_str.add(name.split(' ')[0])
    name_str.remove('combine_with_prefix.py')
for name in name_str:
    print("新建文件夹: "+ name)
    try:
        os.mkdir('./'+name)
    except:
        pass
    files = os.listdir('.')
    for file_name in files:
        if file_name.startswith(name):
            print('move')
            shutil.move(file_name, './'+name)