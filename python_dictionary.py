input1 = input("Give me an adjective:\n")
input2 = input("Give me an verb:\n")
input3 = input("Give me a noun:\n")
input4 = input("Give me a noun:\n")
input5 = input("Give me a verb:\n")
input6 = input("Give me an adverb:\n")
input7 = input("Give me a noun:\n")
input8 = input("Give me an adjective:\n")

words = { "first": input1,"second": input2,"third": input3,"fourth": input4,"fifth": input5,"sixth": input6,"seventh": input7,"eighth": input8}

print(f'''
 
Python is a {words["first"]} language that lets you {words["second"]} more {words["third"]} and integrates your {words["fourth"]} more effectively. 
 
You can learn to {words["fifth"]} Python and see almost {words["sixth"]} {words["seventh"]} in productivity and {words["eighth"]} maintenance costs.
 
''')
