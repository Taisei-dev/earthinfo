height=int(input("Height(cm)?:"))
weight=int(input("Weight(kg)?:"))
bmi=weight/((height/100)**2)
print("痩せ" if bmi<18.5 else "普通" if bmi<25 else "肥満(1)" if bmi<30 else "肥満(2)" if bmi<35 else "肥満(3)" if bmi<40 else "肥満(4)")
