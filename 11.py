sum = 0
print("Enter numbers (blank line to quit):")
while True:
  try:
    line = input()
    if line == "":
      break
    num = float(line)
    sum += num
    print(f"The current sum is {sum}")
  except ValueError:
    print("That is not a valid number. Please try again.")
  except KeyboardInterrupt:
    break


print(f"The final sum is {sum}")
