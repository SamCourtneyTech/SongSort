


def get_mode(mode_index):
    #incorporate this into class later
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

def getGenre(index):
    music_genres = {
        1: "Rock",
        2: "Pop",
        3: "Hip-Hop",
        4: "Jazz",
        5: "Classical",
        6: "Country",
        7: "Electronic",
        8: "R&B",
        9: "Reggae",
        10: "Blues",
        11: "Folk",
        12: "Soul",
        13: "Metal",
        14: "Punk",
        15: "Disco",
        16: "Funk",
        17: "Gospel",
        18: "Latin",
        19: "Reggaeton",
        20: "World Music",
        21: "Alternative",
        22: "House",
        23: "Techno",
        24: "Trance",
        25: "Indie",
        26: "K-Pop",
        27: "J-Pop",
        28: "Ska",
        29: "Ambient",
        30: "New Age"
    }
    try:
        return music_genres[index]
    except KeyError:
        return "ERROR. Non existent genre."
    except:
        return "Unknown error occurred while grabbing genre"

def getSubgenre(genre, subgenre_index):
    music_subgenres = {
        1: {  # Rock
            1: "Classic Rock",
            2: "Hard Rock",
            3: "Progressive Rock",
            4: "Psychedelic Rock",
            5: "Alternative Rock",
            6: "Indie Rock",
            7: "Glam Rock",
            8: "Punk Rock",
            9: "Grunge",
            10: "Garage Rock"
        },
        2: {  # Pop
            1: "Teen Pop",
            2: "Dance Pop",
            3: "Electropop",
            4: "Synthpop",
            5: "Bubblegum Pop",
            6: "Pop Rock",
            7: "K-Pop",
            8: "J-Pop",
            9: "Latin Pop",
            10: "Europop"
        },
        3: {  # Hip-Hop
            1: "East Coast Hip-Hop",
            2: "West Coast Hip-Hop",
            3: "Trap",
            4: "Boom Bap",
            5: "Gangsta Rap",
            6: "Alternative Hip-Hop",
            7: "Conscious Hip-Hop",
            8: "Crunk",
            9: "Cloud Rap",
            10: "Drill"
        },
        4: {  # Jazz
            1: "Bebop",
            2: "Swing",
            3: "Cool Jazz",
            4: "Free Jazz",
            5: "Smooth Jazz",
            6: "Latin Jazz",
            7: "Jazz Fusion",
            8: "Modal Jazz",
            9: "Ragtime",
            10: "Dixieland"
        },
        5: {  # Classical
            1: "Baroque",
            2: "Classical Period",
            3: "Romantic Period",
            4: "Contemporary Classical",
            5: "Opera",
            6: "Chamber Music",
            7: "Choral Music",
            8: "Symphonic Music",
            9: "Minimalism",
            10: "Avant-Garde"
        },
        6: {  # Country
            1: "Bluegrass",
            2: "Honky-Tonk",
            3: "Outlaw Country",
            4: "Alternative Country",
            5: "Country Pop",
            6: "Country Rock",
            7: "Americana",
            8: "Western Swing",
            9: "Contemporary Country",
            10: "Bakersfield Sound"
        },
        7: {  # Electronic
            1: "House",
            2: "Techno",
            3: "Trance",
            4: "Drum and Bass",
            5: "Dubstep",
            6: "Ambient",
            7: "IDM",
            8: "Electro",
            9: "Downtempo",
            10: "Hardcore"
        },
        8: {  # R&B
            1: "Contemporary R&B",
            2: "Neo-Soul",
            3: "Quiet Storm",
            4: "Funk",
            5: "Soul",
            6: "New Jack Swing",
            7: "Blue-Eyed Soul",
            8: "Gospel",
            9: "Motown",
            10: "Urban Contemporary"
        },
        9: {  # Reggae
            1: "Roots Reggae",
            2: "Dub",
            3: "Dancehall",
            4: "Lovers Rock",
            5: "Ragga",
            6: "Reggaeton",
            7: "Ska",
            8: "Rocksteady",
            9: "Roots Rock",
            10: "Mento"
        },
        10: {  # Blues
            1: "Delta Blues",
            2: "Chicago Blues",
            3: "Electric Blues",
            4: "Blues Rock",
            5: "Country Blues",
            6: "Texas Blues",
            7: "Piedmont Blues",
            8: "Jump Blues",
            9: "Soul Blues",
            10: "Rhythm and Blues"
        },
        11: {  # Folk
            1: "Traditional Folk",
            2: "Contemporary Folk",
            3: "Folk Rock",
            4: "Indie Folk",
            5: "Acoustic Folk",
            6: "Folk Punk",
            7: "Americana",
            8: "Celtic Folk",
            9: "Neofolk",
            10: "Anti-Folk"
        },
        12: {  # Soul
            1: "Motown",
            2: "Northern Soul",
            3: "Southern Soul",
            4: "Neo-Soul",
            5: "Funk",
            6: "Philadelphia Soul",
            7: "Blue-Eyed Soul",
            8: "Quiet Storm",
            9: "Gospel",
            10: "Contemporary R&B"
        },
        13: {  # Metal
            1: "Heavy Metal",
            2: "Thrash Metal",
            3: "Black Metal",
            4: "Death Metal",
            5: "Power Metal",
            6: "Doom Metal",
            7: "Symphonic Metal",
            8: "Glam Metal",
            9: "Progressive Metal",
            10: "Metalcore"
        },
        14: {  # Punk
            1: "Anarcho-Punk",
            2: "Hardcore Punk",
            3: "Pop Punk",
            4: "Post-Punk",
            5: "Ska Punk",
            6: "Garage Punk",
            7: "Crust Punk",
            8: "Street Punk",
            9: "Punk Rock",
            10: "Queercore"
        },
        15: {  # Disco
            1: "Eurodisco",
            2: "Funk Disco",
            3: "Hi-NRG",
            4: "Italo Disco",
            5: "Space Disco",
            6: "Nu-Disco",
            7: "Cosmic Disco",
            8: "Boogie",
            9: "Afro-Disco",
            10: "Post-Disco"
        },
        16: {  # Funk
            1: "P-Funk",
            2: "Funk Rock",
            3: "Funk Metal",
            4: "Boogie",
            5: "G-Funk",
            6: "Psychedelic Funk",
            7: "Go-Go",
            8: "Afrobeat",
            9: "Electro Funk",
            10: "Funk Jazz"
        },
        17: {  # Gospel
            1: "Southern Gospel",
            2: "Traditional Gospel",
            3: "Urban Contemporary Gospel",
            4: "Gospel Blues",
            5: "Christian Country",
            6: "Black Gospel",
            7: "Praise & Worship",
            8: "Gospel Soul",
            9: "Contemporary Christian",
            10: "Progressive Southern Gospel"
        },
        18: {  # Latin
            1: "Salsa",
            2: "Merengue",
            3: "Bachata",
            4: "Reggaeton",
            5: "Latin Pop",
            6: "Cumbia",
            7: "Tango",
            8: "Bolero",
            9: "Samba",
            10: "Ranchera"
        },
        19: {  # Reggaeton
            1: "Old School Reggaeton",
            2: "Dembow",
            3: "Perreo",
            4: "Trapeton",
            5: "Romantic Reggaeton",
            6: "Latin Trap",
            7: "Dancehall",
            8: "Moombahton",
            9: "Reggae Fusion",
            10: "Spanish Dancehall"
        },
        20: {  # World Music
            1: "Afrobeat",
            2: "Bossa Nova",
            3: "Flamenco",
            4: "Celtic Music",
            5: "Klezmer",
            6: "Gamelan",
            7: "Soca",
            8: "Taarab",
            9: "Mbalax",
            10: "Qawwali"
        },
        21: {  # Alternative
            1: "Alternative Rock",
            2: "Indie Rock",
            3: "Post-Punk",
            4: "Shoegaze",
            5: "Grunge",
            6: "Britpop",
            7: "Emo",
            8: "Noise Rock",
            9: "Alternative Metal",
            10: "Lo-Fi"
        },
        22: {  # House
            1: "Deep House",
            2: "Tech House",
            3: "Progressive House",
            4: "Funky House",
            5: "Electro House",
            6: "Chicago House",
            7: "Soulful House",
            8: "Acid House",
            9: "Tribal House",
            10: "Microhouse"
        },
        23: {  # Techno
            1: "Detroit Techno",
            2: "Minimal Techno",
            3: "Dub Techno",
            4: "Acid Techno",
            5: "Hard Techno",
            6: "Tech House",
            7: "Industrial Techno",
            8: "Electro Techno",
            9: "Melodic Techno",
            10: "Ambient Techno"
        },
        24: {  # Trance
            1: "Progressive Trance",
            2: "Uplifting Trance",
            3: "Goa Trance",
            4: "Psytrance",
            5: "Vocal Trance",
            6: "Tech Trance",
            7: "Hard Trance",
            8: "Acid Trance",
            9: "Melodic Trance",
            10: "Dream Trance"
        },
        25: {  # Indie
            1: "Indie Rock",
            2: "Indie Pop",
            3: "Indie Folk",
            4: "Indie Electronic",
            5: "Indie Punk",
            6: "Indie Hip-Hop",
            7: "Indie Dance",
            8: "Lo-Fi Indie",
            9: "Dream Pop",
            10: "Shoegaze"
        },
        26: {  # K-Pop
            1: "K-Pop Idol",
            2: "K-Pop Hip-Hop",
            3: "K-Pop Ballad",
            4: "K-Pop Dance",
            5: "K-Pop R&B",
            6: "K-Pop Rock",
            7: "K-Pop Electro",
            8: "K-Pop Indie",
            9: "K-Pop Jazz",
            10: "K-Pop Trot"
        },
        27: {  # J-Pop
            1: "J-Pop Idol",
            2: "J-Pop Rock",
            3: "J-Pop Electro",
            4: "J-Pop Ballad",
            5: "J-Pop Dance",
            6: "J-Pop Hip-Hop",
            7: "J-Pop R&B",
            8: "City Pop",
            9: "J-Pop Folk",
            10: "J-Pop Jazz"
        },
        28: {  # Ska
            1: "Traditional Ska",
            2: "Ska Punk",
            3: "2 Tone Ska",
            4: "Third Wave Ska",
            5: "Ska Jazz",
            6: "Ska Core",
            7: "Reggae Ska",
            8: "Ska Rocksteady",
            9: "Latin Ska",
            10: "Ska Revival"
        },
        29: {  # Ambient
            1: "Dark Ambient",
            2: "Ambient Dub",
            3: "Drone",
            4: "Space Ambient",
            5: "Ambient Techno",
            6: "New Age Ambient",
            7: "Ambient House",
            8: "Psybient",
            9: "Organic Ambient",
            10: "Minimal Ambient"
        },
        30: {  # New Age
            1: "Meditative",
            2: "Ambient New Age",
            3: "Healing",
            4: "Nature Sounds",
            5: "Ethnic Fusion",
            6: "Chillout",
            7: "Spiritual",
            8: "Space Music",
            9: "World Fusion",
            10: "Neo-Classical"
            }
        }
    try:
        return music_subgenres[genre][subgenre_index]
    except KeyError:
        return "ERROR. Non existent subgenre."
    except:
        return "Unknown error occurred when grabbing subgenre"

