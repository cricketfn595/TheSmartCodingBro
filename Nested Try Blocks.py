class FileWritingError(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(message)
        def __str__(self):
            return f"{self.message}"
try:
    try:
        file = open("C:/Users/riku/Desktop/sample1.txt","w")
    except FileNotFoundError:
        print("File not found!")
    file.write("Hello! This is being written in the file!")
    file.close()
    file = open("C:/Users/riku/Desktop/sample1.txt","r")
    content = file.read()
    print(content)
    file.close()
except Exception as e:
    raise FileWritingError("Error while writing to file!")     