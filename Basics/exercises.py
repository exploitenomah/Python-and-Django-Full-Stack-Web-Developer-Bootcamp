

def main():
  exercise_one()
  exercise_two()
  exercise_three()
  exercise_four()
  exercise_five()


def exercise_one():
  print("\n\n exercise one")
  s = "django"
  print(s[0])
  print(s[len(s)-1])
  print(s[0:4])
  print(s[1:4])
  print(s[4:])
  # i = len(s) - 1
  # reversed = ""
  # while len(reversed) < len(s):
  #   reversed += s[i]
  #   i -= 1
  # print(reversed)
  print(s[::-1])

def exercise_two():
  print("\n\n exercise two")
  nested_list = [3, 7, [1, 4, "hello"]]
  print(nested_list[2][2])
  nested_list[2][2] = "goodbye"
  print(nested_list[2][2])

def exercise_three():
  print("\n\n exercise three")
  d1 = { "simple_key": "hello" }
  d2 = { "k1": { "k2": "hello" } }
  d3 = { "k1": [{ "nested_key": [ "this is deep", ["hello"]]}] }
  print(d1["simple_key"])
  print(d2["k1"]["k2"])
  print(d3["k1"][0]["nested_key"][1][0])

def exercise_four():
  print("\n\n exercise four")
  multiple_values_list = [1,1,1,1,1,2,2,2,2,3,3,3,3]
  set_from_multiple_values = set(multiple_values_list)
  for value in set_from_multiple_values:
    print(value)

def exercise_five():
  print("\n\n exercise five")
  name = "Sammy"
  age = 4
  print(f"Hello my dog's name is {name} and he is {age} years old")


if __name__ == '__main__':
  main()
