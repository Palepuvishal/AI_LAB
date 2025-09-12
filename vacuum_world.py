def vacuum_world():
    # Initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("Enter Location of Vacuum (A/B): ").upper()
    status_input = input(f"Enter status of {location_input} (0 for Clean, 1 for Dirty): ")
    other_location = 'B' if location_input == 'A' else 'A'
    status_input_complement = input(f"Enter status of {other_location} (0 for Clean, 1 for Dirty): ")

    print("Initial Location Condition: " + str(goal_state))

    if location_input == 'A':
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty.")
            goal_state['A'] = '0'  # Clean location A
            cost += 1
            print("Cost for CLEANING A: " + str(cost))
            print("Location A has been Cleaned.")

            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving right to Location B.")
                cost += 1
                print("Cost for moving RIGHT: " + str(cost))
                goal_state['B'] = '0'  # Clean location B
                cost += 1
                print("Cost for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean.")
                print("No action, cost: " + str(cost))

        elif status_input == '0':
            print("Location A is already clean.")
            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving RIGHT to Location B.")
                cost += 1
                print("Cost for moving RIGHT: " + str(cost))
                goal_state['B'] = '0'  # Clean location B
                cost += 1
                print("Cost for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean.")
                print("No action, cost: " + str(cost))

    elif location_input == 'B':
        print("Vacuum is placed in Location B")
        if status_input == '1':
            print("Location B is Dirty.")
            goal_state['B'] = '0'  # Clean location B
            cost += 1
            print("Cost for CLEANING B: " + str(cost))
            print("Location B has been Cleaned.")

            if status_input_complement == '1':
                print("Location A is Dirty.")
                print("Moving LEFT to Location A.")
                cost += 1
                print("Cost for moving LEFT: " + str(cost))
                goal_state['A'] = '0'  # Clean location A
                cost += 1
                print("Cost for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("Location A is already clean.")
                print("No action, cost: " + str(cost))

        elif status_input == '0':
            print("Location B is already clean.")
            if status_input_complement == '1':
                print("Location A is Dirty.")
                print("Moving LEFT to Location A.")
                cost += 1
                print("Cost for moving LEFT: " + str(cost))
                goal_state['A'] = '0'  # Clean location A
                cost += 1
                print("Cost for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("Location A is already clean.")
                print("No action, cost: " + str(cost))

    else:
        print("Invalid Location Input. Please enter 'A' or 'B'.")

    # Done cleaning
    print("\nGOAL STATE:")
    print(goal_state)
    print("Performance Measurement (Total Cost): " + str(cost))


# Call the function to run the program
vacuum_world()
