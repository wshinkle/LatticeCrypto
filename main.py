import sys
import numpy as np
import random
import sage.all
from sage.modules.free_module_integer import IntegerLattice

#public key
A1 = [[449857, 1731, 72769],
      [224963, 870, 36380],
      [224927, 861, 36390]]

#private key
A2 =[[6, 0, 1],
     [1, 3, 1],
     [7, 3, -5]]

"""
Encrpytion Scheme:
    A -> most significant 3 bits of the character
    B -> second 3 most significant bits of the character
    C -> least 2 significant bits of the character
"""

def generate_point(A, B, C):
    A = int(A, 2)
    B = int(B, 2)
    C = int(C, 2)
    
    # Create a vector from A, B, C
    vector = np.array([A, B, C])

    # Multiply A1 by the vector
    point = np.dot(A1, vector)
    point += np.array([random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 1)])

    return point

def get_closest_vector(point):
    lattice = IntegerLattice(A2)
    closest_vector = lattice.closest_vector(point)
    return closest_vector   


def solve_abc(A1, point):
    # Calculate the inverse of A1
    A1_inv = np.linalg.inv(A1)

    # Multiply the inverse of A1 by the point to get the original vector
    vector = np.dot(A1_inv, point)

    # Round the values to the nearest integer, as A, B, and C should be integers
    A, B, C = np.round(vector)

    return int(A), int(B), int(C)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <text>")
        sys.exit(1)
    text = sys.argv[1]
    encrypted_chars = []
    for char in text:
        #print(char, ord(char))
        binary = bin(ord(char))[2:].zfill(8)
        A = binary[:3]
        B = binary[3:6]
        C = binary[6:]
        vals = [A, B, C]
        point = generate_point(A, B, C)
        print(f'{char}: {point}')
        encrypted_chars.append(point)
    #print(encrypted_chars)
    
    decrypted_chars = []
    for point in encrypted_chars:
        print(f'Point: {point}')
        unperturbed_point = get_closest_vector(point)
        print(f'Unperturbed Point: {unperturbed_point}')
        A, B, C = solve_abc(A1, unperturbed_point)
        #print(A, B, C)
        binary = bin(A)[2:] + bin(B)[2:] + bin(C)[2:]
        #print(unperturbed_point)
        #print(binary)
        decrypted_chars.append(chr(int(binary, 2)))
    print(''.join(decrypted_chars))


    