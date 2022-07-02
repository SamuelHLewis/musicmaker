from music21 import note, chord, converter

def read_midi(midi:str) -> dict:
    """Read a midi file and extract the notes and pitches.
    Args:
        midi: the name of the midi file.
    Returns:
        midi_contents: the notes and pitches from the midi file.
    """
    notes = []
    durations = []
    parser = converter

    original_score = parser.parse(midi).chordify()
    
    for element in original_score.flat:
        if isinstance(element, note.Note):
            if element.isRest:
                notes.append(str(element.name))
                durations.append(element.duration.quarterLength)
            else:
                notes.append(str(element.nameWithOctave))
                durations.append(element.duration.quarterLength)
        
        if isinstance(element, chord.Chord):
            notes.append('.'.join(n.nameWithOctave for n in element.pitches))
            durations.append(element.duration.quarterLength)
    
    midi_contents = {
        'notes': notes,
        'durations': durations
    }

    return midi_contents