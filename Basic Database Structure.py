


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






User_Preferences = {
    "Mixing": {
        "Frequency Ranges": {
            "20-80hz": {"Val": 0, "Weight": 0, "Adherence": 0},
            "80-180hz": {"Val": 0, "Weight": 0, "Adherence": 0},
            "200-400hz": {"Val": 0, "Weight": 0, "Adherence": 0},
            "400-800hz": {"Val": 0, "Weight": 0, "Adherence": 0},
            "800-2400hz": {"Val": 0, "Weight": 0, "Adherence": 0},
            "2400-5500hz": {"Val": 0, "Weight": 0, "Adherence": 0},
            "5500-9000hz": {"Val": 0, "Weight": 0, "Adherence": 0},
            "9-15khz": {"Val": 0, "Weight": 0, "Adherence": 0},
            "15-20khz": {"Val": 0, "Weight": 0, "Adherence": 0}
        },
        "Weight": 0,
        "Adherence": 0
    },
    "Genre": {"Value": 0, "Weight": 0, "Adherence": 0},
    "Subgenre": {"Value": 0, "Weight": 0, "Adherence": 0},
    "Tempo": {"Value": 0, "Weight": 0, "Adherence": 0},
    "Mode": {"Value": 0, "Weight": 0, "Adherence": 0},
    "Lyrics": {"Value": 0, "Weight": 0, "Adherence": 0}
}

Database = {"Song1":
                {"Mixing":
                    {"Frequency Ranges": {
                        "20-80hz": 0,
                        "80-180hz": 0,
                        "200-400hz": 0,
                        "400-800hz": 0,
                        "800-2400hz": 0,
                        "2400-5500hz": 0,
                        "5500-9000hz": 0,
                        "9-15khz": 0,
                        "15-20khz": 0}},
                 "Genre": 0,
                 "Subgenre": 0,
                 "Tempo": 0,
                 "Mode": 0,
                 "Lyrics": 0}}



print(User_Preferences["Mixing"])



print(get_mode(User_Preferences["Mode"]["Value"]))