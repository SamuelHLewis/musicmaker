import argparse
from utils.midi_utils import read_midi

parser = argparse.ArgumentParser(description="Generate new music")
parser.add_argument('--midi', type=str, help="The name of the midi file to use as input")
args = parser.parse_args()

if __name__=="__main__":
    print("Midi file = {}".format(args.midi))
    midi_contents = read_midi(args.midi)
    print(len(midi_contents['notes']))
    print(len(midi_contents['durations']))