Bangla = int(input("Enter The Marks(B): "))
English = int(input("Enter The Marks(E): "))
Math = int(input("Enter The Marks(M): "))
Science = int(input("Enter The Marks(S): "))
Total_average = (Bangla + English + Math + Science) / 4
print("--------------\n")

if Total_average > 100:
    print("Marks are not valid..!")
elif 41 <= Total_average <= 60:
    print("Result: " + "D")
elif 61 <= Total_average <= 70:
    print("Result: " + "C")
elif 71 <= Total_average <= 80:
    print("Result: " + "B")
elif 81 <= Total_average <= 90:
    print("Result: " + "A")
elif 91 <= Total_average <= 100:
    print("Result: " + "A+")
else:
    print("Result: " + "F")

print(f"The Total Average Mark is : {Total_average}")

