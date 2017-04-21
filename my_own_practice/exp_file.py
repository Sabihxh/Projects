def a_list(item):
    website = []
    email = []
    for value in item:
        if 'http' in value or 'www' in value:
            website.append(value)
        
        else:
            email.append(value)
        
    print(website)
    print(email)
    
a_list(['www.test1.com', 'www.test2.com', 'http//test3.com', 'test1@website.com'])
