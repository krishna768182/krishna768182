from person import Person

class FamilyTree:
    def __init__(self):
        self.member = {}

    def add_person(self, person):
        self.member[person.name] = person
        
    def get_person(self, name):
        return self.member.get(name)

    def get_siblings(self, person):
        siblings = []
        for parent in person.parents:
            siblings.extend(parent.children)
        siblings = [siblings for sibling in siblings if sibling != person]
        return siblings     
    #Feature 1:
    def get_parents(self, name):
        person = self.get_person(name)      
        return person.parents if person else[]
    
    def get_grandchildren(self, person):   
        grandchildren = []
        for child in person:
            grandchildren.extend(child)
        return grandchildren
    
    def get_grandparents(self, name):
        person = self.get_person(name)
        if not person:
            return[]
        grandparents = []
        for parent in person.parents:
            grandparents.extend(parent.parents)
        return grandparents
    #Feature 2:
    def get_immediate_family(self, person):    #Returns immediate family, like parents, sbilings, spouse and children.
        immediate_family = set(person.parents)
        immediate_family.update(self.get_siblings(person))
        if person.spouse:
            immediate_family.add(person.spouse)
        immediate_family.update(person.children)
        return list(immediate_family)
    
    def get_extended_family(self, person):    #Returns extended family like aunt and uncle.
        extended_family = set(self.get_immediate_family(person))
        for parent in person.parents:
            aunt_uncle = self.get_siblings(parent)
            extended_family.update(aunt_uncle)
            for aunt_uncle in aunt_uncle:
                extended_family.update(aunt_uncle.children)
        return list(extended_family)
       