def getLyricMood(index):
    lyricDictionary = \
    {
     0: 'Love',
     1: 'Harmony',
     2: 'Dissonance',
     3: 'Friendship',
     4: 'Enmity',
     5: 'Indifference',
     6: 'Laughter',
     7: 'Tears',
     8: 'Victory',
     9: 'Defeat',
     10: 'Gratitude',
     11: 'Entitlement',
     12: 'Restlessness',
     13: 'Cowardice',
     14: 'Optimism',
     15: 'Pessimism',
     16: 'Complexity',
     17: 'Simplicity',
     18: 'Distance',
     19: 'Intimacy',
     20: 'Magic',
     21: 'Commitment',
     22: 'Escape',
     23: 'Captivity',
     24: 'Obedience',
     25: 'Anxiety',
     26: 'Celebration',
     27: 'Idealism',
     28: 'Mourning',
     29: 'Poverty',
     30: 'Fame',
     31: 'Destiny',
     32: 'Chance',
     33: 'Madness',
     34: 'Sanity',
     35: 'Corruption',
     36: 'Wealth',
     37: 'Routine',
     38: 'Realism',
     39: 'Enlightenment',
     40: 'Liberation',
     41: 'Bondage',
     42: 'Embrace',
     43: 'Kindness',
     44: 'Integrity',
     45: 'Calm',
     46: 'Persistence',
     47: 'Folly',
     48: 'Justice',
     49: 'Injustice',
     50: 'Treachery',
     51: 'Grace',
     52: 'Knowledge',
     53: 'Empathy',
     54: 'Understanding',
     55: 'Growth',
     56: 'Oppression',
     57: 'Decay',
     58: 'Lies',
     59: 'Ignorance',
     60: 'Inspiration',
     61: 'Stagnation',
     62: 'Fulfillment',
     63: 'Emptiness',
     64: 'Acceptance',
     65: 'Rejection',
     66: 'Skepticism',
     67: 'Trust',
     68: 'Violence',
     69: 'Creation',
     70: 'Destruction',
     71: 'Lust',
     72: 'Rivalry',
     73: 'Charity',
     74: 'Honesty',
     75: 'Distrust',
     76: 'Exploration',
     77: 'Mundane',
     78: 'Adventure',
     79: 'Reality',
     80: 'Peace',
     81: 'War',
     82: 'Pain',
     83: 'Healing',
     84: 'Innocence',
     85: 'Guilt',
     86: 'Redemption',
     87: 'Isolation',
     88: 'Unity',
     89: 'Chaos',
     90: 'Order',
     91: 'Darkness',
     92: 'Light',
     93: 'Homecoming',
     94: 'Fantasy',
     95: 'Dreaming',
     96: 'Resilience',
     97: 'Fear',
     98: 'Heartbreak',
     99: 'Joy',
     100: 'Sadness',
     101: 'Nostalgia',
     102: 'Anger',
     103: 'Hope',
     104: 'Despair',
     105: 'Clarity',
     106: 'Freedom',
     107: 'Betrayal',
     108: 'Passion',
     109: 'Regret',
     110: 'Triumph',
     111: 'Loss',
     112: 'Devotion',
     113: 'Courage',
     114: 'Longing',
     115: 'Mystery',
     116: 'Confusion',
     117: 'Temptation',
     118: 'Euphoria',
     119: 'Revelation',
     120: 'Rage',
     121: 'Compassion',
     122: 'Ambition',
     123: 'Failure',
     124: 'Success',
     125: 'Sacrifice',
     126: 'Greed',
     127: 'Generosity',
     128: 'Humility',
     129: 'Pride',
     130: 'Vengeance',
     131: 'Solitude',
     132: 'Togetherness',
     133: 'Deception',
     134: 'Loyalty',
     135: 'Melancholy',
     136: 'Tradition',
     137: 'Restraint',
     138: 'Revenge',
     139: 'Forgiveness',
     140: 'Strength',
     141: 'Weakness',
     142: 'Beauty',
     143: 'Change',
     144: 'Silence',
     145: 'Ugliness',
     146: 'Turmoil',
     147: 'Patience',
     148: 'Impulse',
     149: 'Doubt',
     150: 'Noise',
     151: 'Disrespect',
     152: 'Serenity',
     153: 'Wisdom',
     154: 'Obscurity',
     155: 'Rebellion',
     156: 'Faith'
    }

    return lyricDictionary[index]

