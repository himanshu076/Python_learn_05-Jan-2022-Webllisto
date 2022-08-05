'''Working with csv files in Python

First of all, what is a CSV ?
CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. A CSV file stores tabular data (numbers and text) in plain text. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format.

For working CSV files in python, there is an inbuilt module called csv.
'''

'''****************Reading a CSV file******************'''
# Importing csv pakage
# import csv          

# # csv file name
# filename = "apple.csv"          

# # initilize the title & row list
# fields = []
# rows = []

# # Reading csv file
# with open(filename, 'r') as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)

#     # extracting field names through first row
#     fields = next(csvreader)

#     # extracting each data row one by one
#     for row in csvreader:
#         rows.append(row)

#     # get total number of rows
#     print("Total no. of rows: %d"%(csvreader.line_num))

# # printing the field names
# print('Field names are:' + ', '.join(field for field in fields))
  
# #  printing first 5 rows
# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#     # parsing each column of a row
#     for col in row:
#         print("%10s"%col),
#     print('\n')

'''****************writing a CSV file******************'''

# importing the csv module
import csv
  
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
  
# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'],
         ['Sanchit', 'COE', '2', '9.1'],
         ['Aditya', 'IT', '2', '9.3'],
         ['Sagar', 'SE', '1', '9.5'],
         ['Prateek', 'MCE', '3', '7.8'],
         ['Sahil', 'EP', '2', '9.1']]
  
# name of csv file
filename = "university_records.csv"
  
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
      
    # writing the fields
    csvwriter.writerow(fields)
      
    # writing the data rows
    csvwriter.writerows(rows)