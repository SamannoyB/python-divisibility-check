recommendations = []

try:
          number = int(input("Enter a number: "))
          check = int(input("Enter a number to check divisibility with: "))
except ValueError:
          print("Only integer values accpeted.")
else:
          if number % check == 0:
                    print(f"{number} is divisible by {check}")
          else:
                    print(f"{number} is not divisible by {check}")
                    for i in range(2, 10):
                              if i == check:
                                        continue
                              else:
                                        if number % i == 0:
                                                  recommendations.append(i)
                    print("Recommendations are", recommendations)


