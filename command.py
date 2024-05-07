import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import logging

tf.get_logger().setLevel(logging.ERROR)

from src.services import prediction_service


def get_prediction(request):
    return prediction_service.get_prediction(request)
