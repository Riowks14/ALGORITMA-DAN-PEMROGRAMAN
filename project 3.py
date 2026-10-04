country = input("where do you want drive? (south africa, mexico, india, france) :")
age = int(input("how old are you? "))
if country == "south africa":
    if age > 16:
        print("you can drive in south africa")
    else:
        print("you cannot drive in south africa")

elif country == "mexico":
    if age > 17:
        print("you can drive in mexico")
    elif age > 15:
        print("you can drive in mexico with parental agreement")
    elif age > 14:
            print("you can drive in mexico with parental supervision")
    else:
        print("you cannot drive in mexico") 

elif country == "india":
    if age > 17:
        print("you can drive in india")
    else:
        print("you cannot drive in india")

elif country == "france":
    if age > 17:
        print("you can drive in france")
    elif age > 14:
        print("you can drive in france with supervision")
    else:
        print("you cannot drive in france")

else:
    print("Data is not available for this country")
