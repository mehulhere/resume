import webbrowser
import time
import msvcrt
import os

# Functions to print text in green color
def print_green(text):
    print("\033[38;2;0;255;0m" + text + "\033[0m", end = "")
    
def print_hyperlink(text, url):
    print(f'\033]8;;{url}\033\\{text}\033]8;;\033\\', end ="")
    
def smallsleep():
    time.sleep(0.15)
    
def bigsleep():
    time.sleep(0.30)
# Functions to display different sections of the resume
def welcome_message():
    print_green("\nWelcome to Mehul Pahuja's interactive resume.\n")
    # bigsleep()
    print("1. Academic Background")
    # smallsleep()
    print("2. Career Objectives")
    # smallsleep()
    print("3. Coding Skills")
    # smallsleep()
    print("4. Work Summary(Projects)")
    # smallsleep()
    print("5. Contact Information\n")

def coding_skills():
    smallsleep()
    print_green("CODING SKILLS\n")
    bigsleep()
    print("- Advanced Python: Web Development(Front & Back End), Web Scraping, OS, etc")
    smallsleep()
    print("- C/C++: Multithreading, concurrency, memory management, etc")
    smallsleep()
    print("- Java: JavaFX, Scene Builder, Game Development, Multithreading")
    smallsleep()
    print("- Supervised Machine Learning")
    smallsleep()
    print("- Prolog Programming")
    smallsleep()
    print("- MySQL/SQL Management\n")
    smallsleep()

def academic_background():
    smallsleep()
    print_green("Academic Background\n")
    bigsleep()
    print_green("BTECH IN COMPUTER SCIENCE & AI\n")
    smallsleep()
    print_green("IIITD | 2022-2026\n")
    smallsleep()
    print("SEM 1 SGPA: 9.2")
    smallsleep()
    print("SEM 2 SGPA: 7.8")
    smallsleep()
    print("CGPA: 8.4")
    smallsleep()
    print("A+ in OS(Batch Topper)\n")
    smallsleep()

    bigsleep()
    print_green("SCHOOL EDUCATION\n")
    smallsleep()
    print_green("General Raj's School | 2010-2022\n")
    smallsleep()
    print("- CBSE Class XII: 96% PCM + CS (School Rank 1)")
    smallsleep()
    print("- CBSE CLASS X: 97% (School Rank 1)")
    smallsleep()
    print("- School Basketball Team (2018-2020)")
    smallsleep()
    print("- International Olympiad of Mathematics (School Rank 1)")
    smallsleep()
    print("- Denmark Cultural Exchange (2017-2019)")
    smallsleep()
    print("- Fever FM 2016 Children's Day GK Content Winner (Sponsored Family vacation to Dubai)\n")
    smallsleep()

def career_objectives():
    smallsleep()
    print_green("Career Objectives\n")
    bigsleep()
    print("I am a second-year student currently pursuing a BTECH at IIITD. I aim to secure a challenging role that allows me to demonstrate my abilities and actively contribute to the advancement of the organization.\n")
    bigsleep()

def work_summary():
    smallsleep()
    print_green("WORK SUMMARY(PROJECTS)\n\n")
    bigsleep()
    print_green("1. CleanUrDownloads ")
    # smallsleep()
    print_hyperlink("click\n", "https://github.com/mehulhere/cleanurdownloads")
    bigsleep()
    print("A one-click solution to declutter your unorganized downloads folder. Coded in Python using OS module\n")

    print_green("2. JavaFX Game ")
    # smallsleep()
    print_hyperlink("click\n", "https://github.com/mehulhere/StickMan-Game")
    bigsleep()
    print("PC adaption of Ubisoft's “Stick Hero” game featuring captivating prison-themed visuals, diverse characters, and multiple gameplay themes with an in-game currency as you progress.\n")

    print_green("3. ZCS Shell(Zombie Child Shell) ")
    # smallsleep()
    print_hyperlink("click\n", "https://github.com/mehulhere/ZCS-Shell")
    bigsleep()
    print("A custom zombie themed shell and is a significantly advanced version of one of our OS assignments with Incorporate operational commands such as 'word,' 'dir,' 'date,' 'rm,' 'cd,' 'ls,' 'pwd,' 'grep,' and much more to be added.\n")

    print_green("4. Cupid Discord Bot ")
    # smallsleep()
    print_hyperlink("click\n", "https://github.com/mehulhere/Cupid-Bot")
    bigsleep()
    print("Cupid is a matchmaking Discord bot that pairs users based on their common interests and gender preferences. It enables anonymous chatting and users can reveal their identities when they are comfortable. It also has various moderation features. It is written in Python and uses Discord APIs for handling multiple conversations at the same time.\n")

    print_green("5. Railway Reservation System ")
    # smallsleep()
    print_hyperlink("click\n", "https://github.com/mehulhere/Railway-Reservation-System")
    bigsleep()
    print("Highly realistic simulation of a railway booking platform as a class XII Python project using HTML, CSS, FLASK, Python and a lot of APIs (Google Maps, NgRok, Difflib, etc)\n")
    option = -1
    while option != 0:
        option = int(input("\nPlease enter your choice (0 to exit): "))
        if option == 1:
            url = 'https://github.com/mehulhere/cleanurdownloads'
            webbrowser.open(url)
        elif option == 2:     
            url = "https://github.com/mehulhere/StickMan-Game"
            webbrowser.open(url)
        elif option == 3:
            url = "https://github.com/mehulhere/ZCS-Shell"
            webbrowser.open(url)
        elif option == 4:
            url = "https://github.com/mehulhere/Cupid-Bot"
            webbrowser.open(url)
        elif option == 5:
            url = "https://github.com/mehulhere/railway-reservation-system"
            webbrowser.open(url)
        else:
            pass
            

def contact_information():
    print_green("My contact information: (clickable links)\n")
    bigsleep()
    print("Telephone: (+91)7838844887")
    smallsleep()
    print("Email: ", end = "")
    print_hyperlink("mehul22295@iiitd.ac.in\n", "https://mail.google.com/mail/?view=cm&to=mehul22295@iiitd.ac.in")
    smallsleep()
    print("LinkedIn: ", end="")
    print_hyperlink("@mehulpahuja\n", "https://www.linkedin.com/in/mehulpahuja/")
    smallsleep()
    print("github: ", end = "")
    print_hyperlink("@mehulhere\n","http://github.com/mehulhere")
    smallsleep()
    print("Address: 65/2, Yusuf Sarai, Gautam Nagar Road, New Delhi 110016, India\n")
    smallsleep()

# Main program loop
def main():
    option = -1

    while option != 0:
        os.system("cls")
        welcome_message()
        bigsleep()
        option = int(input("Please enter your choice: "))
        os.system("cls")
        print()

        if option == 1:
            academic_background()
            print("Press any key to continue...")
            msvcrt.getch()
        elif option == 2:
            career_objectives()
            print("Press any key to continue...")
            msvcrt.getch()
        elif option == 3:
            coding_skills()
            print("Press any key to continue...")
            msvcrt.getch()
        elif option == 4:
            work_summary()
        elif option == 5:
            contact_information()
            print("Press any key to continue...")
            msvcrt.getch()
        else:
            print_green("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
