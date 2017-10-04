#To find simple and compound interest

P=float(input('Enter Pricipal Value:'))
R=float(input('Enter Rate Of Interest:'))
t=int(input('Enter Time(in years):'))
SI=(P*R*t)/100
print("Simple Interest:",SI)
n=int(input('No. of times interest is compounded(per year):')) 
CI=P*(1+R/n)*(n*t)
print("Compund Interest:",CI)
