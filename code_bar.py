class Member():
    def __init__(self, first_name=''):
        self.first_name = first_name

    def introduce(self):
        print(f'Hi my name is {self.first_name}')


class Workshop():
    def __init__(self, date='', subject='', instructors=[], students=[]):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_instructors(self, new_instructor=''):
        self.instructors.append(new_instructor)

    def add_students(self, new_student=''):
        self.students.append(new_student)


class Student(Member):
    def __init__(self, first_name='', reason=''):
        self.first_name = first_name
        self.reason = reason

    def say_reason(self):
        print(f'I am here because {self.reason}')


class Instructor(Member):
    def __init__(self, first_name='', bio='', skills=[]):
        self.first_name = first_name
        self.bio = bio
        self.skills = []

    def say_bio(self):
        print(f'Hi my name is {self.first_name} {self.bio}')

    def add_skill(self, new_skill=''):
        self.skills.append(new_skill)


# mark = Student('mark', 'Well I hated my job so here we are')
# mark.say_reason()

# george = Instructor(
#     'george', 'I love helping people do hard things', 'python, ruby')
# # george.add_skill()
# # print(george.skills)

# python_workshop = Workshop('1/1/2019', 'python')

# python_workshop.add_instructors('jeff')
# python_workshop.add_instructors(george.first_name)
# python_workshop.add_students(mark.first_name)
# print(python_workshop.__dict__)

workshop = Workshop('12/03/2014', 'Shutl')

print(workshop.__dict__)

jane = Student('Jane Doe', 'I need help learning to program!')
lena = Student('Lena Smith', 'I am excited to start programming!')
print(jane.__dict__)
print(lena.__dict__)

vicky = Instructor('Vicky Python', 'I want to help people learn')
vicky.add_skill('HTML')
vicky.add_skill('JAVAAAAscript')
print(vicky.__dict__)

nicole = Instructor('Nicole McMillan', 'I type and know things')
nicole.add_skill('python')
print(nicole.__dict__)

workshop.add_instructors(nicole.first_name)
workshop.add_instructors(vicky.first_name)
workshop.add_students(jane.first_name)
workshop.add_students(lena.first_name)
print(workshop.__dict__)
