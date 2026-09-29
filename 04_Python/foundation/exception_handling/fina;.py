while True: 
   try:
    att=float(input("Enter attendance: "))
    if not 0<=att<100:
     raise ValueError("Kindly enter valid attendance between 0 to 100")
    else:
     print("Attendance",att)
    break     

   except ValueError:
     print("Invalid Attendance")    