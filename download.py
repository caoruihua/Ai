#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : download.py
# @Author: laocao
# @Date  : 2019-05-10


from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
mnist=input_data.read_data_sets('MNIST_data/',one_hot=True)
for i in range (20):
    one_hot_lable=mnist.train.labels[i,:]
    label=np.argmax(one_hot_lable)
    print('mnist_train_%d.jpg label: %d' % (i,label))