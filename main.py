# Name: Farhana Lima
# Purpose: Assignment "Pet Chooser"
# Properties: The program will:
# -Start
# -Connect to your personal (pets) database
# -Read data
# -Create one (object) instance of a Pets class for each pet listed in your database
#   --The Pets class in a separate file
# -Display a list of pet names, from the pet object instances
# -Ask the user to choose a pet (see below)
# -Once a pet is chosen, print that pet's info from the (object) instance.
# ---------------------------------------------------------------------------------------------------------------- #

# Now it's time for coding (tried to write playing, but last couple of assignment makes me crying!)
# At first importing mysql.connector . To run this import need to install the following in the venv:
# --- pip3 install pymysql
# --- pip3 install mysql-connector-python
import mysql.connector
# I have created another python file named pet.py. importing Pets from there.
from pet import Pets

# It's time to welcome the user.
print(f"Welcome to Pet Chooser!!!")
# A blank line
print()

# Define database connection parameters
# type your own MySQL password instead of mypassword.
host = "localhost"
user = "root"
password = "mypassword"
database = "pets"

# This time I want to create a connection to the MySQL database
# The try block starts by attempting to establish the connection.
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
# The except will handle potential errors, specially errors that might occur during the database connection process.
# If any error occur it will stored as e, and print the error massage and exit the program.
except mysql.connector.Error as e:
    print(f"Error connecting to the database: {e}, Come back with your password! ")
    exit(1)

# If the try block executed successfully, it will proceed to the cursor object.
# The cursor() will called on the connection object.
# Here cursor will send SQL queries to the database and retrieve results.
cursor = connection.cursor()

# Now it's time for executing an SQL query and fetching data from a MySQL
# Here the marge represent the SQL query, this will retrieve data from multiple tables from the actual database.
marge = """  
        SELECT pets.id, pets.name, types.animal_type, pets.age, owners.name
        FROM pets
        JOIN types ON pets.animal_type_id = types.id
        JOIN owners ON pets.owner_id = owners.id;
        """

# Here the try block is attempting to execute the SQL query (marge).
# The cursor.execute() method sends the query to the database for execution.
try:
    cursor.execute(marge)
    # This method is used to retrieve the result set produced by the query
    pet_data = cursor.fetchall()

# The except block will handle if any error occur during fetching the data.
except mysql.connector.Error as e:
    print(f"Error fetching data from the database: {e}")
    # Closing the cursor to free up memory.
    cursor.close()
    # To terminate the connection properly when program is finished the database operation.
    connection.close()
    # It will exit the program after an error occur.
    exit(1)

# Now a list of Pets instances, it will create a list of Pets instances based on the data fetched from the database.
# This list contains instances of the Pets class, each corresponds to a pet's information retrieved from the database.
pets = [Pets(data[0], data[2], data[4], data[1], data[3]) for data in pet_data]

# We are done with the database part !!! Now it's time for user input.
# This while true loop will continue the program till the user choose to quit.
while True:
    try:
        # It will print the pet list numbered from 1 to n, where n is the number of pet.
        print(f"Please choose a pet from the list below:")
        for i, pet in enumerate(pets, 1):
            print(f"[{i}] {pet.name}")

        # This will add the quit option to the list.
        print("[Q] Quit")
        # This will let the user input his/her choice.
        choice = input("Input your choice from the list: ")
        # Code for the user option, if user choose to quit, break will exit the code with thank you massage.
        if choice.lower() == 'q':
            print(f"Thank you for using pet chooser.")
            break

        # If user input any digit from the list, this code will print the detail of the pet.
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(pets):
                pet = pets[choice - 1]
                print(pet.get_info())
                # Blank line
                print()
                # To give the user continuous choosing option.
                input("Press [ENTER] to continue:")

            # While user input number out of the option, it will print the massage.
            else:
                print(f"Invalid number. Please choose a valid one.")
                # Let the user to continue and make a choice again.
                input("Press [ENTER] to continue:")
        # When The user input anything other than number or q, it will print this, and give other chance.
        else:
            print(f"Invalid input. Please enter a number or 'Q' to quit.")
            # A break and thinking about another chance. as I'm user friendly.
            input("Press [ENTER] to continue:")
    # To handle specific exceptions like unexpected termination of input and provide a user-friendly error message.
    except EOFError:
        print(f"That's not like a good user! ok! quitting the program!!")
        # With the error it will break the loop.
        break
    # A general exception that may occur. it can capture a wide range of exception.
    except Exception as e:
        print(f"An error occurred: {e}, bye bye!")
        # Same as above.
        break

# this will close the program and the database connection to release resources,
# This also ensures that the connection is properly terminated.
cursor.close()
connection.close()
