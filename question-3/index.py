principal = 75000
lastPrincipal = principal
rate = 0.08

for year in range(6):
    earning = lastPrincipal * rate
    print(str(year+1) + ". year earning is: "+str(earning))
    lastPrincipal += earning
    print("Principal: "+str(lastPrincipal))
    print("===================================")

totalEarning = lastPrincipal - principal

print("Total Earning : "+str(totalEarning))
