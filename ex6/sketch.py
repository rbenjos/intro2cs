import scipy as sp
import numpy as np

from wave_helper import *
import math

MAX_VOL = 32767
MIN_VOL = -32768

seinfeld = load_wave('seinfeld.wav')

batman = load_wave('batman_theme_x.wav')


# print(seinfeld[0])
#
# print len(seinfeld[1])
#
#
#
# print(seinfeld[1])
#
# save_wave(seinfeld[0],reverse_seinfeld,'reverse_seinfeld.wav')

# print(save_wave(seinfeld[0],reverse_seinfeld,'reverse_seinfeld.wav'))


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
        avg_tup = avg_of_2_tups(wave[1][index], wave[1][index + 1])
        slow_wave[1].append(avg_tup)
    slow_wave[1].append(wave[1][len(wave[1])-1])
    return slow_wave


def avg_of_2_tups (tup1, tup2):
    avg_tup = []
    avg_tup.append(int((tup1[0]+tup2[0])/2))
    avg_tup.append(int((tup1[1]+tup2[1])/2))
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

def norm_fr_rate (wave1,wave2):
    if (wave1[0]>wave2[0]):
        norm_wave1 = build_norm_wave(wave1, wave2)
        norm_wave2 = wave2
    elif (wave2[0]>wave1[0]):
        norm_wave2 = build_norm_wave(wave2, wave1)
        norm_wave1 = wave1
    else:
        norm_wave1 = wave1
        norm_wave2 = wave2
    return norm_wave1,norm_wave2

def build_norm_wave (big_wave, small_wave):
    normalized_wave = [small_wave[0],[]]
    gcd = math.gcd(big_wave[0],small_wave[0])
    big_gcd_ratio = int(big_wave[0]/gcd)
    small_gcd_ratio = int(small_wave[0]/gcd)
    for index1 in range(0,len(big_wave[1]),big_gcd_ratio):
        for index2 in range(small_gcd_ratio):
            if (index1+index2) > len(big_wave[1])-1:
                break
            else:
                normalized_wave[1].append(big_wave[1][index1+index2])
    return normalized_wave


def unite_waves (wave1, wave2):
    norm_wav1,norm_wav2 = norm_fr_rate(wave1,wave2)
    if len(norm_wav1[1])>=len(norm_wav2[1]):
        uni_wave = uni_norm_waves(norm_wav1, norm_wav2)
    else:
        uni_wave = uni_norm_waves(norm_wav2,norm_wav1)
    return uni_wave

def uni_norm_waves(big_wave, small_wave):
    uni_wave = [big_wave[0],[]]
    for index1 in range(len(small_wave[1])):
        avg_tup = avg_of_2_tups(big_wave[1][index1], small_wave[1][index1])
        uni_wave[1].append(avg_tup)
    for index2 in range(len(small_wave[1]), len(big_wave[1])):
        uni_wave[1].append(big_wave[1][index2])
    return uni_wave

#
#
# list_of_tups1 = [2,[[20,20],[40,40],[60,60],[80,80],[100,100]]]
# list_of_tups2 = [3,[[1,1],[3,3],[5,5],[7,7],[9,9],[11,11],[13,13],[15,15],[17,17],[19,19]]]

list_of_tups3 =[5500,[[10,10],[20,20],[30,30],[40,40],[50,50],[60,60],[70,70],[80,80],[90,90],[100,100]]]
list_of_tups4 = [2200,[[0,0],[0,0],[0,0],[0,0]]]



rev_sein = reverse_wave(seinfeld)
uni_sein_rev = unite_waves(seinfeld,rev_sein)

save_wave(uni_sein_rev[0],uni_sein_rev[1],'uni_sein_rev')


#
# math.gcd()
# muf_seinfeld = muf_sound(seinfeld)
#
# print(len(muf_seinfeld[1]),len(seinfeld[1]))
# print (muf_seinfeld[1])
# print(seinfeld[1])
#
# save_wave(muf_seinfeld[0],muf_seinfeld[1],'muffeled_seinfeld')

# tup1= (10,10)
# tup2= (20,20)
# tup3 = (30,30)
#
# print(avg_of_3_tups(tup1,tup2,tup3))

#
# quiet_seinfeld = dec_vol(seinfeld)
#
# save_wave(quiet_seinfeld[0],quiet_seinfeld[1],'quiet_seinfeld')


#
# loud_seinfeld = inc_vol(seinfeld)
#
# save_wave(loud_seinfeld[0],loud_seinfeld[1],'loud_seinfeld')

#
# reverse_seinfeld = reverse_wave(seinfeld)
#
# print (save_wave(reverse_seinfeld[0],reverse_seinfeld[1],'reverse_seinfeld'))
#
# fast_seinfeld = accelerate_wave(seinfeld)
#
# print (save_wave(fast_seinfeld[0],fast_seinfeld[1],'fast_seinfeld'))
#
# slow_seinfeld = slow_wave(seinfeld)
#
# print (save_wave(slow_seinfeld[0], slow_seinfeld[1], 'slow_seinfeld'))
#
#
# print(len(slow_seinfeld[1]),len(seinfeld[1]))
