''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

# Indexing
item_at_index_three = student_pet_count_list[3]
# print(student_pet_count_list[100])
item_three_from_back = student_pet_count_list[-3]

sum = 0
for individual_pet_count in student_pet_count_list:
    sum = sum + individual_pet_count

num_of_students = len(student_pet_count_list)
print(num_of_students)

# sum_of_items / number_of_items
average = sum / num_of_students
print(average)
