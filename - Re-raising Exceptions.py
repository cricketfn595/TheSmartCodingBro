import logging
def func():
    try:
        erroropp()
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise
    

def erroropp():
    raise ValueError("Exception occurred")

try:
    func()
except Exception as e:
    print("Handled at a higher level: ",e)