def randomVariable(index):
    import random
    # current ranges of indexes
    # mixing = 0
    # freq range 1 = 1
    # freq range 2 = 2
    # freq range 3 = 3
    # freq range 4 = 4
    # freq range 5 = 5
    # freq range 6 = 6
    # freq range 7 = 7
    # freq range 8 = 8
    # freq range 9 = 9
    # genre = 10
    # subgenre = 11
    # tempo = 12
    # mode = 13
    # lyrics = 14
    if index == 0:
        # Provide random vals for all frequency ranges
        return None
    elif index in range(1, 10):
        # Provide a random val for one frequncy range
        return None
    elif index == 10:
        # provide random val for genre
        return random.randint(1, 30)
    elif index == 11:
        # provide random val for subgenre
        return random.randint(1, 10)
    elif index == 12:
        # provide random val for tempo
        return random.randint(40, 200)
    elif index == 13:
        # provide random val for mode
        return random.randint(1, 7)
    elif index == 14:
        # provide random val for lyrics
        return random.randint(0, 156)
    elif index == 15:
        return "Haven't defined harmonic progressions bounds yet"
    elif index == 16:
        return "Haven't defined instrumentation bounds yet"
    elif index == 17:
        return "haven't defined artist bounds yet"

def probability_function(chance_percentage):
    import random
    random_value = random.uniform(0, 100)
    if random_value < chance_percentage:
        return True
    else:
        return False


