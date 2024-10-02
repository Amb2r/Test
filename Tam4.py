a = float(input ("pleas input you firs number"))
b = float(input ("pleas input you second number"))
c = float(input ("pleas input you third number"))
d = float(input ("pleas input you fourth number"))
e = float(input ("pleas input you fifth number"))
Max = 0
Min = 0
if a >= b and a >= c and a >= d and a >= e :
    Max = a
elif b >= a and b >=c and b>=d and b>=e :
    Max=b
elif c>=a and c>=b and c>=d and c>=e :
    Max = c
elif d>=a and b>=b and d>=c and d>=e :
    Max = d
else :
    Max=e

if a <= b and a <= c and a <= d and a <= e  :
    Min = a
elif b <= a and b <=c and b<=d and b<=e :
    Min=b
elif c<=a and c<=b and c<=d and c<=e :
    Min = c
elif d<=a and b<=b and d<=c and d<=e :
    Min = d
else :
    Min = e
    
Avg = (a+b+c+d+e)/5
S = ((Avg-a)*(Avg-a)+(Avg-b)*(Avg-b)+(Avg-c)*(Avg-c)+(Avg-d)*(Avg-d)+(Avg-e)*(Avg-e))/5
print ("Max is = " , Max)
print ("Min is = " , Min)
print ("Average is = " , Avg)
print ("S is = " , S)