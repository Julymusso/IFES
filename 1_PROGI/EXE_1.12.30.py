A=0
while A<6.3:
    rad=A*180/3.1415
    senA=rad-(rad**3/6)+(rad**5/120)-(rad**7/5040)
    print("Sen{:.1f}".format(A),"...... {:.3f}".format(senA))
    A=A+0.1
