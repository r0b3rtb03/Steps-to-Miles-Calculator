
# Inputs
#steps = int(input("How many steps have you've taken?: "))
#walking_speed = float(input("How fast were you walking?: "))
#gender = input("What gender are you?: ")
miles = 5280 # in feet
while True: # Steps
    try:
        steps = int(input("How many steps have you've taken?: "))
        if steps >= 0:
            break
        else:
            print("Invalid input. Please enter positive a number: ")
    except ValueError:
        print("Invalid input. Please enter a number: ")

while True: # Walking Speed
    try:
        walking_speed = float(input("How fast were you walking? (mph): "))
        if walking_speed > 0:
            if walking_speed > 27.78:
                print("Invalid input. Usain Bolt could only run 27.78 mph and he holds the record for fastest man alive.")
            else:
                break
        else:
            print("Invalid input. Please enter a positive number: ")
    except ValueError:
        print("Invalid input. Please enter a number: ")

while True: # Gender
    gender = input("What gender are you?: ")

    if gender.lower() in ["male", "female"]:
        break
    else:
        print("Invalid input. Please enter 'Male' or 'Female'.")

# Height, Feet -> Inches -> CM
print("Input your height")
while True: # Feet
    try:
        h_feet = int(input("Input feet: "))
        if steps >= 0:
            break
        else:
            print("Invalid input. Please enter positive a number: ")
    except ValueError:
        print("Invalid input. Please enter a number: ")
while True: # Inches
    try:
        h_inch = int(input("Input inches: "))
        if h_inch >= 0:
            break
        else:
            print("Invalid input. Please enter a positive number: ")
    except:
        print("Invalid input. Please enter a number: ")

# Equations/Formula

# Height to CM Formula
h_inch += (int(h_feet)*12)
height = round(int(h_inch)*2.54,1)
print("You are "+ str(height) +" cm's tall") # Test to see if it works

# Height to Stride Length Formula
if gender.lower() == "male":
    stride_length = h_inch * 1.0541
elif gender.lower() == "female":
    stride_length = h_inch * 1.0414

print("Your length stride is "+str(stride_length)+" cm's") # Test to see if it works

# Stride Length to Inches to Feet
stride_length = round((float((stride_length * 0.39) / 12)),2)
print("Your length stride is "+str(stride_length)+" ft") # Test to see if it works

# Convert Steps to Miles
avg_mile = round((miles / stride_length), 2)


print("You've walked: "+str(steps)+" steps")
print("You've walked: " +str(avg_mile)+" miles")
