def calculate_distance():

    # Def functions
    def positive_number_int(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("Invalid input. Please enter positive a number: ")
            except ValueError:
                print("Invalid input. Please enter a number: ")

    def positive_number_float(prompt, max_value=None):
        while True:
            try:
                value = float(input(prompt))
                if value > 0 and (max_value is None or value <= max_value):
                    return value
                else:
                    if max_value is not None:
                        print(f"Invalid input. Please enter a positive number up to {max_value}.")
                    else:
                        print("Invalid input. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number: ")

    def gender_input(prompt):
        while True:  # Gender
            gender = input(prompt)
            if gender.lower() in ["male", "female"]:
                return gender.lower()
            else:
                print("Invalid input. Please enter 'Male' or 'Female'.")

    def feet_input(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("Invalid input. Please enter positive a number: ")
            except ValueError:
                print("Invalid input. Please enter a number: ")

    def inch_input(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("Invalid input. Please enter a positive number: ")
            except:
                print("Invalid input. Please enter a number: ")

    # Instance Attributes

    steps = positive_number_int("How many steps have you taken?: ")
    walking_speed = positive_number_float("How fast were you walking? (mph): ", max_value=27.78)
    gender = gender_input("Input your gender (Male/Female): ")
    print("Input your height")
    h_feet = feet_input("Input feet: ")
    h_inch = inch_input("Input inches: ")
    miles = 5280  # in feet

    # Equations/Formula

    # Height to CM Formula
    def height(h_inch, h_feet):
        h_inch += (h_feet * 12)
        return h_inch

    user_height = height(h_inch, h_feet)

    # Height to Stride Length Formula
    def stride_length(gender, user_height):
        if gender == "male":
            stride_length_cm = user_height * 1.0541
        elif gender == "female":
            stride_length_cm = user_height * 1.0414
        return stride_length_cm

    user_stride_length_cm = stride_length(gender, user_height)
    print(f"Your stride length is {user_stride_length_cm} cm")

    # Stride Length to Inches to Feet
    user_stride_length_ft = round((float((user_stride_length_cm * 0.39) / 12)), 2)
    print(f"Your length stride is {user_stride_length_ft} ft")  # Test to see if it works

    # Convert Steps to Miles
    def miles(steps, user_stride_length_ft):
        miles = (steps * user_stride_length_ft) / 5280
        return miles

    avg_miles = miles(steps, user_stride_length_ft)

    print(f"You've walked: {steps} steps")
    print(f"You've walked: {avg_miles:.2f} miles")

calculate_distance()
