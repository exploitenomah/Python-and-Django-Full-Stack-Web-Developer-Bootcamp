

def main():
  print("Starting")
  print("================================")
  print(exercise_one([1, 1, 2, 1, 2, 3, 1]))
  print("================================")
  print(exercise_two("HI"))
  print("================================")
  print(exercise_three("hello", "world"))
  print("================================")
  print(exercise_four([1, 2, 3]))
  print("================================")
  print(exercise_five([1, 2, 3]))

def exercise_one(list_of_numbers):
  print("exercise_one")

  # METHOD 2: Exercise One
  for i in range(len(list_of_numbers) - 2):
    if list_of_numbers[i] == 1 and list_of_numbers[i+1] == 2 and list_of_numbers[i+2] == 3:
      return True
  return False
  # METHOD 1: Exercise One
  # sequence = [1, 2, 3]
  # sequence_in_list = []
  # for number in list_of_numbers:
  #   if len(sequence_in_list) == len(sequence):
  #     return True
  #   is_next_in_sequence = False
  #   if len(sequence_in_list) == 0:
  #     is_next_in_sequence = number == sequence[0]
  #   else:
  #     is_next_in_sequence = number == sequence[len(sequence_in_list)]
  #   if is_next_in_sequence:
  #     sequence_in_list.append(number)
  # return len(sequence_in_list) == len(sequence)

def exercise_two(string):
  print("exercise_two")
  new_string = ""
  for idx in range(len(string)):
   new_string += string[idx] if idx % 2 == 0 else ""
  return new_string


def exercise_three(str1, str2):
  print("exercise_three")
  return str1.lower().endswith(str2.lower()) or str1.lower().endswith(str2.lower())

def fix_teen(num):
  if num == 15 or num == 16 or num <= 12 or num > 19:
    return num
  else:
    return 0

def exercise_four(values):
  print("exercise_four")
  sum = 0
  for value in values:
    sum += fix_teen(value)
  return sum

def exercise_five(values):
  return [value for value in values if value % 2 == 0]

if __name__ == "__main__":
  main()