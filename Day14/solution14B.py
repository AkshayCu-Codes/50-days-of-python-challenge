def your_salary():
    name=input("Enter your name: ")
    periods=int(input("Number of periods taught in a month: "))

    if periods <=100:
        salary = periods * 20
    else:
        overtime = periods -100
        salary = (periods * 20) + (overtime * 25)

    print(f"Teacher: {name}")
    print(f"Periods: {periods}")
    print(f"Gross salary: {salary:,}")

your_salary()