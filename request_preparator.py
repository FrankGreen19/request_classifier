import pickle
from keras.src.utils import pad_sequences


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
