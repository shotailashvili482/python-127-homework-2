#Truthy or Falsy

user_input = input("Type something (or press enter for nothing): ")

print(f"bool of your input: {bool(user_input)}")

#"0" is a string 0 not integer which means it's not empty value, thus it's true.
print(f"bool(\"0\"): {bool("0")}")