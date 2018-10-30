def xxx(num):
    if num >=1:
       result=num * xxx(num-1)
    else:
        result =1
    return result

aaaf = xxx(4)
print(aaaf)