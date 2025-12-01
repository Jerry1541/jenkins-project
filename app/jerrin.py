'''
NAME: Jerrin T.
DATE: 12/01/2025
DESCRIPTION: Main file to run the program.
'''

from datetime import date

today = date.today()

def callUser(username):
    print(f"Hello {username}. Today's date is {today}")

def main():
    callUser("Jerry")

if __name__ == "__main__":
    main()