User_Preferences = {
    "Mixing": {
        "Frequency Ranges": {
            "20-80hz": {"Value": 0, "Weight": 0, "Adherence": .75},
            "80-180hz": {"Value": 0, "Weight": 0, "Adherence": .75},
            "200-400hz": {"Value": 0, "Weight": 0, "Adherence": .75},
            "400-800hz": {"Value": 0, "Weight": 0, "Adherence": .75},
            "800-2400hz": {"Value": 0, "Weight": 0, "Adherence": .75},
            "2400-5500hz": {"Value": 0, "Weight": 0, "Adherence": .75},
            "5500-9000hz": {"Value": 0, "Weight": 0, "Adherence": .75},
            "9000-15000hz": {"Value": 0, "Weight": 0, "Adherence": .75},
            "15000-20000hz": {"Value": 0, "Weight": 0, "Adherence": .75}
        },
        "Weight": 0,
        "Adherence": .75
    },
    "Genre": {"Value": 0, "Weight": 0, "Adherence": .75},
    "Subgenre": {"Value": 0, "Weight": 0, "Adherence": .75},
    "Tempo": {"Value": 0, "Weight": 0, "Adherence": .75},
    "Mode": {"Value": 0, "Weight": 0, "Adherence": .75},
    "Lyrics": {"Value": 0, "Weight": 0, "Adherence": .75},
    "Harmonic Progressions": {"Value": (0), "Weight": 0, "Adherence": .75},
    #harmonic progresssion's values will be indexes that correspond to progressions. There should be able to be multiple or one progression.
    "Instrumentation": {"Value": (0), "Weight": 0, "Adherence": .75},
    #instrumentation's values will be indexes that correspond to instruments. There should be able to be multiple or one instrument.
    "Artist": {"Value": (0), "Weight": 0, "Adherence": .75}


}

