
Subject = ('English', 'Hindi', 'Mathematics', 'Computer Science', 'Physics', 'Chemistry')  
Year = (2001, 2002, 2003, 2004, 2005, 2006)  

if len(Subject) == len(Year):  
    Dict = {Subject[i]: Year[i] for i, _ in enumerate(Year)}  
    print("The dictionary is: ", Dict) 
