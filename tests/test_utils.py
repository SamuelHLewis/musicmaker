from utils.midi_utils import read_midi

def test_read_midi_lengths():
    """Test that each note has an accompanying duration value"""
    midi_contents = read_midi('./data/entertainer.mid')
    assert len(midi_contents['notes']) == len(midi_contents['durations'])