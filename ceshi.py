import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

hellow=tf.constant('nihao')
sess=tf.Session()

print(sess.run(hellow))

