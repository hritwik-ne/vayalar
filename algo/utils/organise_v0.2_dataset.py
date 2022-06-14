import os
import shutil

path = '../data/v_0.2'
folders = os.listdir(path)
if '.DS_Store' in folders: 
    folders.remove('.DS_Store')

for folder in folders:
    os.mkdir(f'../data/train/{folder}')
    os.mkdir(f'../data/val/{folder}')
    os.mkdir(f'../data/test/{folder}')

    path_1 = path + f'/{folder}'

    images_count = len(os.listdir(path_1))
    train_count = round(0.4 * images_count)
    validation_count = round(0.3 * images_count)

    files = os.listdir(path_1)
    for i in range(0, train_count):
        src_path = path_1 + f'/{files[i]}'
        dest_path = f'../data/train/{folder}'
        shutil.move(src_path, dest_path)

    for i in range(train_count, train_count+validation_count):
        src_path = path_1 + f'/{files[i]}'
        dest_path = f'../data/val/{folder}'
        shutil.move(src_path, dest_path)
    
    for i in range(train_count+validation_count, images_count):
        src_path = path_1 + f'/{files[i]}'
        dest_path = f'../data/test/{folder}'
        shutil.move(src_path, dest_path)