# *args:不限参数个数
def print_two(*args): 
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#限定参数个数为2
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#限定参数个数为1
def print_one(ag1):
    print(f"arg1: {ag1}")

#不限参数
def print_none():
    print(f"I got nothin'. ")

print_two("Sandy", "dong")
print_two_again("sandy", "dong")
print_one("First!")
print_one("second!")

print_none()