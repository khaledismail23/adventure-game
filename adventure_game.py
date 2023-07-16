import time
import random
creature = random.choice(['troll', 'dragon', 'pirate'])
weapon = random.choice(['a tiny dagger', 'a knife', 'a rock'])


def main():
    x = field()
    while True:
        if x == 1:
            y = house(weapon)
            if y == 1:
                y_or_n = fight('loss')
                if y_or_n == 'n':
                    break
                elif y_or_n == 'y':
                    x = field()
            elif y == 2:
                x = run_away()
        elif x == 2:
            z = cave()
            if z == 1:
                y = house('the magical Sword of Ogoroth!')
                if y == 1:
                    y_or_n = fight('win')
                    if y_or_n == 'n':
                        break
                    elif y_or_n == 'y':
                        x = field()
                elif y == 2:
                    x = run_away()
            elif z == 2:
                print_pause('You peer cautiously into the cave.')
                print_pause("You've been here before,")
                print_pause("and gotten all the good stuff.")
                print_pause("It's just an empty cave now.")
                print_pause('You walk back out to the field.')
                print()
                house_or_cave()
                x = enter_1_or_2()

    print_pause('Thanks for playing! See you next time.')


def field():
    print_pause("You find yourself standing in an open field,")
    print_pause("filled with grass and yellow wildflowers.")
    print_pause(f'Rumor has it that a {creature} is somewhere around here,')
    print_pause('and has been terrifying the nearby village.')
    print()
    house_or_cave()
    x = enter_1_or_2()
    return x


def run_away():
    print_pause("You run back into the field. Luckily,")
    print_pause("you don't seem to have been followed.")
    print()
    house_or_cave()
    return enter_1_or_2()


def fight(result):
    if result == 'win':
        print_pause(f'As the {creature} moves to attack,')
        print_pause('you unsheath your new sword.')
        print_pause('The Sword of Ogoroth shines brightly in your hand')
        print_pause('as you brace yourself for the attack.')
        print_pause(f'But the {creature} takes one look at your shiny new toy')
        print_pause('and runs away!')
        print_pause(f'You have rid the town of the {creature}.')
        print_pause('You are victorious!')
    elif result == 'loss':
        print_pause('You do your best...')
        print_pause(f'but your {weapon} is no match for the {creature}.')
        print_pause('You have been defeated!')

    print()
    return y_or_n()


def y_or_n():
    while True:
        try:
            answer = input('Would you like to play again? (y/n)')
            if answer in ['y', 'n']:
                return answer
        except ValueError:
            pass


def cave():
    print_pause('You peer cautiously into the cave.')
    print_pause('It turns out to be only a very small cave.')
    print_pause('Your eye catches a glint of metal behind a rock.')
    print_pause('You have found the magical Sword of Ogoroth!')
    print_pause(f'You discard your silly old {weapon}')
    print_pause('and take the sword with you.')
    print_pause('You walk back out to the field.')
    print()
    house_or_cave()
    return enter_1_or_2()


def house(weapon):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock")
    print_pause(f"when the door opens and out steps a {creature}.")
    print_pause(f"Eep! This is the the {creature}'s house!")
    print_pause(f'The {creature} attacks you!')
    if weapon in ['a tiny dagger', 'a knife', 'a rock']:
        print_pause('You feel a bit under-prepared for this,')
        print_pause(f'what with only having {weapon}.')
    return fight_or_run()


def fight_or_run():
    while True:
        try:
            x = int(input('Would you like to (1) fight or (2) run away?'))
            if x in [1, 2]:
                return x
        except ValueError:
            pass


def print_pause(x):
    print(x)
    # time.sleep(2)


def enter_1_or_2():
    while True:
        try:
            x = int(input('(Please enter 1 or 2).'))
            if x in [1, 2]:
                return x
        except ValueError:
            pass


def house_or_cave():
    print_pause('Enter 1 to knock on the door of the house.')
    print_pause('Enter 2 to peer into the cave.')
    print_pause('What would you like to do?')


if __name__ == '__main__':
    main()
