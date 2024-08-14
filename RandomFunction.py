
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
        #Provide random vals for all frequency ranges
        return None
    elif index in range(1, 10):
        #Provide a random val for one frequncy range
        return None
    elif index == 10:
        #provide random val for genre
        return random.randint(1,30)
    elif index == 11:
        #provide random val for subgenre
        return random.randint(1,10)
    elif index == 12:
        #provide random val for tempo
        return random.randint(40, 200)
    elif index == 13:
        #provide random val for mode
        return random.randint(1,7)
    elif index == 14:
        #provide random val for lyrics
        return None





def probability_function(chance_percentage):
    import random
    random_value = random.uniform(0, 100)
    if random_value < chance_percentage:
        return True
    else:
        return False





