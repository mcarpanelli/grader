import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Find Top Students')
parser.add_argument('filename', metavar='F', type=str, nargs='+')
parser.add_argument('percentage', metavar='F', type=int, nargs='+')
args = parser.parse_args()
filename = args.filename
percentage = args.percentage

df = pd.read_csv(filename) # before: 'data/grades.csv'
df1 = df.iloc[:,[0,1,3,5]]
df1['Final'] = df1.apply(lambda row: (row[1] + row[2] + (2*row[3])) / 400, axis = 1)

# Allow top 1% of students to go to a party
num_students = int(len(df1) * (percentage / 100)) # before: 0.01

# IDs of 23 top 1% students
indicies = df1.Final.argsort() # argsort sorts in ascending order

filtered_students = df1.iloc[indicies][-num_students:][::-1] # this will show me sorted indices for the top 23 students!
ids = filtered_students.student_id.values # this creates an array of the students that will be selected to go to the party

print(ids)