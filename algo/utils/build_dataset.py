import os
import cv2
import numpy as np
import pandas as pd
from os import path
from resize_images import resize_image

data_dir = '../data/v_0.1/'
train_dataset = path.join(data_dir, 'fixed_train.csv')
valid_dataset = path.join(data_dir, 'fixed_valid.csv')
test_dataset = path.join(data_dir, 'fixed_test.csv')

cols = [i for i in range(1025)]

train_df = pd.read_csv(train_dataset, header=0, names=cols)
valid_df = pd.read_csv(valid_dataset, header=0, names=cols)
test_df = pd.read_csv(test_dataset, header=0, names=cols)

path = '../data/v_0.2/'
train_dir = path + 'train'
valid_dir = path + 'val'
test_dir = path + 'test'

train_labels = os.listdir(train_dir)
if '.DS_Store' in train_labels:
    train_labels.remove('.DS_Store')

valid_labels = os.listdir(valid_dir)
if '.DS_Store' in valid_labels:
    valid_labels.remove('.DS_Store')

test_labels = os.listdir(test_dir)
if '.DS_Store' in test_labels:
    test_labels.remove('.DS_Store')


new_train_df_list = []    
new_valid_df_list = []
new_test_df_list = []

for character in train_labels:
    train_images = os.listdir(train_dir + f'/{character}')
    for image in train_images:
        if image!='.DS_Store':
            path_1 = f'{train_dir}/{character}/{image}'
            image_cv2 = cv2.imread(path_1, cv2.IMREAD_UNCHANGED)
            image_pix = resize_image(image_cv2)
            row = np.insert(image_pix[0], 0, character)
            new_train_df_list.append(row.tolist())

for character in valid_labels:
    valid_images = os.listdir(valid_dir + f'/{character}')
    for image in valid_images:
        if image!='.DS_Store':
            path_1 = f'{valid_dir}/{character}/{image}'
            image_cv2 = cv2.imread(path_1, cv2.IMREAD_UNCHANGED)
            image_pix = resize_image(image_cv2)
            row = np.insert(image_pix[0], 0, character)
            new_valid_df_list.append(row.tolist())

for character in test_labels:
    test_images = os.listdir(test_dir + f'/{character}')
    for image in test_images:
        if image!='.DS_Store':
            path_1 = f'{test_dir}/{character}/{image}'
            image_cv2 = cv2.imread(path_1, cv2.IMREAD_UNCHANGED)
            image_pix = resize_image(image_cv2)
            row = np.insert(image_pix[0], 0, character)
            new_test_df_list.append(row.tolist())

train_df_2 = pd.DataFrame(new_train_df_list)
valid_df_2 = pd.DataFrame(new_valid_df_list)
test_df_2 = pd.DataFrame(new_test_df_list)

new_train_df = train_df.append(train_df_2)
new_valid_df = valid_df.append(valid_df_2)
new_test_df = test_df.append(test_df_2)

new_train_df.to_csv('../data/combined/train.csv', index=False)
new_valid_df.to_csv('../data/combined/valid.csv', index=False)
new_test_df.to_csv('../data/combined/test.csv', index=False)