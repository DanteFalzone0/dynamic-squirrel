import re
import sys

title = []
author = []
coauth = [] # Bool to put 'et al.' after the author's name or not.
pub_date = []
page_num = []


def get_title():
    print("Input the title of the book for which you wish to create a citation.")
    title_inp = input()
    title.append(title_inp)
    print("\nThis is what you typed in: " + title[0] + "\n")
    print("Is that what you want to put in your database? If so, then type 'y' and press ENTER;")
    print("if not, then type 'n' and press ENTER. To exit the program, type anything else and\npress ENTER.")
    choice = input()
    if choice == 'y':
        get_author()
    if choice == "n":
        title.clear()
        print("The title you typed in hasn't been saved.")
        print('\n')
        get_title()
    else:
        sys.exit()


def get_author():
    print("Input the name of the main author of *" + title[0] + "* and press ENTER.")
    author_inp = input()
    author.append(author_inp)
    print('\n')
    print("The name you typed in was \"" + author[0] + "\". If that's correct, type 'y' and press ENTER.")
    print("If not, then type anything else and press ENTER.")
    choice = input()
    if choice == 'y':
        print("\nDid they have any coauthors? If so, press 'y' and press ENTER. If not, press anything else and")
        print("press ENTER.")
        coauth_choice = input()
        if coauth_choice == 'y':
            coauth.append('TRUE')
            print("In that case, the program will put 'et al.' after the author's name.")
            get_pub_date()
        else:
            coauth.append('FALSE')
            get_pub_date()
    else:
        author.clear()
        print("The name you typed in hasn't been saved.\n")
        get_author()


def get_pub_date():
    print("\nInput the date of publication for that work (in the format \"dd month yyyy\") and press ENTER.")
    pub_date_inp = input()
    pub_date.append(pub_date_inp)
    print("\nThe date you entered was " + pub_date[0] + ". Is that correct? If so, press 'y' and press ENTER; if")
    print("not, press anything else and press ENTER.")
    choice = input()
    if choice == 'y':
        get_pagenum()
    else:
        pub_date.clear()
        print("\nThe data you entered has not been saved.")
        get_pub_date()


def get_pagenum():
    print("\nInput the page number you wish to cite and press ENTER.")
    try:
        page_num.append(int(input()))
        print("The page number has been saved as " + str(page_num) + ".")
        save_info()
        pass
    except ValueError:
        page_num.clear()
        print("Sorry, the page number must be Arabic numerals only. Please try again.")
        get_pagenum()


def save_info():
    coauth_val = ''
    if coauth[0] == 'TRUE':
        coauth_val = ' et al.'
    else:
        pass
    citation_file = open("citations.txt")
    old_citations = str(citation_file.read())
    citation_file.close()
    new_citation = open("citations.txt", "w+")
    new_citation.write(old_citations +
                       "\n" + title[0] +
                       "\n" + author[0] + coauth_val +
                       "\n" + pub_date[0] +
                       "\nPage " + str(page_num[0]) + "\n")
    new_citation.close()


get_title()
