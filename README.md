# paradiddle
Generates a MIDI file with drum paradiddles from a text with "LRRLLRRR" 

Download the pama.py statemachine from my dfa repository
Download the dfa.py statemachine from my dfa repository

Install rosegarden to play the generated midifile (default = 155 BPM)



python lr2randmidi.py -h
usage: l2randmidi.py [-h] [-f FILENAME] [-b BPM] [-v VERBOSE] [-o OUTPUT]

Generates a MIDI file from a "LLRRLLLRR" string

options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
  -b BPM, --bpm BPM
  -v VERBOSE, --verbose VERBOSE
  -o OUTPUT, --output OUTPUT

(c) 2023 René Oudeweg




Example:

$ python pama.py dfa.py | python lr.py | python lr2randmidi.py -b 220 | rosegarden about.mid

