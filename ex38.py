ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Neight", "Song", "Frisbee",
"Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

#从左边开始第二个元素
print(stuff[1])
#从右边开始第一个元素
print(stuff[-1])
#弹出最右边的元素
print(stuff.pop())
print(" ".join(stuff))
print('#'.join(stuff[3:6]))