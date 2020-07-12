import time



def construct_list(total):
    i = 0 
    numbers = []
    print(f"total = {total}")

    while i < total:
        #print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        #print("Numbers now: ", numbers)
        #print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        1
        #print(num)
    
tick = time.time()
print(tick)
construct_list(1000000)
tick = time.time()
print(tick)