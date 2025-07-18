#user_input = input("Enter something: ")
#print("You entered:", user_input)
#print("This is the type:", type(user_input)

#import random
#print(random.randrange(1,10))

#fruits =["apple","bannna"]
#fruits.append("mango")
#print(fruits)
   
#fruits.insert("orange")
#print(fruits)
#fruits.remove("bannna")
#print(fruits)
#fruits.pop() #for delet last vlue 
#print(fruits)

 #sort= arrange the values 
#number =[1,3,7,5,6,]
#number.sort()
#print(number)

 #reverse =
#number =[1,3,7,5,6,]
#number.reverse()
#print(number)
 
# length =find length  by using indexing 
#a=("sahil")
#print(len(a))
 
 #lower
#s="hello"
#print(s.lower())

# upper 
#s="hello"
#print(s.upper())

#student = {
 #   "name": "sahil",
  #  "age": 18
#}

#print(student)


#students={
 #   "student1":{
  #      "name""sahil",
 #  },
   # "student2":{
    #    "name":"ram",
     #   "age":"19"
 #   }
#}
#total_age = students["student1"]["age"]+students["student2"]["age"]
#print("Total age of both students", total_age )

#students= [
 #       {" student name ":"sahil","age":27,"roll number":}
#]
 
students = [
        
        
        {"studentname": "Tushar", 
          
           "age": 25, 
            
            "rollnumber": 179},
       
       {"studentname": "Riya",
       
           "age": 22, 
       
           "rollnumber": 183},
       
       {"studentname": "Aman",
       
          "age": 24, 
          
            "rollnumber": 175},
      
       {"studentname": "Sneha", 
      
          "age": 23, 
      
           "rollnumber": 123},
      
       {"studentname": "Kunal", 
      
           "age": 23, 
      
            "rollnumber": 222},
      
       {"studentname": "shivam ",
      
           "age": 20,
      
            "rollnumber": 209},
      
      
      {"studentname": "abhishek", 
      
           "age": 20, 
      
      
           "rollnumber": 210},
      
      {"studentname": "ram",
      
      
           "age": 18,
      
           "rollnumber": 204},
      
      {"studentname": "sahil",
      
          "age": 19, 
      
           "rollnumber": 246},
       {"studentname": "Simran", 
      
         "age": 18, 
      

          "rollnumber": 205}
]

for sahil in students:
    print(f"{sahil['studentname']} {sahil['age']} , {sahil['rollnumber']}")
