import argparse
from utils.midi_utils import read_midi, write_midi

parser = argparse.ArgumentParser(description="Generate new music")
parser.add_argument('--midi', type=str, help="The name of the midi file to use as input")
args = parser.parse_args()

if __name__=="__main__":
    print("Midi file = {}".format(args.midi))
    midi_contents = read_midi(args.midi)
    print(len(midi_contents['notes']))
    print(len(midi_contents['durations']))

    midi_contents = {
        'notes': ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3'],
        'durations': [1,1,1,1,1,1,1,1]
    }
    write_midi(midi_contents, 'trial.mid')