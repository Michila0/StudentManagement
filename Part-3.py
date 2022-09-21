# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1904447
# Date:18/04/2022

ProgressItem = 0
TrailerItem = 0
RetrieverItem = 0
ExcludedItem = 0
list1 = []
list2 = []
list3 = []
list4 = []

print("Staff version with histogram\n")

while True: # full program boolean loop
    
    while True:         #start loop PASS credit-Integer required,Out of range
        try:                                                         #try block test a block of code for errors
            Pass =int(input('Enter your total PASS credits: '))  
            
        except ValueError:         #except block handle the error       
            print('Integer required ')
            continue      #right path way continue enter pass

        else:   #else block execute code when there is no error(NOT if-else)
                #reference: https://www.w3schools.com/python/python_try_except.asp
            isPass = False  #variable = booleanvalue
            for x in range(0, 121, 20):
                if Pass == x:
                    isPass = True
            if isPass == True:
                break #skipping next credit value
            else:
                print("Out of range")
                



    while True:   #start loop DEFER credit-Integer required,Out of range
        try:
            Defer =int(input('Enter your total DEFER credits:')) 

        except ValueError:                
            print('Integer required ')
            continue

        else:
            isDefer = False
            for x in range(0, 121, 20):
                if Defer == x:
                    isDefer = True
            if isDefer == True:     
                break
            else:
                print("Out of range")

    
    



    while True:   #start loop FAIL credit-Integer required,Out of range
        try:
            Fail =int(input('Enter your total FAIL credits: '))  

        except ValueError:                
            print('Integer required ')
            continue

        else:
            isFail = False
            for x in range(0, 121, 20):
                if Fail == x:
                    isFail = True
            if isFail == True:     
                break
            else:
                print("Out of range")

    
    sum = Pass+Defer+Fail # validation sum
    if sum != 120:
        print("Total incorrect")

    
    
    if Pass == 120 and Defer == 0 and Fail == 0:  #start progress define range of the pass, defer and fail
        print("Progress")
        ProgressItem += 1
        list1.append([Pass,Defer,Fail]) #append the list1

            
    
    if Pass == 100:  #start trailer define range of the pass, defer and fail
            for range1 in range(0,21,20):
                if Defer == range1:
                    for range1 in range(0,21,20):
                        if Fail == range1:
                            print("Progress(module trailer)")
                            TrailerItem += 1
                            list2.append ([Pass,Defer,Fail]) #append the list2

    
    for range2 in range(0,81,20):    #start retriever define range of the pass, defer and fail
            if Pass == range2:
                for range3 in range(0,121,20):
                    if Defer == range3:
                        for range4 in range(0,61,20):
                            if Fail == range4:
                                print("Do not progress – module retriever")  
                                RetrieverItem += 1
                                list3.append([Pass,Defer,Fail]) #append the list3



    
    for range5 in range(0,41,20):  #start Exclude define range of the pass, defer and fail
            if Pass == range5:
                for range5 in range(0,41,20):
                    if Defer == range5:
                        for range6 in range(80,121,20):
                            if Fail == range6:
                                print("Exclude")
                                ExcludedItem += 1
                                list4.append([Pass,Defer,Fail]) #append the list4



    print("\nWould you like to enter another set of data? ")
    answer =input("Enter 'y' for yes or 'q' to quit and view results: ")   
    if answer == 'y':
        print()
        continue
        
    
    elif answer == 'q':
        print('-'*55)
        print("Horizontal Histogram")#start horizontal histogram 

        def histogram(title, number ):  #reference: https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
    
            times = number
            output = ''
            while( times > 0):
                output +='*'
                times = times-1
            if times == 0:
                print(title+str(number),':',output) 
 

        histogram("Progress   ",ProgressItem)
        histogram("Trailer    ",TrailerItem)
        histogram("Retriever  ",RetrieverItem)
        histogram("Excluded   ",ExcludedItem)

        outcome = ProgressItem + TrailerItem + RetrieverItem + ExcludedItem
        print('\n')
        print(outcome ," outcomes in total. ")
        print('-'*55)
        


    
        print('-'*55)
        print("Vertical Histogram")       #start vertical histogram                                                                                                                                                                                             

        
        header = ['Progress '+str(ProgressItem),'|Trailer '+str(TrailerItem),'|Retriever '+str(RetrieverItem),'|Excluded '+str(ExcludedItem)] #Reference:  https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops   
        print(' '.join(header))

        for x in range(max(ProgressItem,TrailerItem,RetrieverItem,ExcludedItem)):# max more than 3 argument
            print('   {0}           {1}         {2}           {3}'.format(
                '*' if x < ProgressItem else ' ',
                '*' if x < TrailerItem else ' ',
                '*' if x < RetrieverItem else ' ',
                '*' if x < ExcludedItem else ' '
                )) 

        print('\n')
        print(outcome ," outcomes in total. ")# outcome = ProgressItem + TrailerItem + RetrieverItem + ExcludedItem
        print('-'*55)    
        



     
        
        def list_histogram(title,number):     #start the LIST histogram
            
            for element in number:   #[pass,defer,fail]
                print(title,' - ',str(element)[1:-1]) 
            
  
        list_histogram('Progress',list1)
        list_histogram('Progress (module trailer)',list2)
        list_histogram('Module retriever',list3)
        list_histogram('Excluded',list4)
        break
    else:
        break