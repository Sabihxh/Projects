num_letters_dict = {'0': '', '00': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', 
'5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', 
'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', 
'14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen',
'18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30': 'thirty',
'40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty',
'90': 'ninety', '100': 'hundred' }

# print num_letters_dict
everything = ''
all_words = []

for x in range(1,1001):

    if x <= 20:
        number = '%s' % x
        words = num_letters_dict.get(number)
        all_words.append(words)

    elif x >= 21 and x <= 99:
        to_string = '%s'%x
        tens = '%s0'% to_string[0]
        ones = '%s' % to_string[1]
        words = num_letters_dict.get(tens) + num_letters_dict.get(ones)
        all_words.append(words)

    elif x == 100:
        words = 'onehundred' 
        all_words.append(words)

    elif x >= 101 and x <= 999:
        to_string = '%s'%x
        hund = '%s'% to_string[0]
        tens = '%s0'% to_string[1]

        if to_string[1] == '1':
            semi_word = num_letters_dict.get(to_string[1:])

        else:
            ones = '%s' % to_string[2]
            semi_word = num_letters_dict.get(tens) + num_letters_dict.get(ones)
        words = '%shundredand%s'%(num_letters_dict.get(hund), semi_word)
        all_words.append(words)
        print(len(words))
        
    elif x == 1000:
        words = 'onethousand'
        all_words.append(words)

print('\n'.join(all_words))
print(len(''.join(all_words)))
print(len(all_words))















