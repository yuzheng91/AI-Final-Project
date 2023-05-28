import argparse
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Activation
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
from preprocess import *

def create_network(network_input, n_vocab):
    """ create the structure of the neural network """
    model = Sequential()
    model.add(LSTM(
        64,
        input_shape=(network_input.shape[1], network_input.shape[2]),
        return_sequences=True
    ))
    model.add(Dropout(0.3))
    model.add(LSTM(64, return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(64))
    model.add(Dense(64))
    model.add(Dropout(0.3))
    model.add(Dense(n_vocab))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    return model

def train(model, network_input, network_output):
    """ train the neural network """
    filepath = "weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
    checkpoint = ModelCheckpoint(
        filepath,
        monitor='loss',
        verbose=0,
        save_best_only=True,
        mode='min'
    )
    callbacks_list = [checkpoint]

    model.fit(network_input, network_output, epochs=10, batch_size=64, callbacks=callbacks_list)

def prepare_sequences(notes, n_vocab):
    """ Prepare the sequences used by the Neural Network """
    sequence_length = 1000
    network_input = []
    network_output = []

    # create input sequences and the corresponding outputs
    for song in notes:
        for i in range(0, len(song) - sequence_length, 1):
            sequence_in = song[i:i + sequence_length]
            sequence_out = song[i + sequence_length]
            network_output.append(sequence_out)

    n_patterns = len(network_input)

    # reshape the input into a format compatible with LSTM layers
    network_input = np.reshape(network_input, (n_patterns, sequence_length, 1))

    # normalize input
    network_input = network_input / float(n_vocab)

    network_output = np_utils.to_categorical(network_output)

    return network_input, network_output


def Get_Argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--read-csv', action='store_true', help='to read notes from csv file, default=False')
    parser.set_defaults(read_csv=False)
    args = parser.parse_args()
    return args.read_csv

if __name__ == '__main__':
    # determine whether to get notes from csv and remove frequency
    read_csv = Get_Argument()
    # get the list of notes of each song
    Notes_List = Load_Dataset(read_csv)
    # map note to index
    Notes_Index_List, Notes_map = Notes_to_Index(Notes_List)

    n_vocab = len(Notes_map)

    network_input, network_output = prepare_sequences(Notes_Index_List, n_vocab)

    model = create_network(network_input, n_vocab)

    train(model, network_input, network_output)