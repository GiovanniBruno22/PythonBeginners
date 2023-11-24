cipher = {
  "A": "X",
  "B": "Y",
  "C": "Z",
  "D": "A",
  "E": "B",
  "F": "C",
  "G": "D",
  "H": "E",
  "I": "F",
  "J": "G",
  "K": "H",
  "L": "I",
  "M": "J",
  "N": "K",
  "O": "L",
  "P": "M",
  "Q": "N",
  "R": "O",
  "S": "P",
  "T": "Q",
  "U": "R",
  "V": "S",
  "W": "T",
  "X": "U",
  "Y": "V",
  "Z": "W"
}

def main():
  print("Please enter a text to cipher: ")
  text = input()
  output = ""

  for a in text:
    if a.isalpha():
      if a.islower():
        output += cipher[a.upper()].lower()
      else:
        output += cipher[a.upper()]
    else:
      output += a

  print("Your ciphered message is: ", output)

if __name__ == "__main__":
  main()