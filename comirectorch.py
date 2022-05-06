# coding:utf-8

# packages
import argparse
import math
import os
import random
import shutil
import sys
import time
from collections import defaultdict
import numpy as np
import torch
from torch import nn
import faiss

# parameters
train_file = '../tfcomirec/src/data/book_data/book_train.txt'
valid_file = '../tfcomirec/src/data/book_data/book_valid.txt'
test_file = '../tfcomirec/src/data/book_data/book_test.txt'
cate_file = '../tfcomirec/src/data/book_data/book_item_cate.txt'
dataset = "book"

batch_size = 128
maxlen = 20
num_interest = 4
lr = 0.001
max_iter = 1000
patience = 20
test_iter = 50

# def func


# def net


# load data


# train


# valid

