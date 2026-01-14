def error_raise():
    try:
        res="hello"*"world"
    except Exception as e:
        print(f"Caught in errorraise: {e}")
        raise
    

def call_error_raise():
    try:
        error_raise()
    except Exception as e:
        print(f"Handled at top level: {e}")

call_error_raise()




