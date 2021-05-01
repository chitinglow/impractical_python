"""Generate funny names by randomly combining names from 2 separate lists."""
import sys
import random

def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ( 'Bill', "Bob", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread',
              'Crapps', 'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy',
              'Gootsy', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo',
             'Joe', 'Johnny', 'Lemongrass', 'Longbranch', 'Mergatroid',
             'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle',
              'Pushmeet', 'Schlomo', 'Scratchensniff', 'Scut', 'Sid',
             'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki',
             'Spitzitout', 'Squids', 'Stinky', 'Storyboard',
             'TeeTee', 'Winston', 'Worms')

    middle  = ('Pottin Soil', 'The Squirts', 'Oil Can', 'The Big News', 'Grunts', 'Tinkie Winkie', 'Baby Oil',
               'Bad News', 'Big Burps', 'Beenie-Weenie', 'Stinkbug', 'Greasy Jim', 'Crab Meat',
               'Dark Skies', 'Dennis Clawhammer', 'Lil Debil', 'Lunch Money', 'Mr Peabody',
               'Pitchfork Ben', 'Potato Bug','Rock Candy', 'The Squirts',
               'Soupcan Sam', 'Wheezy Joe','Sweet Tea', 'Jazz Hands')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
            'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
            'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
            'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
            'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
            'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
            'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
            'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed', 'Vinaigrette',
            'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey',
            'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        middle_name = random.choice(middle)

        print("\n\n")
        print("{} {} {}".format(first_name, middle_name ,last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")

        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()