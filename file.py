def add_student(name,roll,marks):
    with open("students.txt","a") as f:
        f.write(f"{name},{roll},{marks}\n")

def update_marks(roll,new_marks):
    students=[]
    with open("students.txt") as f:
        for line in f:
            data=line.strip().split(',')
            if data[2]==roll:
                data[3]=new_marks
            students.append(",".join(data))
    
    with open("students.txt","w") as f:
        f.write("\n".join(students))

update_marks(348,90)