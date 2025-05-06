# numbers = [1,2,3]
# new_numbers = [number+1 for number in numbers]
# name = "Angela"
# letters_list = [letter for letter in name]
# doubled_list = [n+n for n in range(1,5)]
# names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
# short_names = [name for name in names if len(name)<=4]
# upper_names = [name.upper() for name in names if len(name)>4]

# names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
# import random
# students_score = {student:random.randint(1,100) for student in names}

# passed_students={student:score for (student,score) in students_score.items() if score >=60 }
student_dict = {
    "student":["Angela","James","Lily"],
    "score": [56,76,98]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index,row) in student_data_frame.iterrows():
    print(row.student)


