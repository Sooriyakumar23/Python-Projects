Name = list(input()) #"sooriyakumar"
def Numeric(Name):
    #Name = list(Name)
    numeric = 0
    for i in Name:
        #print (ord(i)-96)
        numeric += (ord(i)-96)
    return (numeric)
numeric=(Numeric(Name))%9
print "Your calculated numerology is " + str(numeric)
