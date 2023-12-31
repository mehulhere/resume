import webbrowser

# Functions to print text in green color
def print_green(text):
    print("\033[38;2;0;255;0m" + text + "\033[0m", end = "")
    
def print_hyperlink(text, url):
    print(f'\033]8;;{url}\033\\{text}\033]8;;\033\\', end ="")
    
# Functions to display different sections of the resume
def welcome_message():
    print_green("\nWelcome to Mehul Pahuja's interactive resume.\n")
    print("1. Academic Background")
    print("2. Career Objectives")
    print("3. Coding Skills")
    print("4. Work Summary(Projects)")
    print("5. Contact Information\n")

def coding_skills():
    print_green("CODING SKILLS\n")
    print("- Advanced Python: Web Development(Front & Back End), Web Scraping, OS, etc")
    print("- C/C++: Multithreading, concurrency, memory management, etc")
    print("- Java: JavaFX, Scene Builder, Game Development, Multithreading")
    print("- Supervised Machine Learning")
    print("- Prolog Programming")
    print("- MySQL/SQL Management\n")

def academic_background():
    print_green("Academic Background\n")
    print_green("BTECH IN COMPUTER SCIENCE & AI\n")
    print_green("IIITD | 2022-2026\n")
    print("SEM 1 SGPA: 9.2")
    print("SEM 2 SGPA: 7.8")
    print("CGPA: 8.4")
    print("A+ in OS(Batch Topper)\n")

    print_green("SCHOOL EDUCATION\n")
    print_green("General Raj's School | 2010-2022\n")
    print("- CBSE Class XII: 96% PCM + CS (School Rank 1)")
    print("- CBSE CLASS X: 97% (School Rank 1)")
    print("- School Basketball Team (2018-2020)")
    print("- International Olympiad of Mathematics (School Rank 1)")
    print("- Denmark Cultural Exchange (2017-2019)")
    print("- Fever FM 2016 Children's Day GK Content Winner (Sponsored Family vacation to Dubai)\n")

def career_objectives():
    print_green("Career Objectives\n")
    print("I am a second-year student currently pursuing a BTECH at IIITD. I aim to secure a challenging role that allows me to demonstrate my abilities and actively contribute to the advancement of the organization.\n")

def work_summary():
    print_green("WORK SUMMARY(PROJECTS)\n\n")
    print_green("1. CleanUrDownloads ")
    print_hyperlink("click\n", "https://github.com/mehulhere/cleanurdownloads")
    print("A one-click solution to declutter your unorganized downloads folder. Coded in Python using OS module\n")

    print_green("2. JavaFX Game ")
    print_hyperlink("click\n", "https://github.com/mehulhere/StickMan-Game")
    print("PC adaption of Ubisoft's “Stick Hero” game featuring captivating prison-themed visuals, diverse characters, and multiple gameplay themes with an in-game currency as you progress.\n")

    print_green("3. ZCS Shell(Zombie Child Shell) ")
    print_hyperlink("click\n", "https://github.com/mehulhere/ZCS-Shell")
    print("A custom zombie themed shell and is a significantly advanced version of one of our OS assignments with Incorporate operational commands such as 'word,' 'dir,' 'date,' 'rm,' 'cd,' 'ls,' 'pwd,' 'grep,' and much more to be added.\n")

    print_green("4. Cupid Discord Bot ")
    print_hyperlink("click\n", "https://github.com/mehulhere/Cupid-Bot")
    print("Cupid is a matchmaking Discord bot that pairs users based on their common interests and gender preferences. It enables anonymous chatting and users can reveal their identities when they are comfortable. It also has various moderation features. It is written in Python and uses Discord APIs for handling multiple conversations at the same time.\n")

    print_green("5. Railway Reservation System ")
    print_hyperlink("click\n", "https://github.com/mehulhere/Railway-Reservation-System")
    print("Highly realistic simulation of a railway booking platform as a class XII Python project using HTML, CSS, FLASK, Python and a lot of APIs (Google Maps, NgRok, Difflib, etc)\n")
    option = -1
    while option != 0:
        option = int(input("\nPlease enter your choice (0 to go back): "))
        print()
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
            print_green("Invalid option. Please try again.\n")
            

def contact_information():
    print_green("My contact information:\n")
    print("Telephone: (+91)7838844887")
    print("Email: mehul22295@iiitd.ac.in")
    print("LinkedIn: @mehulpahuja")
    print("Address: 65/2, Yusuf Sarai, Gautam Nagar Road, New Delhi 110016\n")

# Main program loop
def main():
    option = -1

    while option != 0:
        welcome_message()
        option = int(input("Please enter your choice: "))
        print()

        if option == 1:
            academic_background()
        elif option == 2:
            career_objectives()
        elif option == 3:
            coding_skills()
        elif option == 4:
            work_summary()
        elif option == 5:
            contact_information()
        elif option == 0:
            print_green("Thank you for using the interactive resume. Goodbye!\n")
        else:
            print_green("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
