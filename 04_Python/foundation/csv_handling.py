import csv 

with open(r"C:\Angel\04_Python\foundation\data.csv","a",newline="") as file:
    # reader=csv.reader(file)
    # for row in file:
    #     # print(row)
    #     print(file)
    # reader=csv.DictReader(file)
    # for row in reader:
    #     print(row["Dept"])

    writer=csv.writer(file)
    writer.writerows([["Michale","BSc"],["Jeffrey","MSc"]])

    