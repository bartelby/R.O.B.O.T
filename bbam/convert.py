# This script does this:
#fluidsynth -ni sound_font.sf2 input.mid -F output.wav -r 44100

import sys
from midi2audio import FluidSynth as fs

def convert(infile, outfile):
    fs('home/pi/.fluidsynth/tuba.sf2').midi_to_audio(infile, outfile)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print '<input filename> <output filename>'
    else:
        inf = sys.argv[1]
        out = sys.argv[2]
        convert(inf, out)
