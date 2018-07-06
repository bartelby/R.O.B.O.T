#!/home/pi/.virtualenvs/robot/bin/python
import sys
import midi2audio
from midi2audio import FluidSynth

def play(filename):
    FluidSynth('/home/pi/.fluidsynth/tuba.sf2', sample_rate=48000).play_midi(filename)

if __name__ == '__main__':
        if len(sys.argv) < 2:
            print "Enter the name of your piece"
        else:
            filename = sys.argv[1]
            play(filename)
