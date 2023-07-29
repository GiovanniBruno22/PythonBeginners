
def alphaToNATO(word):
    '''
        function alphaToNATO converts every letter in word to its NATO word.
        args: word - string.
        returns NATO - list of strings.
        dictionary containing letters and corresponding NATO words.
    '''
    NATO_Alpha = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
        'Z': 'Zulu'
    }
    #This will add "can not convert to NATO" if key is not found in NATO_Alpha.
    NATO = [NATO_Alpha.get(letter.upper(),letter) for letter in word]
    return '\n'.join(NATO)

if __name__ == '__main__':
        str=input('Enter a word: ')
        print(alphaToNATO(str))