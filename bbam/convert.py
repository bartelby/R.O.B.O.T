#!/home/pi/.virtualenvs/robot/bin/python
import sys
import midi2audio
from midi2audio import FluidSynth

#fluidsynth -ni sound_font.sf2 input.mid -F output.wav -r 44100

def convert_file(inf, out):
    FluidSynth('tuba.sf2', sample_rate=48000).midi_to_audio(inf, out)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print '<input filename> <output filename>'
    else:
        inf = sys.argv[1]
        out = sys.argv[2]
        convert_file(inf, out)
