lastname = input("Enter your last name: ")
midterm = float(input("Enter your midterm exam score (0-100): "))
finals = float(input("Enter your final exam score (0-100): "))

totalexam = (midterm*.40) + (finals*.60)

print(f"Hello {lastname}, your total exam score is {totalexam/100:.0%}")
