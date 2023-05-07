import os
import numpy as np
import pandas as pd
from music21 import *
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

def Load_Dataset():
    Midi_List = []
    for dir in os.listdir('./Data_p'):
        path = f'./Data_p/{dir}'
        for file in os.listdir(path):
            filepath = path + f'/{file}'
            print(filepath)
            # Load data from midi file
            midi = converter.parse(filepath)
            Midi_List.append(midi)

    return Midi_List

def Notes_Extraction(Midi_List):
    Notes_List = []
    for midi in Midi_List:
        Notes = []
        # partition song with instrument
        songs = instrument.partitionByInstrument(midi)
        for part in songs.parts:
            # get access to each element
            pick = part.recurse()
            for element in pick:
                if isinstance(element, note.Note):
                    # if this element is note, then get its pitch
                    Notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    # if this element is chord, get list of order
                    # ex: chord=['c', 'e', 'g'], list=[0, 4, 7]
                    Notes.append(".".join(str(n) for n in element.normalOrder))
        if Notes:
            Notes_List.append(' '.join(Notes))

    # save as csv file
    df = pd.DataFrame(Notes_List)
    df.to_csv('Notes.csv', index=False, header=False)
    return Notes_List