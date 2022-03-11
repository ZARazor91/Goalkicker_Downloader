import os
import sys
import wget
from tkinter import filedialog
import webbrowser

selection = '-1'
books = [
    'Algorithms', 'Android', 'Angular2', 'AngularJS', 'Bash', 'C', 'CPlusPlus', 'CSharp', 'CSS', 'DotNETFramework',
    'EntityFramework', 'ExcelVBA', 'Git', 'Haskell', 'Hibernate', 'HTML5', 'HTML5Canvas', 'iOS', 'Java', 'JavaEE',
    'JavaScript', 'jQuery', 'Kotlin', 'LaTeX', 'Linux', 'MATLAB', 'MicrosoftSQLServer', 'MongoDB', 'MySQL', 'NodeJS',
    'ObjectiveC', 'OracleDatabase', 'Perl', 'PHP', 'PostgreSQL', 'PowerShell', 'Python', 'R', 'ReactJS', 'ReactNative',
    'Ruby', 'RubyOnRails', 'SpringFramework', 'SQL', 'Swift', 'TypeScript', 'VBA', 'VisualBasic_NET', 'XamarinForms'
]

def use_storage():
    if not os.path.exists('book_storage'):
        os.makedirs('book_storage')
    directory = str(os.path.abspath(os.path.dirname(sys.argv[0]))).replace('\\', '/') + '/book_storage/'
    return directory


os.system('cls' if os.name=='nt' else 'clear')
while selection == '-1':
    selection = input('Where to save the books?\n[1] Downloader folder\n[2] Book_storage folder\n[3] Select own '
                      'folder\n[0] Donate to GoalKicker :)\n[E] Exit program\nYour selection: ')
    if selection == '1':
        path = str(os.path.abspath(os.path.dirname(sys.argv[0]))).replace('\\', '/') + '/'
        print('\nUsing same folder as downloader')
    elif selection == '2':
        path = use_storage()
        print('\nUsing book_storage in downloader folder')
    elif selection == '3':
        path = filedialog.askdirectory() + '/'
        if path == '/':
            path = use_storage()
            print('\nUsing book_storage in downloader folder')
        else:
            print('\nSelected folder:' + path[:-1])
    elif selection == '0':
        webbrowser.open('https://www.buymeacoffee.com/GoalKickerBooks')
        input('\nOpening donation site for GoalKicker\nPress Enter to continue...')
        sys.exit()
    else:
        selection = '-1'
        os.system('cls' if os.name=='nt' else 'clear')

print('Books download started...\n')
for val in books:
    url = 'https://goalkicker.com/' + val + 'Book/' + val + 'NotesForProfessionals.pdf'
    print(val + 'NotesForProfessionals.pdf')
    wget.download(url, path + val + '.pdf')
    print('\n')
input('Books download finished...\nPress Enter to continue...')
sys.exit()
