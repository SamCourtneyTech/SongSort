

#Just a function to retrieve the name of the mode we are looking at. (Modes will be indexed from 0-6

def get_mode(mode_index):
    modes = {
        1: "Ionian",
        2: "Dorian",
        3: "Phrygian",
        4: "Lydian",
        5: "Mixolydian",
        6: "Aeolian",
        7: "Locrian"
    }
    return modes[mode_index]