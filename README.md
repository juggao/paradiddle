# paradiddle
Generates a MIDI file with drum paradiddles from a text with "LRRLLRRR" 

Download the pama.py statemachine from my dfa repository
Download the dfa.py statemachine from my dfa repository

Install rosegarden to play the generated midifile in 155 BPM

usage: l2randmidi.py [-h] [-b BPM] [-v VERBOSE] filename

Generates a MIDI file from a "LLRRLLLRR" string

positional arguments:
  filename

options:
  -h, --help            show this help message and exit
  -b BPM, --bpm BPM
  -v VERBOSE, --verbose VERBOSE


Example:

$ python pama.py dfa.py | python lr.py | python lr2randmidi.py | rosegarden about.mid

