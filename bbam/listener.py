import midi
from midi import sequencer
import sys

CLIENT = 20
PORT   = 0
PLAY = True

seq = sequencer.SequencerRead(sequencer_resolution=128)
seq.subscribe_port(CLIENT, PORT)
seq.start_sequencer()

wseq = sequencer.SequencerWrite(sequencer_resolution=128)
wseq.subscribe_port(CLIENT, PORT)
wseq.start_sequencer()

def read_event():
    event = seq.event_read()
    return event

def stop_events():
    global PLAY
    PLAY = False
    
def record(filename):
    pattern = midi.Pattern()
    track = midi.Track()
    pattern.append(track)
    try:
        while True:
            event = read_event()
            if event:
                evtyp = event.name
                tick = event.tick 
                velocity = event.velocity 
                pitch = event.pitch
                track.append(event)
                print(evtyp, 'tick:%s' % tick, 'velocity: %s' % velocity, 'pitch: %s' % pitch)
                buf = wseq.event_write(event, False, False, True)
    finally:
        eot = midi.EndOfTrackEvent(tick=1)
        if pattern and track:
            track.append(eot)
            midi.write_midifile(filename, pattern)
        else:
            print "S:omething's All Fucked Up."

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Enter the name of your piece"
    else:
        filename = sys.argv[1]
        record(filename)


