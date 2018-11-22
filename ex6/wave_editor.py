import scipy as sp
import numpy as np
from wave_helper import *


MAX_VOL = 32767
MIN_VOL = -32768



def reverse_wave(wave):
    reversed_wave = [wave[0],[]]
    for index in range ((len(wave[1]))-1,-1,-1):
        reversed_wave[1].append(wave[1][index])
    return reversed_wave


def accelerate_wave(wave):
    acc_wave = [wave[0],[]]
    for index in range (0,len(wave[1]),2):
        acc_wave[1].append(wave[1][index])
    return acc_wave


def slow_wave(wave):
    slow_wave = [wave[0],[]]
    for index in range (len(wave[1])-1):
        slow_wave[1].append(wave[1][index])
        avg_tup = avg_of_tups(wave[1][index],wave[1][index+1])
        slow_wave[1].append(avg_tup)
    slow_wave[1].append(wave[1][len(wave[1])-1])
    return slow_wave


def avg_of_tups (tup1,tup2):
    avg_tup = []
    avg_tup.append((tup1[0]+tup2[0])/2)
    avg_tup.append((tup1[1]+tup2[1])/2)
    return avg_tup


def inc_vol (wave):
    loud_wave = [wave[0],[]]
    for tupple in wave[1]:
        amp_tup = amplify_tup(tupple)
        loud_wave[1].append(amp_tup)
    return loud_wave


def amplify_tup(tup):
    amp_tup = []
    amp_tup1 = int(1.2*tup[0])
    amp_tup2 = int(1.2*tup[1])

    if amp_tup1 > MAX_VOL:
        amp_tup1 = MAX_VOL
    elif amp_tup1 < MIN_VOL:
        amp_tup1 = MIN_VOL

    if amp_tup2 > MAX_VOL:
        amp_tup2 = MAX_VOL
    elif amp_tup2 < MIN_VOL:
        amp_tup2 = MIN_VOL

    amp_tup.append(amp_tup1)
    amp_tup.append(amp_tup2)
    return amp_tup



def dec_vol (wave):
    quiet_wave = [wave[0],[]]
    for tupple in wave[1]:
        qui_tup = quiet_tup(tupple)
        quiet_wave[1].append(qui_tup)
    return quiet_wave


def quiet_tup(tup):
    qui_tup = []

    qui_tup1 = int(tup[0]/1.2)
    qui_tup2 = int(tup[1]/1.2)

    qui_tup.append(qui_tup1)
    qui_tup.append(qui_tup2)

    return qui_tup


def muf_sound (wave):

    muf_wave = [wave[0],[]]

    muf_wave[1].append(avg_of_2_tups(wave[1][0],wave[1][1]))
    for index in range (1,len(wave[1])-1):
        muf_tup = avg_of_3_tups(wave[1][index-1],wave[1][index],wave[1][index+1])
        muf_wave[1].append(muf_tup)
    muf_wave[1].append(avg_of_2_tups(wave[1][len(wave[1])-1],wave[1][len(wave[1])-2]))
    return muf_wave


def avg_of_3_tups (tup1,tup2,tup3):
    avg_tup = []
    avg_tup1 = int((tup1[0]+tup2[0]+tup3[0])/3)
    avg_tup2 = int((tup1[1]+tup2[1]+tup3[1])/3)

    avg_tup.append(avg_tup1)
    avg_tup.append(avg_tup2)
    return avg_tup


