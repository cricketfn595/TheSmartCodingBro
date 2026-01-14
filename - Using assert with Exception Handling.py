import traceback
x=-5
try:
    assert x>0,"x must be positive"
except AssertionError as e:
    print("AssertionError: ",e)
    traceback.print_exc()
