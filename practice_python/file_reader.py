with open('file_to_be_read.txt', 'r') as open_file:
    all_text = open_file.read()
    all_text = all_text.split('\n')
    print(len(all_text))
