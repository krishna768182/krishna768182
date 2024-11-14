from family_tree import FamilyTree

def menu():
    print("Family Tree Menu.")
    print("1. Display Parents.")
    print("2. Display Grandchildren.")
    print("3. Display Grandparents.")
    print("4. Display Immediate Family.")
    print("5. Display Extended Family.")
    print("6. Exit.")

def user_option(family_tree):
    option = {
        '1': ("Parents", family_tree.get_parents),
        '2': ("Grandchildren", family_tree.get_grandchildren),
        '3': ("Grandparents", family_tree.get_grandparents),
        '4': ("Immediate Family", family_tree.get_immediate_family),
        '5': ("Extended Family", family_tree.get_extended_family)
    }
    while True:
        menu()
        choice = input("Enter your choice:")

        if choice == '6':
            print("Exiting the system.")
            break

        if choice in option:
            name = input("Enter a name:")
            person = family_tree.get_person(name)  # Retrieve Person object by name

            if person:  # Check if the person exists
                label, method = option[choice]
                result = method(person) 
                print(f"{label}: {[p.name for p in result]}")
            else:
                print("Person not found in the family tree.")
        else:
            print("Please enter a valid number.")
