try:
    file = open("sample.txt","r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")