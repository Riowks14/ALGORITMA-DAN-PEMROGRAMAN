ingredients = ["flour", "sugar", "butter", "egg", "chocolate"]

print("=== COOKIE INGREDIENT CHECKER ===")

jumlah = int(input("How many ingredients do you have? "))

for i in range(jumlah):
    ingredient = input("Enter ingredient: ").lower()

    if ingredient in ingredients:
        print("You have successfully entered", ingredient)
    else:
        print("Uh oh, your ingredient is invalid!")

print("Thank you for using the program!")