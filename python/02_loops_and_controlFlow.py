# if - statement

# age = float(input("Enter your age: "))
# if age < 18:
#     print("You are a minor.")
#     if age < 13:
#         print("You are a child.")
#     else:
#         print("You are a teenager.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")





# switch - statement (using match-case in Python 3.10+)

# day = input("Enter a day of the week: ")
# match day.lower():
#     case "monday":
#         print("It's the start of the week.")
#     case "tuesday":
#         print("It's the second day of the week.")
#     case "wednesday":
#         print("It's the middle of the week.")
#     case "thursday":
#         print("It's almost the weekend.")
#     case "friday":
#         print("It's the last day of the workweek.")
#     case "saturday" | "sunday":
#         print("It's the weekend!")
#     case _:
#         print("That's not a valid day of the week.")




#for - loop

# for i in range(5):
#     print(i)


# for - loop for finding even and odd sum
# even_sum = 0
# odd_sum = 0
# for i in range(1,11):
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i
# print("The sum of even numbers from 1 to 10 is:", even_sum)
# print("The sum of odd numbers from 1 to 10 is:", odd_sum)


# while loop
# a = 10
# while a > 0:
#     print(a)
#     a -= 1  

# break and continue
for i in range(1, 11):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    if i % 2 == 0:
        print("Skipping even number:", i)
        continue
    print("Current number is:", i)  