
workouts = []

def add_workout():
    activity = input("Enter activity: ")
    duration = int(input("Enter duration in minutes"))
    workouts.append((activity, duration))
    print("Workout added!")

def view_workouts():
    for activity, duration in workouts:
        print(activity, "-", duration, "minutes")

def calculate_calories():
    total=sum(duration * 5 for activity, duration in workouts)
    print("Estimated calories burned: ", total)

def main():
    while True:
        print("\n1.Add Workout  2.View Workouts  3. Calories  4.Exit")
        choice = input("Enter choice: ")
        if choice == "1": add_workout()
        elif choice == "2": view_workouts()
        elif choice == "3": calculate_calories()
        elif choice == "4": break
        else: print("Invalid choice")

main()
