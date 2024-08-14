

#Just a function to retrieve the name of the mode we are looking at. (Modes will be indexed from 0-6

def get_mode(mode_index):
    modes = {
        0: "Ionian",
        1: "Dorian",
        2: "Phrygian",
        3: "Lydian",
        4: "Mixolydian",
        5: "Aeolian",
        6: "Locrian"
    }
    return modes[mode_index]