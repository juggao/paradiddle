from midiutil import MIDIFile
import random

#Key# Note Drum Sound Key# Note Drum Sound
#35 B0 Acoustic Bass Drum 59 B2 Ride Cymbal 2
#36 C1 Bass Drum 1 60 C3 Hi Bongo
#37 C#1 Side Stick 61 C#3 Low Bongo
#38 D1 Acoustic Snare 62 D3 Mute Hi Conga
#39 Eb1 Hand Clap 63 Eb3 Open Hi Conga
#40 E1 Electric Snare 64 E3 Low Conga
#41 F1 Low Floor Tom 65 F3 High Timbale
#42 F#1 Closed Hi Hat 66 F#3 Low Timbale
#43 G1 High Floor Tom 67 G3 High Agogo
#44 Ab1 Pedal Hi-Hat 68 Ab3 Low Agogo
#45 A1 Low Tom 69 A3 Cabasa
#46 Bb1 Open Hi-Hat 70 Bb3 Maracas
#47 B1 Low-Mid Tom 71 B3 Short Whistle
#48 C2 Hi Mid Tom 72 C4 Long Whistle
#49 C#2 Crash Cymbal 1 73 C#4 Short Guiro
#50 D2 High Tom 74 D4 Long Guiro
#51 Eb2 Ride Cymbal 1 75 Eb4 Claves
#52 E2 Chinese Cymbal 76 E4 Hi Wood Block
#53 F2 Ride Bell 77 F4 Low Wood Block
#54 F#2 Tambourine 78 F#4 Mute Cuica
#55 G2 Splash Cymbal 79 G4 Open Cuica
#56 Ab2 Cowbell 80 Ab4 Mute Triangle
#57 A2 Crash Cymbal 2 81 A4 Open Triangle
#58 Bb2 Vibraslap

def translate_to_midi(text, output_file):
    # Set up MIDI parameters
    track = 0
    channel = 10
    time = 1  # In beats
    duration = 0.25  # In beats
    tempo = 155  # In BPM
    volume = 100  # 0-127, as per MIDI standard

    # Create MIDIFile object with 1 track
    midi = MIDIFile(1)
    midi.addTempo(track, time, tempo)

    # Map 'L' and 'R' to MIDI notes
#    notes = {'L': 38, 'R': 40}
    random.seed(5)
    
    # Convert text to MIDI notes
    for char in text:
        if char == 'L' or char == 'R':   
            note = random.randint(35,81)
            random_volume = random.randint(68, 100)
            midi.addNote(track, channel, note, time, duration, random_volume)
            time += duration

    # Write MIDI data to file
    with open(output_file, 'wb') as file:
        midi.writeFile(file)

# Example usage
import sys

# Check if filename is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the filename as a command-line argument.")
    sys.exit(1)

filename = sys.argv[1]
try:
    with open(filename, 'r') as file:
        lrstring = file.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")
            
output_file = 'snare_drum.mid'
print(lrstring)
translate_to_midi(lrstring, output_file)