Database = {"Song1":
                {"Name": "Test Song",
                    "Mixing":
                    {"Frequency Ranges": {
                        "20-80hz": 0,
                        "80-180hz": 0,
                        "200-400hz": 0,
                        "400-800hz": 0,
                        "800-2400hz": 0,
                        "2400-5500hz": 0,
                        "5500-9000hz": 0,
                        "9000-15000hz": 0,
                        "15000-20000hz": 0}},
                 "Genre": 0,
                 "Subgenre": 0,
                 "Tempo": 0,
                 "Mode": 0,
                 "Lyrics": 0},
            "Song2":
                {"Name": "Test Song 2",
                 "Mixing":
                     {"Frequency Ranges": {
                         "20-80hz": 0,
                         "80-180hz": 0,
                         "200-400hz": 0,
                         "400-800hz": 0,
                         "800-2400hz": 0,
                         "2400-5500hz": 0,
                         "5500-9000hz": 0,
                         "9000-15000hz": 0,
                         "15000-20000hz": 0}},
                 "Genre": 0,
                 "Subgenre": 0,
                 "Tempo": 0,
                 "Mode": 0,
                 "Lyrics": 0,
                 "Harmonic Progressions": (0),
                 "Instrumentation": (0),
                 "Artist": 0
                 }
            }


