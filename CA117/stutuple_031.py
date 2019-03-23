from collections import namedtuple

Student = namedtuple("student", ["firstname", "surname", "id"])

def show_student(s):
	print("{:>10} {}\n {:>10} {}\n {:>10} {}".format("First name:", s.firstname, "Surname:", s.surname, "ID:", s.id))