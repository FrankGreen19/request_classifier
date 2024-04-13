import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import logging

tf.get_logger().setLevel(logging.ERROR)

import sys
import keras
import request_preparator
from classes import classes_dict

request = None
try:
    request = sys.argv[1]
except IndexError:
    print('Не передан запрос')
    sys.exit(1)

sequence = request_preparator.get_sequence(request)
if sequence is []:
    print('Не удалось построить последовательность')
    sys.exit(1)

lstm_model = keras.models.load_model('files/classifier_model_lstm.h5')
predictions = lstm_model.predict(x=sequence, verbose=0)[0]

result = None
for idx, prediction in enumerate(predictions):
    if prediction >= 0.7:
        result = classes_dict[idx]
        break

print(result)