def perfect_sort(user_pref, database):
    frequency_ranges = [
        "20-80hz",
        "80-180hz",
        "200-400hz",
        "400-800hz",
        "800-2400hz",
        "2400-5500hz",
        "5500-9000hz",
        "9000-15000hz",
        "15000-20000hz"
    ]

    #pefect match means all 14 variables of user preferences are met
    for song in database:
        checks = 0
        for freq_range in frequency_ranges:
            if database[song]["Mixing"]["Frequency Ranges"][freq_range] == user_pref["Mixing"]["Frequency Ranges"][freq_range]["Value"]:
                checks += 1
        for var in database[song]:
            try:
                if database[song][var] == user_pref[var]["Value"]:
                    checks += 1
            except KeyError:
                continue
        if checks == 14:
            return database[song]["Name"]


    if user_pref["Mixing"]["Frequency Ranges"]["20-80hz"]:
        None
    return None

def adherence_sort(user_pref, database):
    frequency_ranges = [
        "20-80hz",
        "80-180hz",
        "200-400hz",
        "400-800hz",
        "800-2400hz",
        "2400-5500hz",
        "5500-9000hz",
        "9000-15000hz",
        "15000-20000hz"
    ]

    params = [
        user_pref["Mixing"]["Adherence"],
        user_pref["Mixing"]["Frequency Ranges"]["20-80hz"]["Adherence"],
        user_pref["Mixing"]["Frequency Ranges"]["80-180hz"]["Adherence"],
        user_pref["Mixing"]["Frequency Ranges"]["200-400hz"]["Adherence"],
        user_pref["Mixing"]["Frequency Ranges"]["400-800hz"]["Adherence"],
        user_pref["Mixing"]["Frequency Ranges"]["800-2400hz"]["Adherence"],
        user_pref["Mixing"]["Frequency Ranges"]["2400-5500hz"]["Adherence"],
        user_pref["Mixing"]["Frequency Ranges"]["5500-9000hz"]["Adherence"],
        user_pref["Mixing"]["Frequency Ranges"]["9000-15000hz"]["Adherence"],
        user_pref["Mixing"]["Frequency Ranges"]["15000-20000hz"]["Adherence"],
        user_pref["Genre"]["Adherence"],
        user_pref["Subgenre"]["Adherence"],
        user_pref["Tempo"]["Adherence"],
        user_pref["Mode"]["Adherence"],
        user_pref["Lyrics"]["Adherence"],
        user_pref["Harmonic Progressions"]["Adherence"],
        user_pref["Instrumentation"]["Adherence"],
        user_pref["Artist"]["Adherence"]
    ]

    mixingProb = params[0]
    FrangeOneProb = params[1]
    FrangeTwoProb = params[2]
    FrangeThreeProb = params[3]
    FrangeFourProb = params[4]
    FrangeFiveProb = params[5]
    FrangeSixProb = params[6]
    FrangeSevenProb = params[7]
    FrangeEightProb = params[8]
    FrangeNineProb = params[9]
    genreProb = params[10]
    subgenreProb = params[11]
    tempoProb = params[12]
    modeProb = params[13]
    lyricsProb = params[14]
    harmonicProb = params[15]
    instrumentProb = params[16]
    artistProb = params[17]



    #for each probability, perform x-probability that x variable will be that genre
    #if result is True, then set target song to have that parameter. If negative,
    #set target song to have a random parameter (Maybe in the future, it'll be the next most likely variable
    willAdhere = [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True
    ]



    for i in range(len(params)):
        None




