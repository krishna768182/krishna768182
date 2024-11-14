class Person:
    def __init__(self,name, birth_date, death_date=None):
        self.name = name
        self.birth_date = birth_date
        self.death_date = death_date
        self.parents = []     #List of Parents
        self.children = []    #List of children
        self.spouse = None      #List of Spouse

    def add_child(self,child):
        if child not in self.children:
            self.children.append(child)
        child.add_parent(self)             #Adds a child to the person's children list.

    def add_spouse(self,spouse):
        if spouse is None:
            self.spouse = spouse
            spouse.spouse = self          #Adds a spouse for the person.

    def add_parent(self, parent):
        if len(self.parents) < 2:        #Check if the person has two parents.
            self.parents.append(parent)
            parent.children.append(self)

    