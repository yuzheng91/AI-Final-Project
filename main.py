import csv
import argparse
from preprocess import *

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
    Notes_Index_List = Notes_to_Index(Notes_List)