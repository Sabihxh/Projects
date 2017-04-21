import os.path

text = raw_input('Enter some text here: ')

path = os.path.abspath('.')


def filesave():
    for x in range(3):
        save = raw_input("Would you like to save your text? (Y/N)")
        if save == 'Y' or save == 'Yes':
            save_location = raw_input('Where would you like to save it? (MiniProjects or Files): ')
            file_name = raw_input('What would you like to name your file? ')

            if save_location == 'MiniProjects':
                file = open('%s/%s.txt'% (path, file_name), 'w')
                file.close()

            elif save_location == 'Files':
                file = open('%s/%s/%s.txt'% (path, save_location, file_name), 'w')
                file.write(text)
                file.close()
            break

        elif save == 'N' or save == 'No':
            print 'Goodbye'

filesave()