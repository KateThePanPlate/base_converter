#possible bases are based on the length of this string, with values of symbols based on their position within this string
#add and modify to your own content
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
version = "1.1.3.5"
def baseFromDecim(num, base):
    #converts an integer from base ten to given integer base
    #a portion of this function comes from a paper I found here https://arxiv.org/abs/1701.04506v1
    if str(num) == "0":
        return "0"
    values, sign = [], ""
    amt=0
    flnum = float(num)
    while (flnum - int(flnum)) != 0:
        amt += 1
        flnum *= base
    num, E = int(flnum), int(flnum)
    #try:
    #    if abs(base) < 2 or abs(base) > len(digits): # base check
    #        raise ValueError("invalid base")
    #except:
    #    error = "invalid base"
    #    return error

    if int(E) < 0 and base > 0:
        # handle negatives
        num *= -1
        sign = "-"

    while num:
        num, d = divmod(int(num), base)
        if d < 0: num += 1; d -= base # handle negative base conversion
        values.append(d)

    values.reverse()
    converted = str(sign + "".join(digits[i] for i in values))
    if amt != 0:
        convlist = list()
        for x in range(len(converted)):
            convlist.append(converted[x])
        convlist.reverse()
        convlist.insert(amt, ".")
        convlist.reverse()
        convertedfinal = ""
        for x in range(len(convlist)):
            convertedfinal += convlist[x]
    else:
        convertedfinal = converted
    return convertedfinal
def baseToDecim(num, base):
    #Converts an integer from a given integer base to base ten
    # initializing substring
    if str(num) == "0":
        return 0
    A = 1
    # create a result list
    result1 = []
    result2 = []
    B = 0
    l = 0
    if str(num).find(".") > -1:
        l =  len(str(num)) - str(num).find(".")-1
        num = str(num).replace(".","")
    for i in range(0, len(num), A):
        #convert to int, after the slicing process
        result1.append(num[i : i + A])
    if str(result1[0])=="-":
        isnegative=1
        result1.remove("-")
    else:
        isnegative=0

    result1.reverse()
    for i in range(0, len(result1), A):
        #Convert from base
        for x in range(0, len(digits), A):
            if result1[i]==digits[x]:
                D=x
                result2.append(D*(base**i))
    for i in range(0, len(result2), A):
        #combines digits
        #B = B + int(result2[i])
        B = B + result2[i]
    B = ((B*((isnegative*2)-1))*-1)/(base**l)
    return B
def baseToBase(num, base1, base2):
    try:
        base1 = int(base1)
        base2 = int(base2)
    except:
        return "base not integer!"
    num = str(num).replace(",","")
    num = str(num).upper()
    if base1 == 1:
        C = len(str(num))
    elif abs(base1) > len(digits):
        if base1 > 0:
            return "maximum base is "+str(len(digits))+"!"
        else:
            return "minimum base is -"+str(len(digits))+"!"
    elif abs(base2) > len(digits):
        if base2 > 0:
            return "maximum base is "+str(len(digits))+"!"
        else:
            return "minimum base is -"+str(len(digits))+"!"
    elif base1 == -1 or base1 == 0 or base2 == -1 or base2 == 0:
        return "invalid base!"
    elif base1 != 10:
        C = baseToDecim(num, base1)
    else:
        C = num
    
    for digit in num:
        if digit not in digits[0:abs(base1)] and digit != ".":
            return "invalid number!"
    if num == "":
        return ""
    if base2 == 1:
        return ("1"*int(float(C)))
    elif base2 != 10:
        finale = baseFromDecim(C, base2)
    else:
        finale = str(C)
    return finale
