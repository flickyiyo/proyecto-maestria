import midi
import os
import pathlib

def convert_midi_files(dir_name):
    files = os.listdir(dir_name)
    samples = {}
    for f in files:
        if f.endswith('.mid') or f.endswith('.midi'):
            try:
                samples[f] = midi.midi_to_samples(os.path.abspath(dir_name + '/' + f))
            except:
                print('Failed to parse: ' + f)
    
    return samples
