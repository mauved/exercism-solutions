# Score categories
# Each is implemented as a function


def YACHT(dice):
    '''
    All five dice showing the same face
    '''
    if dice.count(dice[0]) != 5:
        return 0
    return 50


def ONES(dice):
    return dice.count(1)


def TWOS(dice):
    return dice.count(2) * 2


def THREES(dice):
    return dice.count(3) * 3


def FOURS(dice):
    return dice.count(4) * 4


def FIVES(dice):
    return dice.count(5) * 5


def SIXES(dice):
    return dice.count(6) * 6


def FULL_HOUSE(dice):
    '''
    Three of one number and two of another
    '''
    for roll in dice:
        if dice.count(roll) < 2:
            return 0
        elif dice.count(roll) > 3:
            return 0
    return sum(dice)


def FOUR_OF_A_KIND(dice):
    '''
    At least four dice showing the same face
    '''
    for roll in dice:
        if dice.count(roll) >= 4:
            return 4 * roll

    return 0


def LITTLE_STRAIGHT(dice):
    '''
    1-2-3-4-5
    '''
    for roll in range(1, 6):
        if dice.count(roll) != 1:
            return 0

    return 30


def BIG_STRAIGHT(dice):
    '''
    2-3-4-5-6
    '''
    for roll in range(2, 7):
        if dice.count(roll) != 1:
            return 0

    return 30


def CHOICE(dice):
    '''
    Any combination
    '''
    return sum(dice)


def score(dice, category):
    return category(dice)
