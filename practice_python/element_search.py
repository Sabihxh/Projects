#Python_Practise_20_element_search

# def element_search(aList, aNum):
#     if aNum in aList:
#         print('True')
#     else:
#         print('False')
# element_search([1,2,3], 6)

def element_search_2(aList):
    count = len(aList)
    aNum = int(raw_input("Enter a number: "))
    while count > 0:

        if aList[count/2] == aNum:
            print('Found it')
            aList = []

        elif aList[count/2] > aNum:
            aList = aList[0:count/2]
            if len(aList) == 0:
                print('%s is not in the list'%aNum)

        elif aList[count/2] < aNum:
            aList = aList[(count/2) + 1:]
            if len(aList) == 0:
                print('%s is not in the list'%aNum)

        count = len(aList)

another_list = [2,3,4,5,6,7,8,9]
element_search_2(another_list)