def weighted_sort(user_pref, database):

    frequency_ranges = [
        "20-80hz",
        "80-180hz",
        "200-400hz",
        "400-800hz",
        "800-2400hz",
        "2400-5500hz",
        "5500-9000hz",
        "9000-15000hz",
        "15000-20000hz"
    ]

    params = [
        user_pref["Mixing"]["Weight"],
        user_pref["Mixing"]["Frequency Ranges"]["20-80hz"]["Weight"],
        user_pref["Mixing"]["Frequency Ranges"]["80-180hz"]["Weight"],
        user_pref["Mixing"]["Frequency Ranges"]["200-400hz"]["Weight"],
        user_pref["Mixing"]["Frequency Ranges"]["400-800hz"]["Weight"],
        user_pref["Mixing"]["Frequency Ranges"]["800-2400hz"]["Weight"],
        user_pref["Mixing"]["Frequency Ranges"]["2400-5500hz"]["Weight"],
        user_pref["Mixing"]["Frequency Ranges"]["5500-9000hz"]["Weight"],
        user_pref["Mixing"]["Frequency Ranges"]["9000-15000hz"]["Weight"],
        user_pref["Mixing"]["Frequency Ranges"]["15000-20000hz"]["Weight"],
        user_pref["Genre"]["Weight"],
        user_pref["Subgenre"]["Weight"],
        user_pref["Tempo"]["Weight"],
        user_pref["Mode"]["Weight"],
        user_pref["Lyrics"]["Weight"],
        user_pref["Harmonic Progressions"]["Weight"],
        user_pref["Instrumentation"]["Weight"],
        user_pref["Artist"]["Weight"]
    ]
    values = [
        0,
        user_pref["Mixing"]["Frequency Ranges"]["20-80hz"]["Value"],
        user_pref["Mixing"]["Frequency Ranges"]["80-180hz"]["Value"],
        user_pref["Mixing"]["Frequency Ranges"]["200-400hz"]["Value"],
        user_pref["Mixing"]["Frequency Ranges"]["400-800hz"]["Value"],
        user_pref["Mixing"]["Frequency Ranges"]["800-2400hz"]["Value"],
        user_pref["Mixing"]["Frequency Ranges"]["2400-5500hz"]["Value"],
        user_pref["Mixing"]["Frequency Ranges"]["5500-9000hz"]["Value"],
        user_pref["Mixing"]["Frequency Ranges"]["9000-15000hz"]["Value"],
        user_pref["Mixing"]["Frequency Ranges"]["15000-20000hz"]["Value"],
        user_pref["Genre"]["Value"],
        user_pref["Subgenre"]["Value"],
        user_pref["Tempo"]["Value"],
        user_pref["Mode"]["Value"],
        user_pref["Lyrics"]["Value"],
        user_pref["Harmonic Progressions"]["Value"],
        user_pref["Instrumentation"]["Value"],
        user_pref["Artist"]["Value"]
    ]

    mixingWeight = params[0]
    FrangeOneWeight = params[1]
    FrangeTwoWeight = params[2]
    FrangeThreeWeight = params[3]
    FrangeFourWeight = params[4]
    FrangeFiveWeight = params[5]
    FrangeSixWeight = params[6]
    FrangeSevenWeight = params[7]
    FrangeEightWeight = params[8]
    FrangeNineWeight = params[9]
    genreWeight = params[10]
    subgenreWeight = params[11]
    tempoWeight = params[12]
    modeWeight = params[13]
    lyricsWeight = params[14]
    harmonicWeight = params[15]
    instrumentWeight = params[16]
    artistWeight = params[17]

    # for each probability, perform x-probability that x variable will considered
    considerWeight = []
    for weight in params:
        considerWeight.append(probability_function(weight))

    target_song = []
    skipMi xing = False
    for i in range(0, len(params)):
        if skipMixing and i < 10:
            target_song.append(randomVariable(i))
        elif not considerWeight[i]:
            if i == 0:
                skipMixing = True
                continue
            target_song.append(randomVariable(i))
        elif i == 0:
            continue
        else:
            target_song.append(values[i])
    #Make target song into similar database to user pref?
    for song in database:
        index = 0
        checks = 0
        for freq_range in frequency_ranges:
            if database[song]["Mixing"]["Frequency Ranges"][freq_range] == target_song[index]:
                checks += 1
                index += 1
        for var in database[song]:
            try:
                if database[song][var] == user_pref[var]["Value"]:
                    checks += 1
            except KeyError:
                continue
        if checks == 14:
            return database[song]["Name"]
        #The sorting algorithm will eventually need some version of logarithmic search to stay efficient



print(weighted_sort(User_Preferences, Database))

