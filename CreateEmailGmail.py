#imports 
import random
import uuid
import imaplib
import email
import string
import sqlite3 
import time
import re
from email.header import decode_header
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def XCreateAcc():
    try:
        # Open the website
        driver.get("https://www.x.com")

        # Wait for the Create Account Button and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/a"))
        ).click()

        # Wait for the Name input field to appear
        input_Name = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/label/div/div[2]/div/input"))  
        )
        input_Name.clear()
        global Name
        Name = GenerateRandomName()
        input_Name.send_keys(Name)
        
        # Wait for the Email input field to appear
        input_Email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/label/div/div[2]/div/input"))  
        )
        input_Email.clear()
        global Email
        Email = GenerateRandomEmail()
        input_Email.send_keys(Email)
        
        # Birthdaty Selection
        Month,Day,Year = BrithDateGeneration()
        global BirthDate
        BirthDate = str(Year)+str(Month)+str(Day)
        #Month Selection
        drop_down_Month_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[3]/div/div[1]'))  
        )
        drop_down_Month_element.click()
        
        # Select the Months option
        Month_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//option[text()="{Month}"]'))  # Adjust XPath to match the visible text
        )
        Month_element.click()        
         
        #Day Selection
        drop_down_Day_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[3]/div/div[2]'))  
        )
        drop_down_Day_element.click()

        # Select the Day option
        Day_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//option[text()="{Day}"]'))  # Adjust XPath to match the visible text
        )
        Day_element.click()   
        
        #Year Selection
        drop_down_Year_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[3]/div/div[3]'))  
        )
        drop_down_Year_element.click()
        # Select the Year option
        Year_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//option[text()="{Year}"]'))  # Adjust XPath to match the visible text
        )
        Year_element.click()  

        #Click The Next Button For Countinue
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button"))
        ).click()
        
        #Click The Next Button
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button"))
        ).click()
        
        #SELF Authentication Capthcha No Ai or .. for handle this part if i have time for next update i will done this
        #Email Verify
        input_Email_Verify = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"))  
        )
        input_Email_Verify.clear()
        Email_Verify_Code = ReciveMassageEmail()
        input_Email_Verify.send_keys(Email_Verify_Code)
        
        #Click The Button For Next
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button"))
        ).click()
    
        #Set PassWord
        global Pass
        Pass = CreatePasword()
        password = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input"))  
        )
        password.clear()
        password.send_keys(Pass)
        
        #Click The Button For Next
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/button"))
        ).click()
        
        #Skip Image
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button"))
        ).click()
        
        #Copy Our UserName Then Skip For Now
        Username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"))
        )
        global UserName_value
        UserName_value = Username.get_attribute("value")
        #print(UserName_value)
        
        #Skip ID
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button"))
        ).click()
        
        #Skip Notif
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/button[2]"))
        ).click()
        
        #Click On 3 Interests
        
        #1
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div[3]/div/div/div/li[1]/div/div/div/button/div/div/div"))
        ).click()
        
        #2
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div[4]/div/div/div/li[1]/div/div/div/button/div/div/div"))
        ).click()
        
        #3
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div[5]/div/div/div/li[1]/div/div/div/button/div/div/div"))
        ).click()
        
        #Next Interest
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/button"))
        ).click()
        
        #NEXT Personalaize
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/button"))
        ).click()
        
        #fOLLOW 1 OR MORE ACCS
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/section/div/div/div[3]/div/div/button/div/div[2]/div/div[2]/button"))
        ).click()
        
        #Next After Follow
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button"))
        ).click()
        #IT IS FINISHED CREATION    
    except TimeoutException:
        print("An element took too long to load.")
    finally:
        # Close the browser
        driver.quit()
        
def GenerateRandomEmail():
    Email = "YourEmailHere" + "+" + str(uuid.uuid4()) + "@gmail.com"
    return Email

