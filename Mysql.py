import mysql.connector
# Import the mysql.connector library
word = input("Enter a world in English and press Enter: ")
# Store the input string into the word variable to look for in the database
con = mysql.connector.connect(user="ardit700_student",
password="ardit700_student", host="108.167.140.122",
database="ardit700_pm1database")
# Establish connection with the remote database using the arguments above:
# user, password, host and database
cursor = con.cursor()
# Create the cursor
query = cursor.execute("SELECT * FROM Dictionary Where Expression = '%s'"
% word)
# Query the data in the Dictionary dabatabase selecting those data equal
# to the word input
results = cursor.fetchall()
# Store all the definition for the word into results variable
if results:
# Start of if block
    for results in results:
        print(results[1])
        # Print the defintions
else:
    print("We couldn´t find any results about that")
    # If not definitions are found print the sentence above
