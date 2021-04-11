import sys

print("Hi there! Thank you so much for taking this short time to help Matrix Lotus with its research.")
print("This survey is for people with a female reproductive system between the ages of 18 and 45.")
print("This survey is for United States residents only.")
print("Your answers will be anonymous and there are no wrong answers.\nThank you so much!")

# This ensures that any inputs that should be numbers is checked
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError :
            print("Invalid entry! Please try again.")
            continue
        else:
            return userInput

# This records the client's name
print("Question 1")
name = input("What is your first name?\nPlease enter your name: ")
name = name.title()
print("Welcome", name)

# This block restricts users to females
print("Question 2")
gender = input("Please select your gender:\n[Please enter Male, Female or Other]: ")
if gender in ["M", "m", "MALE", "Male", "male"]:
    gender = 'm'
    sys.exit("Sorry, this survey is for females only. Check back soon for male-centered surveys. Thank you for your interest.")
elif gender in ["F", "f", "FEMALE", "Female", "female"]:
    gender = 'f'
    print("You entered Female")
    # break
else:
    print("Invalid entry! Please try again.")

# This tests that the client's age is between and including 18 and 45.
print("Question 3")
while True:
    age = inputNumber("Please enter your age: [Age must be between 18 and 45]\nPlease enter your age: ")
    if age >= 18 and age <= 45:
        print(f"Great! Your age is {age}, which is within the correct range.")
        break
    else:
        print("Invalid entry! Please try again.")

# This block tests for US citizenship
print("Question 4")
us_Resident = input("Are you a resident of the United States?\n[Please enter Yes or No]: ")
if us_Resident in ["Yes", "YES", "y", "Y", "yes"]:
    print("Great! You are a United States resident and qualified to take this survey.")
elif us_Resident in ["No", "NO", "n", "N", "no"]:
    sys.exit("Sorry! This survey is only for United States residents. Thanks for trying.")
else:
    print("Sorry! Invalid entry! Please try again")

# probes for birth control usage
print("Question 5")
birth_control = input("Have you every used birth control?\nPlease enter yes or no: ")
if birth_control in ["Yes", "YES", "y", "Y", "yes"]:
    print("You indicated that you HAVE used birth control.")
elif birth_control in ["No", "NO", "n", "N", "no"]:
    birth_control = 0
    print("You indicated that you HAVE NOT used birth control.")
else:
    print("Sorry! Invalid entry! Please try again")

# probes if the user ever considered birth control
print("Question 6")
if birth_control == 0:
    considered_birth_control = input("Have you ever considered taking birth control?: ")
    if considered_birth_control in ["Yes", "YES", "y", "Y", "yes"]:
        print("You indicated that you HAVE considered taking birth control.")
    elif considered_birth_control in ["No", "NO", "n", "N", "no"]:
        sys.exit("Sorry! This survey is only for women who have taken or considered taking birth control.")
else:
    print("Sorry! Invalid entry! Please try again")

# probes for age started on birth control
print("Question 7")
age_started = inputNumber("At what age did you start or consider taking birth control?: [Age must be greater than 13 and less 45]\nPlease enter an age: ")
if age_started >= 13 and age_started <= 45:
    print(f"You indicated you began or considered taking birth control at {age_started}.")
else:
    print("Invalid entry! Please try again.")

# probes for reason starting birth control
print("Question 8")
reason_started = input("What was the reason you started birth control?\nPlease select from the following:\n[1 for menstrual cramps, 2 for irregular periods, or 3 for did not want to have period every month.")
if reason_started == 1:
    print("You indicated you started birth control because of menstrual cramps.")
elif reason_started == 2:
        print("You indicated you started birth control because you were having irregular periods.")
elif reason_started == 3:
    print("You indicated you started birth control because you did not want to have your period every month.")
else:
    print("Sorry! Invalid entry! Please try again")

# probes for level of reproductive health
print("Question 9")
birth_control_ed = input("Do you think you learned enough about birth control and reproductive health when growing up?:\nPlease enter yes or no.")
if birth_control_ed in ["Yes", "YES", "y", "Y", "yes"]:
    print("You indicated you HAVE learned enough about birth control and reproductive health when growing up.")
elif birth_control_ed in ["No", "NO", "n", "N", "no"]:
    print("You indicated you HAVE NOT learned enough about birth control and reproductive health when growing up.")
else:
    print("Sorry! Invalid entry! Please try again")

# probes if users can easily talk to their doctors about birth control
print("Question 10")
doc_talk = input("Do you think you can easily talk to your doctor about birth control?\nPlease enter yes or no.")
if doc_talk in ["Yes", "YES", "y", "Y", "yes"]:
    print("You indicated you CAN easily talk to your doctor about birth control.")
elif doc_talk in ["No", "NO", "n", "N", "no"]:
    print("You indicated you CANNOT easily talk to your doctor about birth control.")
else:
    print("Sorry! Invalid entry! Please try again")

# probes for hormonal contraception usage for better employment
print("Question 11")
contraception = input("Have you ever used hormonal contraception for better employability at work?\nPlease enter yes or no.")
if contraception in ["Yes", "YES", "y", "Y", "yes"]:
    print("You indicated you HAVE used hormonal contraception for better employability at work.")
elif contraception in ["No", "NO", "n", "N", "no"]:
    print("You indicated you HAVE NOT used hormonal contraception for better employability at work.")
else:
    print("Sorry! Invalid entry! Please try again")
 
print("Question 12")
print("With this research we want to help people with a female resproductive system to make informed choices about birth control.")
volunteer = input("Would you like to help us with this and share more about your experiences?\nPlease enter yes or no:")
if volunteer in ["Yes", "YES", "y", "Y", "yes"]:
    phone_number = input("Great! Someone will be in contact with you soon.")
elif volunteer in ["No", "NO", "n", "N", "no"]:
    print("Thank you anyway. Please feel free to contact us if you change your mind.")
else:
    print("Sorry! Invalid entry! Please try again")

print("Thank you so much for your time. If you have any questions, please do not hesitate to contact us at matrixlotus@icloud.com.")