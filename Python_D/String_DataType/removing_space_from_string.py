city = input("Enter your cityname :")
#city = input("Enter your cityname :").strip() -> This is valid 
'''
 three ways to remove the space
 lstrip() -> Remove the sapce from left of the stirng 
 rstrip() -> Remove the sapce from right of the stirng 
 strip() -> Remove the sapce from string
'''
scity = city.strip()

if scity == "Hyderabad":
    print("Hello Hyderabad")
elif scity == "Chennai":
    print("Hello Chennai")
elif scity == "Odisha":
    print("Hello Odisha")
else:
    print("Your city is not listed")