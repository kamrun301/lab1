# -*- coding: utf-8 -*-


file_name = "student_ids.txt"
def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            if not content:
                raise ValueError(f"The {file_name}  is empty.")
            return content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
    return None

content = read_file(file_name)
if content:
    print(content)
else:
    print("No content found in the file")

"""Txt file to list

"""

with open("student_ids.txt") as f:
    students_list = f.readlines()
print(students_list)

"""Select Student for Viva list and students list life make empty"""

import random
vivalist_students = []
viva_counter  = 1
while students_list:
  random_student = random.choice(students_list)
  vivalist_students.append(random_student)
  students_list.remove(random_student)
  ##viva_counter  +=  1
  print(f"Viva_list #{viva_counter}: {random_student}")
  print(f"Remaining students: {students_list}")

  viva_counter += 1
print(f"\nAll selected students for viva : {vivalist_students}")

if not students_list:
  print(f" The students list is now empty : {students_list}")

print(students_list)

print(vivalist_students)

"""Viva list students copy and save again Student list"""

students_list = vivalist_students.copy()
print(students_list)

