TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
name=(input("Insert your username: "))
password=(input("Insert your password: "))
print('-' * 50)
if name not in registered_users.keys():
    print("unregistered user, terminating the program..")
    exit()
elif registered_users.get(name) != password:
    print("wrong password, terminating the program..")
    exit()
else:
    print(f"""Welcome to the app, {name}.
We have {len(TEXTS)} texts to be analyzed.""")
print('-' * 50)
number_to_analyse = input(f"Enter a number of the text to be analysed (1-{len(TEXTS)}): ")
if not number_to_analyse.isdigit():
    print("Invalid input, terminating the program..")
    exit()
else:
    number = int(number_to_analyse)
    if number < 1 or number > len(TEXTS):
        print("Invalid input, terminating the program..")
        exit()
    else:
        print("Analyzing text...")
text = TEXTS[number-1]
words = []
import string
for word in text.split():
    clean_word = word.strip(string.punctuation)
    words.append(clean_word)
print(f"There are {len(words)} words in the selected text.")
capitalized_words = sum(1 for word in words if word[0].isupper())
#kontrola velkých písmen
#capitalized_words_list = [word for word in words if word[0].isupper()]
#print(capitalized_words_list)
print(f"There are {capitalized_words} titlecase words.")
capital_only = sum(1 for word in words if word.isupper())
print(f"There are {capital_only} uppercase words.")
lower_only = sum(1 for word in words if word.islower())
print(f"There are {lower_only} lowercase words.")
digit = sum(1 for word in words if word.isdigit())
print(f"There are {digit} numeric strings.")
sum_of_digits = 0
for word in words:
    if word.isdigit():
        sum_of_digits += int(word)
print(f"The sum of all the numbers {sum_of_digits}.")
length_count = {}

for word in words:
    length = len(word)
    if length in length_count:
        length_count[length] += 1
    else:
        length_count[length] = 1
print('-' * 50)
print(f"{'LEN':>3} | {'OCCURRENCES':<17} | {'NR.':>2}")
print('-' * 50)
for length in sorted(length_count):
    stars = '*' * length_count[length]
    print(f"{length:>3} | {stars:<17} | {length_count[length]:>2}")

