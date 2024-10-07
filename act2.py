#1.Get the sum of all even numbers in a list: 
numbers = [1, 4, 7, 10, 13, 16] 

s = 0

for n in numbers:
    if n % 2 == 0:
        s += n

print("Sum: ", s)

#2.Print student name at a specific index in a tuple: 
students = ('John', 'Maria', 'David', 'Samantha') 

print(students[0])

#3.Print names of people older than 20 in a dictionary: 
people = {'John': 19, 'Emily': 21, 'Sarah': 25, 'Tom': 18} 

for name, age in people.items():
    if age > 20:
        print(name)

#4.Print numbers that appear more than once in a tuple: 

numbers = (1, 3, 2, 4, 3, 1, 2, 5)

duplicates = []

for i in range(len(numbers)):
    count = 0 

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1  #
    if count > 1 and numbers[i] not in duplicates:
        duplicates.append(numbers[i])  
print("Numbers are:")
for number in duplicates:
    print(number)

#5. Print student with the highest score: 
students_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)] 

top_stud = ""
top_score = 0

for stud, score in students_scores:
    if score > top_score:
        top_stud = stud
        top_score = score

print(f"Highest scorrer: {stud}")