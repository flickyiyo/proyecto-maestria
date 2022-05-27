import midi
import os
import pathlib

def convert_midi_files(dir_name):
    files = os.listdir(dir_name)
    samples = []
    for f in files:
        if f.endswith('.mid') or f.endswith('.midi'):
            try:
                samples.append(midi.midi_to_samples(os.path.abspath(dir_name + '/' + f)))
            except:
                print('Failed to parse: ' + f)
    measures = []
    for sample in samples:
        for measure in sample:
            measures.append(measure)
    return measures
