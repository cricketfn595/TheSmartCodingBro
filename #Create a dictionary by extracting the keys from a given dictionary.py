#Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

resdict={}

for key in keys:
    if key in sample_dict:
        resdict[key]=sample_dict[key]

print(resdict)
