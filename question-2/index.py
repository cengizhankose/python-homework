quitProgram = 0
while True:
    print("Enter day count of the vehicle was rented: ")
    rentedDays = input()
    print("Enter the vehicle's odometer reading at the start of the rental period: ")
    startKm = input()
    print("Enter the vehicle's odometer reading at the end of the rental period: ")
    finishKm = input()
    priceForDays = int(rentedDays) * 300
    print("Price for the number of days you rented (300₺/day): "+str(priceForDays))
    priceForKm = (int(finishKm) - int(startKm)) * 2
    print("Price for the km you travelled (2₺/km): "+str(priceForKm))
    totalPrice = priceForDays + priceForKm
    print("Total price: "+str(totalPrice))
    print("Type n to exit program")
    quitProgram = input().lower()
    if quitProgram == "n":
        exit()
