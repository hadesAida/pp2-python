import math
import random
import itertools

# Task 1: Convert Grams to Ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams

# Task 2: Convert Fahrenheit to Centigrade
def fahrenheit_to_centigrade(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# Task 3: Solve Classic Puzzle (Chickens and Rabbits)
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return chickens, rabbits

# Task 4: Filter Prime Numbers from a List
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

# Task 5: Generate Permutations of a String
def string_permutations(string):
    return [''.join(p) for p in itertools.permutations(string)]

# Task 6: Reverse Words in a Sentence
def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

# Task 7: Check if 3 is Next to 3 in a List
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# Task 8: Check if 007 Exists in Order in a List
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [0, 0, 7]:
            return True
    return False

# Task 9: Compute Volume of a Sphere Given Its Radius
def sphere_volume(radius):
    return (4/3) * math.pi * (radius**3)

# Task 10: Get Unique Elements from a List
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

# Task 11: Check if a Word or Phrase is a Palindrome
def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

# Task 12: Create a Histogram from a List of Integers
def histogram(lst):
    for value in lst:
        print('*' * value)

# Task 13: "Guess the Number" Game
def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number_to_guess = random.randint(1, 20)
    guesses_taken = 0
    
    while True:
        guess = int(input("Take a guess.\n"))
        guesses_taken += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

def main():
    print(grams_to_ounces(100))  # Convert 100 grams to ounces
    print(fahrenheit_to_centigrade(98.6))  # Convert 98.6°F to Celsius
    print(solve(35, 94))  # Solve for chickens and rabbits
    print(filter_prime([1, 2, 3, 4, 5, 6, 7]))  # Filter prime numbers
    print(string_permutations("abc"))  # Get permutations of 'abc'
    print(reverse_words("We are ready"))  # Reverse words in a sentence
    print(has_33([1, 3, 3]))  # Check for 33
    print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Check for 007
    print(sphere_volume(5))  # Compute volume of a sphere with radius 5
    print(unique_elements([1, 2, 2, 3, 3, 4]))  # Get unique elements
    print(is_palindrome("madam"))  # Check if a word is palindrome
    histogram([4, 9, 7])  # Print histogram
    guess_the_number()  # Start the "Guess the Number" game

if __name__ == "__main__":
    main()
