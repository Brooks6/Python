def get_Cmn(num):
    if num == 1:
        return num * 1 #ending code
    else:
        return num * get_Cmn(num - 1)

m = int(input("enter number M"))
n = int(input("enter number N"))

Cmn = (get_Cmn(m))/((get_Cmn(n)) * get_Cmn(m - n))

print("the result of Cmn is : %d" % Cmn)
