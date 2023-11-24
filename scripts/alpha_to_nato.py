
def normal_to_nato(word: str = 'Hello'):
    """
        function normal_to_nato converts every letter in word to its NATO word.
        args: word - string.
        returns NATO - list of strings.
        dictionary containing letters and corresponding NATO words.
    """
    alpha_to_nato = {
        'A': 'Alpha', 
        'B': 'Bravo', 
        'C': 'Charlie', 
        'D': 'Delta', 
        'E': 'Echo',
        'F': 'Foxtrot', 
        'G': 'Golf', 
        'H': 'Hotel', 
        'I': 'India', 
        'J': 'Juliett',
        'K': 'Kilo', 
        'L': 'Lima', 
        'M': 'Mike', 
        'N': 'November', 
        'O': 'Oscar',
        'P': 'Papa', 
        'Q': 'Quebec', 
        'R': 'Romeo', 
        'S': 'Sierra', 
        'T': 'Tango',
        'U': 'Uniform', 
        'V': 'Victor', 
        'W': 'Whiskey', 
        'X': 'X-ray', 
        'Y': 'Yankee',
        'Z': 'Zulu'
    }
    # This will add "can not convert to NATO" if key is not found in NATO_Alpha.
    nato = [alpha_to_nato.get(letter.upper(), letter) for letter in word]
    return '\n'.join(nato)

if __name__ == '__main__':
    str = input('Enter a word: ')

    print('The word in NATO is:')
    print(normal_to_nato(str))