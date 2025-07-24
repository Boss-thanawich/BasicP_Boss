# x = {"name":"Boss","SID":"133"}

# print(x["name"],x["SID"])

# x["score"] = 99
# print(x)

# x["name"] = "Pee"
# print(x)

#------------EX-----------------------

students = [ {"name":"Boss","id":133,"score":80},
            {"name":"Pee","id":000,"score":100},
]

# print(students[0]["name"])

for student in students:
    if (student["score"] >= 90):
        student["score"] = "A"
    elif (student["score"] >= 80):
        student["score"] = "B"
    elif (student["score"] >= 70):
        student["score"] = "C"
    else :
        student["score"] = "F"
    print(student)
    