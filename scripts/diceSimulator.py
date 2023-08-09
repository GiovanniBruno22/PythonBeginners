from random import randint

def ask_num_dice():
    '''
    Asks the user for the number of six-sided dice to roll as an integer
    '''
    int_Flag1 = True

    while int_Flag1:
        num_of_Dice = input("Please input an integer for number of dice to roll: ")

        # Makes sure input is an integer 
        try:
            num_of_Dice = int(num_of_Dice)

            int_Flag1 = False
        except ValueError:
            continue

    return num_of_Dice

def ask_dice_face():
    '''
    Asks the user for number of each face of a six-sided die. 
    
    Assumes all die are identical.
    '''
    dice_face_List = []
    for face in range(1,7):
        int_Flag2 = True

        while int_Flag2:
            num_Face = input("What integer is on face {} of die: ".format(face))

            # Makes sure input is an integer 
            try:
                num_Face = int(num_Face)
                dice_face_List.append(num_Face)

                int_Flag2 = False
            except ValueError:
                continue

    return dice_face_List

def main():
    '''
    Computes the output of a dice roll given number of die and what numbers
    are on each face

    Assumes all die are identical.
    '''
    output = 0

    num_Dice = ask_num_dice()
    dice_face_List = ask_dice_face()

    for die in range(0,num_Dice):
        output += dice_face_List[randint(0,5)]

    print("Your dice roll is", output)

if __name__ == "__main__":
    main()
