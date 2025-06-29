import random
import string

def generate_random_username(length=8):
    """
    Generate a random username with letters and digits.

    Parameters:
    - length (int): Length of the username (default 8)

    Returns:
    - str: Randomly generated username
    """
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    username = ''.join(random.choice(characters) for _ in range(length))
    return username

def generate_username_with_words():
    """
    Generate a username combining adjectives and nouns.

    Returns:
    - str: Username like 'BlueTiger42'
    """
    adjectives = ['Blue', 'Fast', 'Silent', 'Crazy', 'Happy', 'Lucky', 'Bright', 'Dark', 'Cool', 'Wild']
    nouns = ['Tiger', 'Eagle', 'Shark', 'Wolf', 'Lion', 'Falcon', 'Panther', 'Dragon', 'Bear', 'Fox']

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(10, 99)

    return f"{adjective}{noun}{number}"

def generate_username_with_name():
    """
    Generate a username using random first and last names with numbers.

    Returns:
    - str: Username like 'JohnSmith87'
    """
    first_names = ['John', 'Emma', 'Michael', 'Olivia', 'David', 'Sophia', 'Chris', 'Isabella', 'James', 'Mia']
    last_names = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

    first = random.choice(first_names)
    last = random.choice(last_names)
    number = random.randint(1, 999)

    return f"{first}{last}{number}"

if __name__ == "__main__":
    print("Random username (letters+digits):", generate_random_username())
    print("Username with words:", generate_username_with_words())
    print("Username with names:", generate_username_with_name())
