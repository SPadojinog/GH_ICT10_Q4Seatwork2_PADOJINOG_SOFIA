#Seatwork#2
from pyscript import document, display 

# Parent Class
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! My name is {self.name} from Grade 10 - {self.section}. My favorite subject is {self.favorite_subject}."

# Child Class
class Student(Classmate):
    pass

# Pre-made classmates 
classmate1 = Student("Jillian Grospe", "Sapphire", "Math") 
classmate2 = Student("Tessa Aseo", "Sapphire", "Science") 
classmate3 = Student("Margo Intalan", "Sapphire", "Social Studies") 
classmate4 = Student("Francesca Yao", "Sapphire", "English") 
classmate5 = Student("Jennifer Uy", "Sapphire", "Special Subjects")

other_classmates = []

def add_classmate(e):
    document.getElementById('output').innerHTML = ''
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    fav_subject = document.getElementById("favsubject").value
    output = document.getElementById("output")

    if name == "" or section == "" or fav_subject == "":
        output.innerHTML = "⚠️ Please fill all information first."
        return

    new_classmate = Student(name, section, fav_subject)
    other_classmates.append(new_classmate)

    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("favsubject").value = ""

    output.innerHTML = f"✅ {name} has been added successfully!"

def show_list(e):
    document.getElementById('output').innerHTML = ''
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    fav_subject = document.getElementById("favsubject").value
    
    new_classmate = Student(name, section, fav_subject)
    other_classmates.append(new_classmate) 

    display(f"Hi! My name is {classmate1.name} from Grade 10 - {classmate1.section}. My favorite subject is {classmate1.favorite_subject}", target="output") 
    display(f"Hi! My name is {classmate2.name} from Grade 10 - {classmate2.section}. My favorite subject is {classmate2.favorite_subject}", target="output") 
    display(f"Hi! My name is {classmate3.name} from Grade 10 - {classmate3.section}. My favorite subject is {classmate3.favorite_subject}", target="output") 
    display(f"Hi! My name is {classmate4.name} from Grade 10 - {classmate4.section}. My favorite subject is {classmate4.favorite_subject}", target="output") 
    display(f"Hi! My name is {classmate5.name} from Grade 10 - {classmate5.section}. My favorite subject is {classmate5.favorite_subject}", target="output") 
    
    # Display for new 
    for classmate in other_classmates: 
        display(f"Hi! My name is {classmate.name} from Grade 10 - {classmate.section}. My favorite subject is {classmate.favorite_subject}", target="output")

    # Clear the information
    document.getElementById("name").value = ""
    document.getElementById("favsubject").value = ""
    document.getElementById("section").value = ""