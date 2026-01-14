#Make a class for Cricketers, and record their runs in ODI, T20Is and Tests
class Cricketers:
    name = ""
    runs_in_ODIs = 0

virat_kohli = Cricketers()
virat_kohli.name = "Virat Kohli"
virat_kohli.runs_in_ODIs = 14181

rohit_sharma = Cricketers()
rohit_sharma.name = "Rohit Sharma"
rohit_sharma.runs_in_ODIs = 11168

ms_dhoni = Cricketers()
ms_dhoni.name = "Mahendra Singh Dhoni"
ms_dhoni.runs_in_ODIs = 10773

#print(f"Name: {virat_kohli.name} , Runs: {virat_kohli.runs_in_ODIs}")
#print(f"Name: {rohit_sharma.name} , Runs: {rohit_sharma.runs_in_ODIs}")
#print(f"Name: {ms_dhoni.name} , Runs: {ms_dhoni.runs_in_ODIs}")

mylist = [virat_kohli,rohit_sharma,ms_dhoni]
#mylist = [Cricketers(name="vk", runs_in_ODIs=100), Cricketers(name="rs", runs_in_ODIs=200),Cricketers(name="ms", runs_in_ODIs=300)]
mylist.sort(key=lambda x: x.runs_in_ODIs, reverse=True)

print(mylist)