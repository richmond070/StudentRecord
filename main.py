student = {}

done = True

while done == True:
    #set a list that helps add a new student to the list
    student.setdefault('name', []).append(input('Student name:\n'))
    student.setdefault('age', []).append(int(input('Student age:\n')))
    student.setdefault('class', []).append(int(input('Current class:\n')))

    print('add new student >')
    choice = str(input("Type 'c' for continue or 'd' for done:\n"))

    if choice == 'c':
        done = True
    else:
        done = False

    #this is to give you a record of all the students in the class

    for i in range(len(student['name'])):
        history = [str(student['name'][i]) + ' ' +str(student['age']) + ' '+str(student['class'])]
        print(history)