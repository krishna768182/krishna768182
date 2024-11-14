from person import Person
from family_tree import FamilyTree

def data():
    family_tree = FamilyTree()

    Walter = Person("Walter Emmerson","1930-06-25")
    Anna = Person("Anna Emmerson","1931-05-06")
    Cornelia = Person("Cornelia Emmerson","1950-01-01")
    Otto = Person("Otto Emmerson","1948-05-15")
    Alex = Person("Alex Emmerson","1975-07-20")
    Luke = Person("Luke Emmerson","1978-10-05")
    
#Sets relationship from parents to children and spouses to spouses.
    Otto.add_spouse(Cornelia)
    Otto.add_child(Alex)
    Otto.add_child(Luke)
    Cornelia.add_child(Alex)
    Cornelia.add_child(Luke)

#Adds grandparents
    Walter.add_child(Otto)
    Anna.add_child(Otto)

#Adds person to family tree
    family_tree.add_person(Walter)
    family_tree.add_person(Anna)
    family_tree.add_person(Otto)
    family_tree.add_person(Cornelia)
    family_tree.add_person(Luke)
    family_tree.add_person(Alex)

    return family_tree