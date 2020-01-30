#Presume that you can only drive 8 hours per day. So, if a trip requires 15.25 
#hours, it will require a one-night hotel stay at an additional cost (beyond gas
#and food costs) equal to hotelCostPerNight.

def tripCostAndInfo(distanceKM, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay,
                    lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
    #determine the time (hrs) you need to finish trip by dividing kilo per second by 60 and 1000 to make it kilo per hour then dividing by kilometers  
    time = distanceKM / (vehSpeedMPS * (60 ** 2) / 1000)
    #calculate cost of fuel by calculating liters used then mult by cost of liter
    fuel_cost = gasCostPerLiter * (distanceKM / vehKPL)
    
    
    #calculate days traveled (time / 8) because 8hrs max a day
    days = time / 8
    #create days_rounded for future calculations 
    days_rounded = int(days)    
    #calulate nights in hotel by evaluating if days_str is whole number or not
    days_str = str(days)
    
    
    #if the last to indicies of days_str are '.0'
    if days_str[-2:] == '.0':
        #subtract a day from days and turn to an integer
        total_hotel = int(days - 1)
    else:
        #if not, simply round down using days_rounded
        total_hotel = days_rounded
    #calculate total cost of hotel stays by mult hotel_num and hotelCostPerNight
    hotel_price = total_hotel * hotelCostPerNight
    
    
    #use days str to calculate number of dinners needed for the trip because every day needs a dinnner except for the last
    #if the string of days it takes to get there is a whole number
    if days_str[-2:] == '.0':
        #sub a day
        dinners = int(days_rounded - 1)
    #if it isn't
    else:
        #just round down using days_rounded
        dinners = days_rounded
    #calculate dinner cost
    din_cost = dinners * dinnerCostPerDay
    
    
    #calculate breakfasts by rounding up and subtracting by -1
    if days_str[-2:] == '.0':
        brekfasts = int(days - 1)
    else:
        brekfasts = int(days + 1) - 1
    #calculate breakfasts
    brek_cost = brekfasts * breakfastCostPerDay
    
    #new variable lunch
    lunch = 0    
    #calculate lunches through while loop that finds the total hours of the last day
    while time >= 8:
        #while time is larger or the same as 8 continue to subtract 8 from time's total until it no longer is above or equal to 8
        time -= 8
        #add to lunch
        lunch += 1
    #with new time.. if it is higher than 4
    if time > 4:
        #add to lunch 
        lunch += 1
    #calculate lunch total cost
    lun_cost = lunch * lunchCostPerDay
        
        
    #calculate total cost of trip by tallying up each variable costs (gas, brek, lunch, din, hotel)
    trip_cost = lun_cost + brek_cost + din_cost + hotel_price + fuel_cost
    #calculate total food cost with (brek, lunch, din)
    food_total = lun_cost + brek_cost + din_cost
    
    return round(trip_cost, 2), round(fuel_cost, 2), total_hotel, lunch, round(food_total, 2)
    

def convertMphtoMs(mph):
    '''Convert miles per hour to meters persecond'''
    kmh = mph * 1.609344
    meters_per_hour = kmh * 1000
    #return meters per second after dividing meters per hour by 60 twice... once
    #for minutes then for seconds
    return (meters_per_hour / (60 ** 2))
    
def convertMpgtoLKm(mpg):
    return mpg * 1.609344 / 3.785411784
    
def compareVehiclesForTrip(distanceM, veh1Name, veh1SpeedMPH, veh1MPG, veh2Name, veh2SpeedMPH, veh2MPG, gasCostPerGallon, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
    '''Convert useful info from miles and gallons to km and liters to pass into tripCostAndInfo. use that information to derive a comparison between the two cars'''
    #convert distanceM (miles to km) given 1 mile == 1.60934 kms
    km = distanceM * 1.609344
    #convert miles pergallon to km per liter of each car
    car1_KmL = convertMpgtoLKm(veh1MPG)
    car2_KmL = convertMpgtoLKm(veh2MPG)
    #convert speed mph to kmh
    car1_ms = convertMphtoMs(veh1SpeedMPH)
    car2_ms = convertMphtoMs(veh2SpeedMPH)
    
    #convert gas cost from gallon to L
    gasCostPerL = gasCostPerGallon / 3.785411784
    
    #first car
    total1, gas1, hotel_nights1, lunches1, food1 = tripCostAndInfo(km, car1_ms,
    #### variables above!####                                                               
    car1_KmL, gasCostPerL, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight)
    
    #second car
    total2, gas2, hotel_nights2, lunches2, food2 = tripCostAndInfo(km, car2_ms,
    #### variables above!####                                                               
    car2_KmL, gasCostPerL, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight)    
    
    print(f"{distanceM} miles in vehicle '{veh1Name}' will cost ${total1}, including:\n${round((hotel_nights1 * hotelCostPerNight), 2)} for {hotel_nights1} hotel night(s), ${gas1} for gas, ${food1} for food (including {lunches1} lunch)") 
    
    print(f"{distanceM} miles in vehicle '{veh2Name}' will cost ${total2}, including:\n${round((hotel_nights2 * hotelCostPerNight), 2)} for {hotel_nights2} hotel night(s), ${gas2} for gas, ${food2} for food (including {lunches2} lunch)") 
    
def testQ1():
    '''make at least five calls to tripCostAndInfo with different arguments'''
    a,b,c,d,e = tripCostAndInfo(1000.0, 33.33, 9.408, 3.0, 5.0, 7.0, 8.0, 20.0)
    print('Call 1:', a,b,c,d,e)
    a,b,c,d,e = tripCostAndInfo(1050.0, 34.33, 9.408, 4.0, 5.0, 7.0, 8.0, 20.0)
    print('Call 2', a,b,c,d,e)
    a,b,c,d,e = tripCostAndInfo(2000.0, 33.33, 9.408, 3.0, 5.0, 7.0, 8.0, 20.0)
    print('Call 3',a,b,c,d,e)
    a,b,c,d,e = tripCostAndInfo(1000.0, 33.33, 10.4, 3.0, 5.0, 7.0, 8.0, 60.5)
    print('Call 4', a,b,c,d,e)
    a,b,c,d,e = tripCostAndInfo(1000.0, 32.33, 9.408, 2.0, 4.0, 7.0, 8.0, 27.0)
    print('Call 5', a,b,c,d,e)    
    
def testQ2():
    '''make at least five calls to compareVehiclesForTrip with different arguments'''
    (compareVehiclesForTrip(1000, 'ford', 45.0, 30.0, 'chevy', 60.0, 25.0, 3.0, 4.0, 5.0, 7.0, 25.0))
    (compareVehiclesForTrip(1000, 'chevy', 75.0, 35.0, 'tesla', 100.0, 1.0, 4.0, 4.0, 5.0, 7.0, 30.0))
    (compareVehiclesForTrip(1000, 'ford', 45.0, 30.0, 'chevy', 60.0, 25.0, 3.0, 4.0, 5.0, 7.0, 25.0))
    (compareVehiclesForTrip(1000, 'honda', 64.0, 40.0, 'toyota', 77.0, 44.0, 3.0, 4.0, 8.0, 7.0, 25.0))
    (compareVehiclesForTrip(1000, 'audi', 120.0, 25.0, 'bmw', 110.0, 25.0, 3.0, 4.0, 8.0, 7.0, 45.0))