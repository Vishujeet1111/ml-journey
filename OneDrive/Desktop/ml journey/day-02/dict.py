student = { 
    "name" : "vishujeet sharma",
    "age" : 20,
    "city" : "delhi",
    "skills" : ['python','ML']
}

print(student["name"])
print(student["skills"])

student["college"] = "PIET"
student["skills"] = "web dev"
# student["skills"].append("web dev")

for key ,value in student.items():
    print(key, ":",value)