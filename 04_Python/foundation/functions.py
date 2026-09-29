marks = int(input("Enter your marks:"))
if (marks >= 90):
    print("Grade O")
elif (marks >= 80 ) :
    print("Grade A")   
elif (marks >= 70 ) :
    print("Grade B") 
elif (marks >= 60 ) :
    print("Grade C") 
elif (marks >= 40) :
    print("Grade D") 
else:
    print("Fail")
        
#Lambda
# square =lambda square : square **2
# print (square(5))

# increase by 10% 
# prices = [100,200,300]
# result = list(map (lambda x:x * 1.10 , prices))
# print(result)

# # # to comvert the result from dec to int
# # prices = [100,200,300]
# # result = list(map (lambda x:int(x * 1.10) , prices))
# # print (result)

# # find only even numbers
# numbers = [1,2,3,4,5,6]
# result = list(filter(lambda numbers:numbers % 2 == 0,numbers))
# print(result)

# # using functions find even
# numbers = [1,2,3,4,5,6]
# even=[]
# for num in numbers:
#     if numbers %2==0:
#         even.append(numbers)
#         print(even)















