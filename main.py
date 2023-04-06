# """squaring numbers"""
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# squaredNumbers = [num ** 2 for num in numbers]
# print(squaredNumbers)

# """filtering even numbers"""
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# evenNumbers = [num for num in numbers if num % 2 == 0]
# print(evenNumbers)

# """data overlap"""
# with open("file1.txt") as file:
#     l1 = file.readlines()
# with open("file2.txt") as file:
#     l2 = file.readlines()
#
# result = [int(num) for num in l1 if num in l2]
# print(result)

# """creating random scores"""
# """imported random module"""
# import random

# """list of students"""
# students = ["Arup", "Bibek", "Aadarsh", "Anshu", "Anuragini", "Shruti", "Manisha", "Hemanshi"]

# """creating dictionary using dictionary comprehension"""
# studentsScore = {student: random.randint(1, 100) for student in students}
# print(studentsScore)

# """creating a dictionary from dictionary"""
# passedStudents = {student:value for (student, value) in studentsScore.items() if value > 60}
# print(passedStudents)

# """using Dictionary Comprehension to create a dictionary called result that takes each word in the given
# sentence and calculates the number of letters in each word"""
# sentence = input("Enter a sentence: ")
# sentenceList = sentence.split(" ")
# result = {word:len(word) for word in sentenceList}
# print(result)