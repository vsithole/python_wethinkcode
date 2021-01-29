

def create_outline():
    """
    TODO: implement your code here
    """

    # Set
    topics = {'Introduction to Python', 'Tools of the Trade', 'How to make decisions','How to repeat code', 'How to structure data', 'Functions','Modules'} 
    topics = sorted(topics)
    print ('Course Topics:')
    for x in topics:
        print("* "+x)
      
    problist = ['Problem 1, ','Problem 2, ','Problem 3']
    newprob =""
    for i in range (len(problist)):
        newprob = newprob + problist[i]

    # Converting set to dictionary/map
    problems = {element:newprob for element in topics} 
  
    print('Problems:')
    for i,j in problems.items():
        print ("* {}{}{}".format(i," : ",j))

    # Tuple
    studentprogress = ("1. Nyari - Introduction to Python - Problem 2 [STARTED]", 
     "2. Adam - How to make decisions - Problem 1 [GRADED]", 
     "3. Vusi - How to repaet code - Problem 3 [COMPLETED]")
    
    print('Student Progress:')

    for i in range (len(studentprogress)):
        print (studentprogress[i])

    pass

if __name__ == "__main__": 
    create_outline()
