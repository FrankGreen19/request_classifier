import pickle
from keras.src.utils import pad_sequences
from src.models.models import RequestClass
import keras


def get_tokenizer():
    tokenizer = None

    with open('files/tokenizer.pickle', 'rb') as handle:
        loaded_tokenizer = pickle.load(handle)
        if loaded_tokenizer is not None:
            tokenizer = loaded_tokenizer

    return tokenizer

def get_sequence(request):
    tokenizer = get_tokenizer()
    if tokenizer is None:
        return None

    sequence = tokenizer.texts_to_sequences([request])
    return pad_sequences(sequence, maxlen=30)

def get_prediction(request):
    if request is None:
        return 'Empty request'

    sequence = get_sequence(request)
    if sequence is None:
        return 'Sequence is undefined'

    lstm_model = keras.models.load_model('files/classifier_model_lstm.h5')
    predictions = lstm_model.predict(x=sequence, verbose=0)[0]

    result = None
    for idx, prediction in enumerate(predictions):
        if prediction >= 0.7:
            result = RequestClass.classes_dict[idx]
            break

    return result
