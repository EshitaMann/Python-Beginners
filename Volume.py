#Volume of sphere,cone and cylinder

PI=3.14
r=float(input('Enter radius:'))
h=float(input('Enter height:'))
S=(4*PI*(pow(r,3)))/3
Cone=(PI*h*(pow(r,2)))/3
Cy=PI*h*(pow(r,2))
print("Sphere Vol.=",S)
print("Cone Vol.=",Cone)
print("Cylinder Vol.",Cy)
