def gradingStudents(grades):
    new_grade = []
    
    for grade in grades:
        if grade < 38:
            new_grade.append(grade)
        else:
            multiple_of_five = math.ceil(grade / 5) * 5
            if multiple_of_five - grade < 3:
                new_grade.append(multiple_of_five)
            else:
                new_grade.append(grade)  
    
    return new_grade
