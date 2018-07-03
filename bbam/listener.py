import midi
from midi import sequencer
import sys

CLIENT = 20
PORT   = 0
PLAY = True

seq = sequencer.SequencerRead(sequencer_resolution=128)
seq.subscribe_port(CLIENT, PORT)
seq.start_sequencer()

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
    port = get_port()
    try:
        while True:
            event = read_event()
            if event:
                evtyp = event.name
                tick = event.tick 
                velocity = event.velocity 
                pitch = event.pitch
                track.append(event)
                if port and port.isOpen():
                    port.write(event)
                print(evtyp, 'tick:%s' % tick, 'velocity: %s' % velocity, 'pitch: %s' % pitch)
    finally:
        eot = midi.EndOfTrackEvent(tick=1)
        if pattern and track:
            track.append(eot)
            if port and port.isOpen():
                port.write(eot)
                port.close()
            midi.write_midifile(filename, pattern)
        else:
            print "S:omething's All Fucked Up."

def get_port():
    port =serial.Serial(
                "/dev/ttyUSB0",
                baudrate=57600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                writeTimeout = 0,
                timeout = 10,
                rtscts=False,
                dsrdtr=False,
                xonxoff=False)
    return port

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Enter the name of your piece"
    else:
        filename = sys.argv[1]
        record(filename)


