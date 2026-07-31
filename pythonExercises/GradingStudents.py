from typing import List

def gradingStudents(grades: List):
    for i in range(len(grades)):
        if( grades[i] >= 38):
            aux= (grades[i]//5)+1
            if ((aux*5)-grades[i]<3):
                grades[i]= aux*5
    return grades

print(gradingStudents([73,67,38,33]))

