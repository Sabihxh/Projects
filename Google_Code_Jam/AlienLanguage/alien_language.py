sample = 'sample.txt'
small = 'small.txt'
import re

def file_in_list(file_path):
    file = open(file_path, 'r')
    #put each line as an element in a list
    file_list = file.read().split('\n')
    if file_list[-1] == '':
        file_list = file_list[:-1]

    file.close()
    return file_list

def output(file_path):
#takes a text file and return the output for alien_language problem
    #2nd number in first line is the number of alien words
    number_of_alien_words = file_in_list(file_path)[0].split()[1]
    #makes a list of all the alien words
    alien_words = file_in_list(file_path)[1: 1+int(number_of_alien_words)]
    output_file = file_path.replace('.txt', '')
    file = open('%s_output.txt'%output_file, 'w')
    #signals is recieved alien words
    signals = file_in_list(file_path)[1+int(number_of_alien_words):]
    case = 1
    for word in signals:
        count = 0
        if word in alien_words:
            count += 1
        else:
            cleaned_signals = [x for x in re.split(r'[()]',word) if x != '']
            for a_word in alien_words:
                word_construct = ''
                
                if len(a_word) == len(cleaned_signals):
                    c = 0
                    for letter in a_word:
                        if letter in cleaned_signals[c]:
                            word_construct += letter
                            
                        c += 1
                if word_construct in alien_words:
                    count += 1
                    print word_construct
                    continue
        file.write('Case #%s: %s\n' % (case, count))
        case += 1
    file.close()

output(sample)
output(small)














