def grams_to_ounces(grams):
    return 28.3495231 * grams
def fahrenheit_to_centigrade(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return chickens, rabbits
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))
import itertools

def string_permutations(string):
    return [''.join(p) for p in itertools.permutations(string)]
def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
