#!/usr/bin/python3

import argparse

import os
from gtts import gTTS
from pydub import AudioSegment

from tabulate import tabulate

parser = argparse.ArgumentParser(description='Pytness creates an mp3 audio file which speaks at regular intervals.')
parser.add_argument('-e', '--exercise', type=str, default="exercise", help='name of the exercise/audiofile.')
parser.add_argument('-a', '--alternate', type=bool, default=False, help='if given, the exercise alternates left and right')
parser.add_argument('-d', '--seconds', type=int, default=3, help='duration of each repetition')
parser.add_argument('-r', '--rest', type=int, default=2, help='seconds of rest after each repetition')
parser.add_argument('-n', '--reps', type=int, default=10, help='number of repetitions')
parser.add_argument('-s', '--series', type=int, default=1, help='number of series (between 0 and 9)')
parser.add_argument('-c', '--change-side', type=int, default=5, help='seconds allowed for changing side')

def say(text):
    # There must be a better way to do this without creating and deleting the dummyfile
    tts = gTTS(text, lang='en')
    tts.save("_dummyfile")
    audiosegment = AudioSegment.from_file("_dummyfile")
    os.remove("_dummyfile")
    return audiosegment

def perform(session, exercise):
    for i in range(series):
        session = session + number[i] + sec

        if alternate:
            session = session + left
            session = session + sec*change_side
            session = repeat(session, exercise)
            session = session + right
            session = session + sec*change_side
            session = repeat(session, exercise)
        else:
            session = repeat(session, exercise)
    return session

def repeat(session, exercise):
    for rep in range(reps):
        session = session + start
        session = session + sec*seconds
        session = session + stop
        session = session + sec*rest
    return session

if __name__ == "__main__":
    args = parser.parse_args()

    exercise = args.exercise
    alternate = args.alternate
    seconds = args.seconds
    rest = args.rest
    reps = args.reps
    series = args.series
    change_side = args.change_side

    headers = ['exercise', 'alternate', 'seconds', 'rest', 'reps', 'series', 'change side']
    values = [[exercise, alternate, seconds, rest, reps, series, change_side]]
    print(tabulate(values, headers=headers))

    sec = AudioSegment.silent(duration=1000)
    start =  say("start")
    stop =  say("stop")
    left = say("left")
    right = say("right")
    number = [say(num) for num in ["zero","one","two","three","four","five","six","seven","eight","nine"]]

    session = say(exercise) + sec

    session = perform(session, exercise)

    session.export(exercise + ".mp3", format="mp3")
