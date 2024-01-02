
from random import random, randint


def generate_randints_list(length):
  non_repeating_randints = []
  while len(non_repeating_randints) < length:
    new_random_number = randint(1,9) 
    if new_random_number not in non_repeating_randints:
      non_repeating_randints.append(new_random_number)
  return non_repeating_randints

three_non_repeating_random_numbers = list(map(lambda a: str(a), generate_randints_list(3)))

def main():
  guess = input("Guess: ").strip()
  answer = validate_guess_against_random(guess, three_non_repeating_random_numbers)
  print(answer)
  if answer == "Match" or answer == "Close" or answer == "Nope":
    return main()


def validate_guess_against_random(guess, random_list):
  if guess == "".join(random_list):
    return "Correct"
  is_correct = False
  matches = []
  closes = []  
  print(random_list)
  for idx, guess_value in enumerate(guess):
    if idx > 2: 
      break;
    is_correct = str(random_list[idx]) == guess_value
    matches.append(is_correct)
    closes.append(guess_value in random_list and not is_correct)
  if True in matches:
    return "Match" 
  elif True in closes:
    return "Close" 
  else:
    return "Nope"

if __name__ == '__main__':
  main()