import psycopg2
import random
import string

def rand_string_gen(length):
  letters = string.ascii_lowercase
  rand_string = ''.join(random.choice(letters) for i in range(length))
  return rand_string

min_len = 2
max_len = 10
min_year = 1990
max_year = 2024
min_hours = 34
max_hours = 170
min_score = 2
max_score = 5

try:
  connection = psycopg2.connect(dbname="academy", 
                                host="127.0.0.1", 
                                user="postgres",
                                password="rootroot"
                              )
  print("[INFO] Connection is established")
  cursor = connection.cursor()
except:
	print("[INFO] Connection is not established")


# Fill Student Table
cursor.execute("CREATE TABLE IF NOT EXISTS Students (s_id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, start_year INT NOT NULL);")

num_students = 0
try:
  num_students = int(input("Enter the number of rows insert in the Student table : "))
except:
  print("[INFO] No row insert in the Student table")
random_number = []
random_name = []

for i in range(0, num_students): 
  random_number.append(random.randint(min_year, max_year))
  random_name.append(rand_string_gen(random.randint(min_len, max_len)) + ' ' + rand_string_gen(random.randint(min_len, max_len)))

try:
    cursor.executemany("INSERT INTO students (name, start_year) VALUES (%s, %s);", zip(random_name, random_number))
    connection.commit()
except:
	print("[INFO] Insert in the Students Table failed")

# Print Student Table
print("Students Table:")
request_to_read_data = "SELECT * FROM students;"
cursor.execute(request_to_read_data)
data = cursor.fetchall()
num_students = 0
for row in data:
  print(row)
  num_students += 1
# End work with the Student table


# Fill Courses Table
cursor.execute("CREATE TABLE IF NOT EXISTS Courses (c_no SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, hours INT);")

num_courses = 0
try:
  num_courses = int(input("Enter the number of rows insert in the Courses table : "))
except:
  print("[INFO] No row insert in the Courses table")

random_hours = []
random_title = []

for i in range(0, num_courses): 
  random_hours.append(random.randint(min_hours, max_hours))
  random_title.append(rand_string_gen(random.randint(min_len, max_len)))

try:
    cursor.executemany("INSERT INTO courses (title, hours) VALUES (%s, %s);", zip(random_title, random_hours))
    connection.commit()
except:
	print("[INFO] Insert in the Courses Table failed")

# Print Courses Table
print("Courses Table:")
request_to_read_data = "SELECT * FROM courses;"
cursor.execute(request_to_read_data)
data = cursor.fetchall()
num_courses = 0
for row in data:
  print(row)
  num_courses += 1
# End work with the Courses table

# Fill Exams Table
cursor.execute("CREATE TABLE IF NOT EXISTS Exams (s_id INT REFERENCES Students (s_id), c_no INT REFERENCES Courses (c_no), score INT NOT NULL);")

num_exams = 0
try:
  num_exams = int(input("Enter the number of rows insert in the Exams table : "))
except:
  print("[INFO] No row insert in the Exams table")

random_score = []
random_s_id = []
random_c_no = []

for i in range(0, num_exams): 
  random_score.append(random.randint(min_score, max_score))
  random_s_id.append(random.randint(1, num_students))
  random_c_no.append(random.randint(1, num_courses))

try:
    cursor.executemany("INSERT INTO exams (s_id, c_no, score) VALUES (%s, %s, %s);", zip(random_s_id, random_c_no, random_score))
    connection.commit()
except:
	print("[INFO] Insert in the Exams Table failed")

# Print Exams Table
print("Exams Table:")
request_to_read_data = "SELECT * FROM exams;"
cursor.execute(request_to_read_data)
data = cursor.fetchall()
for row in data:
  print(row)
# End work with the Exams table

cursor.close()
connection.close()

