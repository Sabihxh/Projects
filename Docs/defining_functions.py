def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

# ask_ok('Do you have to overwrite your memories? ', 2)


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

# parrot(32000, action = 'Epitome', type = 'VOOOOOM')

def super_new(compulsory, *optional, **WTFFFanything):
    print '*'*60
    print 'Compulsory statement is coming: '
    print '*'*60
    print 'I have a %s statement for you' % compulsory
    print '\n'

    print '*'*60
    print 'Next comes the optional statement/s: '
    print '*'*60
    for optionality in optional:
        print 'This is option statement: %s' % optionality
    print '\n'
    print '*'*60
    print 'Next comes the super optional stuff: '
    print '*'*60

    for key in sorted(WTFFFanything.keys(), reverse = True):
        print '%s: %s' % (key, WTFFFanything.get(key))

    print '\n'

compulsory = 'compulsory'
o1 = 'WHAAHAAAAAAAAAAAAAAAA' 
o2 = 'HUUUUHHHH????'
o3 = 'what what, what, what'

super_new('compulsory', o1, o2, o3, Try = 'I can do this', Fly = 'I can do this', Die = 'Not yet')
















