import math
import numpy as np
import scipy as sp
from wave_helper import *
import matplotlib.pyplot as plt
import PIL
import copy
from wave_editor import *

MAX_VOL = 32767
MIN_VOL = -32768
PI = math.pi


# A #


def build_melody(note_list):
    list_of_melody = []
    # check if valid (note_list)
    for i in range(0,len(note_list),2):
        if (note_list[i] == 'Q'):
            current_note = build_empty(int(note_list[i+1]))
        else:
            current_note = build_note(note_list[i],int(note_list[i+1]))
        list_of_melody += current_note
    return list_of_melody

def build_note (note,length):
    freq_of_note = note_to_freq(note)
    spc = (2000/freq_of_note)

    note_list = []
    for i in range (int(length*(2000/16))):
        note_list.append([sample_i(i,spc), sample_i(i,spc)])
    return note_list

def build_empty(length):
    empty_note = []
    for i in range(int(length*(2000/16))):
        empty_note.append([0,0])
    return empty_note

def sample_i(i,spc):
    return int(MAX_VOL*math.sin((2*PI)*(i/spc)))

def note_to_freq(note):
    if note == 'A':
        return 440
    elif note == 'B':
        return 494
    elif note == 'C':
        return 523
    elif note == 'D':
        return 587
    elif note == 'E':
        return 659
    elif note == 'F':
        return 698
    elif note == 'G':
        return 784


def read_melody (filepath):
    melody_file = open(filepath, 'r')
    text_in_file = list(melody_file.read())
    clean_melody_list = []
    for i in range (len(text_in_file)):
        if text_in_file[i] != ' ' and text_in_file[i] != '\n':
            clean_melody_list.append(text_in_file[i])
    return clean_melody_list

melody_lst = (read_melody('/cs/usr/roeyby/Desktop/ex6/Composition_Samples/sample2.txt'))

melody = build_melody(melody_lst)
save_wave(2000,melody,'melody23')


# A = build_note('G',1)
# print (A)
# list_melody1 = ['A',16,'B',8,'C',16,'D',8,'E',16,'Q',32,'D',8,'G',8,'A',12,'E',22]
# list_melody2 = ['A',16,'A',8,'A',16,'F',8,'G',16,'Q',32,'F',8,'B',8]
# melody1 = [2000,build_melody(list_melody1)]
# melody2 = [2000,build_melody(list_melody2)]
#
# print(melody1)
#
# melody = unite_waves(melody1,melody2)
#
# print(melody)
# print(save_wave(2000,melody[1],'melody'))

