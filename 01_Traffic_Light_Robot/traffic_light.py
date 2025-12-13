light = input("Enter traffic light color (red / yellow / green): ").lower()

if light == "green":
    print("Robot moves forward")
elif light == "yellow":
    print("Robot slows down")
elif light == "red":
    print("Robot stops")
else:
    print("Invalid signal")