def GenerateRandomName():
    first_names = [
        "John", "Emma", "Oliver", "Sophia", "Liam", "Isabella", 
        "Mason", "Mia", "Noah", "Ava", "Ethan", "Emily", 
        "James", "Charlotte", "Benjamin", "Amelia", "Lucas", 
        "Harper", "Elijah", "Evelyn", "Alexander", "Abigail",
        "William", "Ella", "Henry", "Scarlett", "Daniel", 
        "Aria", "Sebastian", "Penelope", "Matthew", "Luna"
    ]
    last_names = [
        "Smith", "Johnson", "Brown", "Williams", "Jones", 
        "Garcia", "Miller", "Davis", "Martinez", "Hernandez",
        "Lopez", "Gonzalez", "Wilson", "Anderson", "Taylor",
        "Thomas", "Moore", "Jackson", "Martin", "Lee",
        "Perez", "Thompson", "White", "Harris", "Sanchez",
        "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
        "Young", "Allen", "King", "Scott", "Green"
    ]
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

def BrithDateGeneration():
    Month = ['January','February','March','April','May','June','July','August','September','October','November','December']
    Year  = list(range(1990,2006))
    Day   = list(range(1,32))
    Month_Selected = random.choice(Month)
    Year_Selected = random.choice(Year)
    Day_Selected = random.choice(Day)
    return Month_Selected,Day_Selected,Year_Selected
    
def CreatePasword():
    # Define the character set
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    # Generate a random password
    password = ''.join(random.choices(characters, k=13))
    return password

#Create data base for first time
def CreateDataBase():
    
    #DB Name
    DB_Name = "XAccs.db"
    
    #Schema
    schema = """
    CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Full_Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    BirthDay TEXT NOT NULL,
    Password TEXT NOT NULL,
    User_Id TEXT UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    Activation TEXT DEFAULT Not_Activate,
    is_follow INTEGER NOT NULL DEFAULT 0
    );
    """
    with sqlite3.connect(DB_Name) as conn:
        cursor = conn.cursor()
        cursor.executescript(schema)
        print(f"Database {DB_Name} created with the provided structure.")
        
def SaveDatas(Name, Email, BirthDay, Password, UserId):
    DB_Name = "XAccs.db"
    
    # Use placeholders for the values in the SQL query
    insert_users = """
    INSERT INTO users (Full_Name, Email, BirthDay, Password, User_Id)
    VALUES (?, ?, ?, ?, ?);
    """
    
    with sqlite3.connect(DB_Name) as conn:
        cursor = conn.cursor()
        
        # Execute the INSERT query with parameters
        cursor.execute(insert_users, (Name, Email, BirthDay, Password, UserId))
        
        # Commit the changes
        conn.commit()
        
    print("Data inserted successfully.")

def ReciveMassageEmail():
    # Connect to Gmail
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('YourEmailHere@gmail.com', 'YourPasswordHere')

    # Select the inbox
    mail.select("inbox")

    # Search for all emails
    result, data = mail.search(None, "ALL")

    # Check if emails exist
    if data[0]:
        ids = data[0]  # Data is a list
        id_list = ids.split()  # Split IDs into a list
        latest_email_id = id_list[-1]  # Get the latest email ID

        # Fetch the email body (RFC822) for the given ID
        result, data = mail.fetch(latest_email_id, "(RFC822)")

        # Extract raw email
        raw_email = data[0][1]

        # Parse raw email to a message object
        msg = email.message_from_bytes(raw_email)

        # Decode the subject
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")

        return(subject[0:6])

    # Logout from the mail server
    mail.logout()
    
    # Return None if no emails or code found
    return None  
def XFollowUser(user_id,password):
    try:
        
        # Open the website
        driver.get("https://x.com/i/flow/login")
        
        #Fill User_ID
        Id_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input"))  
        )
        Id_input.clear()
        Id_input.send_keys(user_id)
        
        #Click The Next
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]"))
        ).click()
        
        #Enter The pass for user
        pass_Input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"))  
        )
        pass_Input.clear()
        pass_Input.send_keys(password)
        
        #Select LogIn
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button"))
        ).click()
        
        #travel to my page to follow
        #Click on The Search Bar
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]"))
        ).click()
        
        #Click on tne input Serch Bar
        follow_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input"))  
        )
        follow_input.clear()
        follow_input.send_keys('YourAccHere')
        follow_input.send_keys(Keys.RETURN)
        
        #Follow Buttton
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[3]/div/div/button/div/div[2]/div/div[2]/button"))
        ).click()
        
    except TimeoutException:
        print("An element took too long to load.")
    finally:
        # Close the browser
        driver.quit()
        
