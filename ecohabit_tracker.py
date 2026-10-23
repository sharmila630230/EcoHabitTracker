
from datetime import date, timedelta

print("===== ECOHABIT TRACKER =====")

# Lists to store habits, points, and dates
habits = []
points = []
dates = []

# Load previously saved habits
try:
    file = open("habits.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if len(data) >= 2:
            habits.append(data[0])
            points.append(int(data[1]))

            if len(data) >= 3:
                dates.append(data[2])
            else:
                dates.append("")

    file.close()

except FileNotFoundError:
    pass

# Display the menu until the user exits
while True:
    print("\n" + "=" * 35)
    print("       ECOHABIT TRACKER")
    print("=" * 35)
    print("1. Add an eco-friendly habit")
    print("2. View all habits")
    print("3. View total points")
    print("4. View weekly summary")
    print("5. Exit")
    print("=" * 35)

    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("Please enter a number from 1 to 5.")
        continue

    choice = int(choice)

    # Option 1: Add a habit
    if choice == 1:
        habit = input("Enter your eco-friendly habit: ")
        habit = habit.strip()

        if habit == "":
            print("Habit name cannot be empty!")
            continue

        # Avoid commas because commas separate saved fields
        if "," in habit:
            print("Please do not use commas in the habit name.")
            continue

        point_text = input("Enter points earned: ")

        if not point_text.isdigit() or int(point_text) == 0:
            print("Please enter points as a positive number.")
            continue

        point = int(point_text)
        today = str(date.today())

        # Add information to the lists
        habits.append(habit)
        points.append(point)
        dates.append(today)

        # Save the habit, points, and date
        file = open("habits.txt", "a")
        file.write(habit + "," + str(point) + "," + today + "\n")
        file.close()

        print("Habit added successfully!")
        print("Date:", today)
    # Option 2: View all habits
    elif choice == 2:
        if len(habits) == 0:
            print("No habits recorded yet.")
        else:
            print("\n===== YOUR ECO-FRIENDLY HABITS =====")

            for i in range(len(habits)):
                print(
                    str(i + 1) + ". " + habits[i]
                    + " - " + str(points[i]) + " points"
                )

                if dates[i] != "":
                    print("   Date:", dates[i])

    # Option 3: View total points
    elif choice == 3:
        total = sum(points)
        print("Your total points:", total)

    # Option 4: View weekly summary
    elif choice == 4:
        today = date.today()
        last_week = today - timedelta(days=6)

        weekly_count = 0
        weekly_points = 0

        print("\n===== LAST 7 DAYS SUMMARY =====")

        for i in range(len(habits)):
            if dates[i] != "":
                habit_date = date.fromisoformat(dates[i])

                if last_week <= habit_date <= today:
                    print(
                        habits[i], "-", points[i],
                        "points on", dates[i]
                    )
                    weekly_count += 1
                    weekly_points += points[i]

        print("-------------------------------")
        print("Habits recorded:", weekly_count)
        print("Points earned:", weekly_points)

    # Option 5: Exit
    elif choice == 5:
        print("Thank you for using EcoHabit Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 5.")
