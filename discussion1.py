def printTimeAndCostOfTrip(distanceInKilometers, speedInKPH, KmPerLiter, gasCostPerLiter):
    #calculate time required in hours 
    hours = distanceInKilometers / speedInKPH
    #calculate liters of gass needed
    liters_need = distanceInKilometers / KmPerLiter
    #calculate gas cost 
    gas_cost = round(liters_need * gasCostPerLiter, 2)
    
    print(f"Time needed for trip: {hours} hours.")
    print(f"Gas cost for the trip: ${gas_cost}")
    
          