def CountNotFollowUser():
    DB_Name = "XAccs.db"

    # Query to count the number of users where is_follow is 0
    count_query = "SELECT COUNT(*) FROM users WHERE is_follow = 0;"

    with sqlite3.connect(DB_Name) as conn:
        cursor = conn.cursor()
        
        # Execute the query
        cursor.execute(count_query)
        
        # Fetch the result (the count)
        count = cursor.fetchone()[0]
        
        return count
def ReadDB_First_User_Not_Follow():
    DB_Name = "XAccs.db"

    # Query to get the first user_id and password where is_follow = 0
    query = "SELECT User_Id, Password FROM users WHERE is_follow = 0 LIMIT 1;"

    with sqlite3.connect(DB_Name) as conn:
        cursor = conn.cursor()
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch the first matching row (user_id, password)
        result = cursor.fetchone()
        
        if result:
            return result
        
        #Will Never Happend Hope So
        else:
            print("No user found with is_follow = 0.")

def Update_Follow_DB_Not_Follow(user_id):
    DB_Name = "XAccs.db"

    # SQL query to update is_follow to 1 for the given username where is_follow is 0
    update_query = """
    UPDATE users
    SET is_follow = 1
    WHERE User_Id = ? AND is_follow = 0;
    """

    with sqlite3.connect(DB_Name) as conn:
        cursor = conn.cursor()
        
        # Execute the update query with the provided username
        cursor.execute(update_query, (user_id,))
        
        # Commit the changes
        conn.commit()

        # Check if any row was updated
        if cursor.rowcount > 0:
            print(f"Successfully updated 'is_follow' to 1 for username: {user_id}")
        else:
            print(f"No update made. Either the username does not exist or 'is_follow' was already 1.")

def ActiveUsers(user_id,password):
    try:
        
        # Open the website
        driver.get("https://x.com/i/flow/login")
        
        #Fill User_ID
        Id_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input"))  
        )
        Id_input.clear()
        Id_input.send_keys(user_id)
        
        #Click The Next
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]"))
        ).click()
        
        #Enter The pass for user
        pass_Input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"))  
        )
        pass_Input.clear()
        pass_Input.send_keys(password)
        
        #Select LogIn
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button"))
        ).click()
        
        #Select Start
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/form/input[6]"))
        ).click()
        
        #Select Send Mail
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/form/input[5]"))
        ).click()
        
        #Send Code That We Recive
        Verify = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/form/input[5]"))  
        )
        Verify.clear()
        Verify.send_keys(ReciveMassageEmailOnBody())
        
        #Click Verify
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/form/input[6]"))
        ).click()
        
        #Click Continue To X
        WebDriverWait(driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/form/input[6]"))
        ).click()
        
    except TimeoutException:
        print("An element took too long to load.")
    finally:
        # Close the browser
        driver.quit()
        pass
def NotActive():
    DB_Name = "XAccs.db"

    # SQL query to count users where Activation is 'Not_Activate'
    count_query = "SELECT COUNT(*) FROM users WHERE Activation = 'Not_Activate';"

    with sqlite3.connect(DB_Name) as conn:
        cursor = conn.cursor()
        
        # Execute the query
        cursor.execute(count_query)
        
        # Fetch the result (the count)
        count = cursor.fetchone()[0]
        
        return count

def get_user_with_not_activated():
    DB_Name = "XAccs.db"

    # SQL query to get user_id and password for the first row with Activation = 'Not_Activate'
    query = "SELECT User_Id, Password FROM users WHERE Activation = 'Not_Activate' LIMIT 1;"

    with sqlite3.connect(DB_Name) as conn:
        cursor = conn.cursor()
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch the result (the user_id and password)
        result = cursor.fetchone()
        
        if result:
            return result
        else:
            print("No user found with Activation = 'Not_Activate'.")

