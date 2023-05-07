import csv
import argparse
from preprocess import *

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--read-csv', action='store_true', help='to read notes from csv file, default=False')
    parser.set_defaults(read_csv=False)
    args = parser.parse_args()
    return args.read_csv

if __name__ == '__main__':
    # determine whether to get notes from csv and remove frequency
    read_csv = get_argument()

    Notes_List = []
    if read_csv:
        # read notes from csv
        with open("Notes.csv", "r") as f:
            reader = csv.reader(f, delimiter="\n")
            for Notes in reader:
                Notes_List.append(Notes[0])
    else:
        # load midi files
        Midi_List = Load_Dataset()
        # extract notes and saves in Notes.csv
        Notes_List = Notes_Extraction(Midi_List)

