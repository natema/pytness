# Pytness

This is a Python program that produces an audio file in mp3 format, in order to guide you during the performance of some physical exercise repetition.

More generally, it should come in handy in any scenario in which you would like to hear some verbal instructions repeated according to some scheme. 

The program uses Google's TTS API to synthesize the spoken words. 


## Requirements  

`pytness.py` uses the Python modules `gtts`, `tabulate` and `pydub`. You can install them with `pip`

	pip install gtts tabulate pydub

You'll also need `ffmpeg`. On Debian-based distros you can install it with 

	sudo apt install ffmpeg -y

## Usage

You can get some basic instructions on how to use the program by running it with the `-h` flag:

```
# ./pytness.py -h                 
usage: pytness.py [-h] [-e EXERCISE] [-a ALTERNATE] [-d SECONDS] [-r REST] [-n REPS] [-s SERIES] [-c CHANGE_SIDE]

Pytness creates an mp3 audio file which speaks at regular intervals.

optional arguments:
  -h, --help            show this help message and exit
  -e EXERCISE, --exercise EXERCISE
                        name of the exercise/audiofile.
  -a ALTERNATE, --alternate ALTERNATE
                        if given, the exercise alternates left and right
  -d SECONDS, --seconds SECONDS
                        duration of each repetition
  -r REST, --rest REST  seconds of rest after each repetition
  -n REPS, --reps REPS  number of repetitions
  -s SERIES, --series SERIES
                        number of series (between 0 and 9)
  -c CHANGE_SIDE, --change-side CHANGE_SIDE
                        seconds allowed for changing side
```


That said, the program should be simple enough to easily allow someone with some programming experience to adapt it.