def update_activation(user_id):
    DB_Name = "XAccs.db"

    # SQL query to update Activation to 'Activate' for the given user_id
    update_query = "UPDATE users SET Activation = 'Activate' WHERE User_Id = ?;"

    with sqlite3.connect(DB_Name) as conn:
        cursor = conn.cursor()
        
        # Execute the update query with the provided user_id
        cursor.execute(update_query, (user_id,))
        
        # Commit the changes
        conn.commit()

        # Check if any row was updated
        if cursor.rowcount > 0:
            print(f"Successfully updated 'Activation' to 'Activate' for user_id: {user_id}")
        else:
            print(f"No update made. The user_id may not exist.")
            
def ReciveMassageEmailOnBody():
    # Connect to Gmail
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('YourEmailHere', 'YourPassHere')

    # Select the inbox
    mail.select("inbox")

    # Search for all emails
    result, data = mail.search(None, "ALL")

    # Check if emails exist
    if data[0]:
        ids = data[0]  # Data is a list
        id_list = ids.split()  # Split IDs into a list
        latest_email_id = id_list[-1]  # Get the latest email ID

        # Fetch the email body (RFC822) for the given ID
        result, data = mail.fetch(latest_email_id, "(RFC822)")

        # Extract raw email
        raw_email = data[0][1]

        # Parse raw email to a message object
        msg = email.message_from_bytes(raw_email)

        # Check if the email is multipart
        if msg.is_multipart():
            # Iterate over the email parts
            for part in msg.walk():
                # Extract content type of the email
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                # If the email part is text/plain or text/html
                if "attachment" not in content_disposition:
                    payload = part.get_payload(decode=True)
                    if payload:
                        body = payload.decode(errors="ignore").strip()  # Clean up any extra spaces/newlines
                        #print("Body:", body)  # Debug print

                        # Search for 6-digit code in the body using regex
                        match = re.search(r'\b\d{6}\b', body)
                        if match:
                            result = (match.group(0))  # Debug print
                            return result
if __name__ == "__main__":
    # Specify the path to geckodriver
    service = Service("/usr/bin/geckodriver")  
    driver = webdriver.Firefox(service=service)   
    
    while (True):
        print("This is My App In Teriminal. \n Type '1' for Create Account. \n Type '2' for close. \n Type '3' for ReActivate Accounts in DataBase. \n Type '4' for follow your Account. \n Type '5' for Count Users That Not Follow You.")
        input_user = int(input()) 
        if input_user == 1 :
            Count_Of_User_Creation = int(input("How Many User Do You Want To Create? \n"))
            for _ in range (Count_Of_User_Creation):
                XCreateAcc()
                SaveDatas(Name , Email , BirthDate , Pass , UserName_value)
                driver = webdriver.Firefox(service=service)   
                time.sleep(10)
        elif input_user == 2:
            quit()
        elif input_user == 3: 
            for _ in range (NotActive()):
                user_id, password = get_user_with_not_activated()
                ActiveUsers(user_id,password)
                update_activation(user_id)
                driver = webdriver.Firefox(service=service)   
                time.sleep(10)
        elif input_user == 4: 
            Count_Of_User_Follow = int(input("How Many User Do You Want To Follow You? \n"))
            if(CountNotFollowUser() >= Count_Of_User_Follow ):
                for _ in range(Count_Of_User_Follow):
                        user_id, password = ReadDB_First_User_Not_Follow()
                        XFollowUser(user_id,password)
                        Update_Follow_DB_Not_Follow(user_id)
                        driver = webdriver.Firefox(service=service)
                        time.sleep(10)
            else:
                print('We Dont Have That Much User')
                time.sleep(10)
        elif input_user == 5:
            print(f"Number of users that not follow you is : {CountNotFollowUser()}")
            time.sleep(10)


