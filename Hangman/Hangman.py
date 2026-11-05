#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
play='y'
while play == 'y' or play == 'Y':
    print("\n"*100)
    print("~~~~HANGMAN~~~~")
    print("            Menu            ")
    print("-----------------------------")
    print("1. Rules")
    print("2. Strategy")
    print("3. Start")

    choice=int(input("Enter:"))
    if choice == 1:
        print("""                                        Rules
The objective of the game is simple. You will be given a word, for example, Hangman.
The word to guess is represented by a row of dashes representing each letter of the
word.
If the guessing player suggests a letter which occurs in the word, the game writes it in
all its correct positions. If the suggested letter does not occur in the word, the game
removes (or alternatively, adds) one element of a hanged stick figure as a tally mark.
Generally, the game ends once the word is fully guessed, or if the stick figure is complete
— signifying that all guesses have been used.
If the word is correct, the game is over and the guesser wins. Otherwise, the game
may choose to penalize the guesser by adding an element to the diagram. On the other
hand, if the guesser makes enough incorrect guesses to allow the game to complete
the diagram, the guesser loses. However, the guesser can also win by guessing all the letters
that appear in the word, thereby completing the word, before the diagram is completed.""")
        re=input("\nReady to play(Y/N)?")
        if re == 'Y' or re == 'y':
            continue
        else:
            break
    elif choice == 2:
        print("""                                         Strategy
1. The twelve most commonly occurring letters in the English language are e-t-a-o-i-n-s-h-r-d-l-u.
2. Another common strategy is to guess vowels first, as English only has five vowels (a, e, i, o, and
u, while y may sometimes, but rarely, be used as a vowel) and almost every word has at least one.""")
        re=input("\nReady to play(Y/N)?")
        if re == 'Y' or re == 'y':
            continue
        else:
            break
    elif choice == 3:
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #print hangman
        H1=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
        H2=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|']
        H3=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] #27
        H4=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] #25, 26, 27, 28, 29
        H5=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] #26, 27 
        H6=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|']
        H7=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|']
        H8=[' ', ' ', ' ', ' ', '`', '`', '`', '`', '`', '`', '`', '`', ' ']

        print("\n"*100)
        print("========================")
        print("                 Hangman                  ")
        print("========================")

        for H in [H1, H2, H3, H4, H5, H6, H7, H8]:
            s1=''
            for s2 in H:
                s1=s1+s2
            print(s1, end="\n")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #functions
        def listring(string):
            L=[]
            for i in string:
                L.append(i)
            return L

        def replace(string, L):
                Lin=[]
                for i in range(0, len(string)):
                    if L == string[i]:
                        Lin.append(i)
                for j in Lin:
                    queL[j] = L
                queS=''
                for s2 in queL:
                    queS=queS+s2
                return queS

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        words = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'hangman', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac']
        import random
        ansS=random.choice(words)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        t1=()
        ly=len(ansS)
        t2={ly}
        ansL=listring(ansS)
        queS="-"*len(ansS)
        print("___________________________")
        print("\n", queS, t2)
        print(t1)
        queL=listring(queS)
        ques=''

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        x=0
        lives=0

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        while True:
            if queS == ansS:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~")
                print("           Congratulations               ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~")
                break
            elif lives > 5:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~")
                print("              Game Over!                 ")
                print("  The word was", ansS)
                print("~~~~~~~~~~~~~~~~~~~~~~~~")
                break
            else:
                print("___________________________")
                L=input("enter a letter:")
                if len(L) <= 1:
                    if L in ansS:
                        queS=replace(ansS, L)
                        l=L.swapcase()
                        ques=replace(ansS, l)
                        print("\n"*100)
                        print("========================")
                        print("                 Hangman                  ")
                        print("========================")
                        for H in [H1, H2, H3, H4, H5, H6, H7, H8]:
                            s1=''
                            for s2 in H:
                                s1=s1+s2
                            print(s1, end="\n")
                        print("______________________________")
                        print("\n", ques, t2)
                        print(t1)
                    else:
                        queS=replace(ansS, L)
                        l=L.swapcase()
                        ques=replace(ansS, l)
                        for q in range(0,1):
                            Hangin=[27, 27, 27, 29, 27, 28]
                            Hanglist=[H3, H4, H4, H4, H5, H5]
                            Hangbody=['O', '|', '-', '-', '/', '|']
                            while True:
                                h1=Hangin[x]
                                h2=Hanglist[x]
                                h3=Hangbody[x]
                                h2.insert(h1, h3)
                                x+=1
                                break

                        print("\n"*100)    
                        print("========================")
                        print("                 Hangman                  ")
                        print("========================")
                        for H in [H1, H2, H3, H4, H5, H6, H7, H8]:
                            s1=''
                            for s2 in H:
                                s1=s1+s2
                            print(s1, end="\n")
                        lives+=1

                        if L not in t1:
                            t1=t1+(L,)
                        
                        print("______________________________")
                        print("\n", ques, t2)
                        print(t1)
                else:
                    queS=replace(ansS, L)
                    l=L.swapcase()
                    ques=replace(ansS, l)
                    print("\n"*100)    
                    print("========================")
                    print("                 Hangman                  ")
                    print("========================")
                    print("What you did wrong :- You typed in more than one letter.")
                    for H in [H1, H2, H3, H4, H5, H6, H7, H8]:
                        s1=''
                        for s2 in H:
                            s1=s1+s2
                        print(s1, end="\n")
                        
                    print("______________________________")
                    print("\n", ques)
                    print(t1)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        play=input("Play Again(Y/N)?")