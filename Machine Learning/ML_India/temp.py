# num = "21"

# numInspected = None
# numOfTimes = 1

# output = ""

# i = 0

# while i<len(num)-1:
#     print("evaluating: ", num[i])
#     if num[i] == num[i+1]:
#         numInspected = num[i]
#         numOfTimes += 1
#     else:
#         output += str(1)
#         output += str(num[i])
#     i +=1

# output += str(numOfTimes)
# output += str(numInspected)

# print(output)


# num = "21"
# start = 0
# counter = 0

# tempStr = str(num[0])

# output = []

# i = 0
# while i<len(num)-1:
#     print(f"i: {i},num: {num[i]}")
#     if num[i] == num[i+1]:
#         tempStr += str(num[i])
#     else:
#         print(tempStr)
#         output.append(tempStr)
#         tempStr = str(num[i+1])

#     if i == len(num)-2:
#         output.append(tempStr)
#     i +=1

# output2 = ""
# for chunk in output:
#     output2 += str(chunk.count(chunk[0]))
#     output2 += str(chunk[0])

# print(output2)
# # return output2

def countAndSay(n):
    if n == 1:
        return "1"
    elif n==2:
        return "11"

    solution = ""
    
    j = 3

    num = "21"
    while j < n:
        tempStr = str(num[0])

        output = []

        i = 0
        while i<len(num)-1:
            # print(f"i: {i},num: {num[i]}")
            if num[i] == num[i+1]:
                tempStr += str(num[i])
            else:
                # print(tempStr)
                output.append(tempStr)
                tempStr = str(num[i+1])

            if i == len(num)-2:
                output.append(tempStr)
            i +=1

        output2 = ""
        for chunk in output:
            output2 += str(chunk.count(chunk[0]))
            output2 += str(chunk[0])
        
        num = output2
        j += 1    

    return output2


print(countAndSay(5))







# for i in range(len(num)-1):
#     print("evaluating: ", num[i])
#     if num[i] != num[i+1]:
#         if counter == 0:
#             print(num[start:i+1])
#         if counter != 0:

#         start = i+1
#         counter = 0
#     else 

