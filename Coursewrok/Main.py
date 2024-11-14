from Menu import user_option
from Data import data

def main():
    family_tree = data()
    user_option(family_tree)

    alex_grandparents = family_tree.get_grandparents("Alex")
    if alex_grandparents:
        print("Grandparents of Alex are: {[person.name for person in alex_grandparents]}")
    else:
        print("No grandparents found for Alex.")

if __name__ == "__main__":
    main()