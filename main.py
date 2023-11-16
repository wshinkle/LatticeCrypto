import sys

A1 = [[449857, 1731, 72769],
      [224963, 870, 36380],
      [224927, 861, 36390]]

A2 =[[6, 0, 1],
     [1, 3, 1],
     [7, 3, -5]]

"""
Encrpytion Scheme:
    A -> most significant 3 bits of the character
    B -> second 3 most significant bits of the character
    C -> least 2 significant bits of the character
"""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <text>")
        sys.exit(1)
    text = sys.argv[1]
    
    for char in text:
        print(char, ord(char))
        binary = bin(ord(char))[2:].zfill(8)
        A = binary[:3]
        B = binary[3:6]
        C = binary[6:]
        print(f'{A} {B} {C}')
    