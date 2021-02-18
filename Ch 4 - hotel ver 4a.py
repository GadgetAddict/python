 # Michael King -  HOTEL Occupancy Calculations - PYTHON 3


def occupancyRateCalc(occupiedRooms, roomCount):
	return occupiedRooms / roomCount

def validateInput(prompt,maxRooms = None):
    while True:

        try:
            user_input = int(input(prompt))

             # use this for total floors and rooms per floor
            while maxRooms is None and user_input > 0:
                return user_input
            #else:
            #    print("\nTry Again. Number should be greater than zero.\n")

            while maxRooms is not None:
                #print("TEST MODE Max Rooms not none")
                while user_input <= maxRooms and user_input >= 0:
                    return user_input
                else:
                    raise Exception
                
                
        except ValueError:
            print("\nTry again. Please enter numbers only.\n")
        except Exception:
            print(f"\nTry again. Please enter a number between 0 and {(maxRooms)}.\n")
   
print("Calculate Hotel Occupancy\nLet's Begin\n")			
totalFloors = validateInput("Enter Number of Hotel Floors\n")

totalRoomCount_List = []
occupiedRoomCount_List = []


for floor in range(1,totalFloors+1):
	if floor == 13:
		print(f"** Attention: There are no rooms on Floor {floor}\n")
		# Add Zero to the  2 lists so that the list contains the same amount of elements as hotel floors
		totalRoomCount_List.append(0)
		occupiedRoomCount_List.append(0)
		continue     #takes you back to the top of the loop

	#enter number of rooms:
	totalRoomCount_List.append(validateInput(f"How many rooms on Floor {floor}?\n"))
	occupiedRoomCount_List.append(validateInput(f"How many rooms are occupied on Floor {floor}?\n", totalRoomCount_List[floor-1]))
	
	# Get Occupancy rate
	occupancyRate = occupancyRateCalc(occupiedRoomCount_List[floor-1], totalRoomCount_List[floor-1])
	print(f"Floor {floor}: {totalRoomCount_List[floor-1]} Rooms, {occupiedRoomCount_List[floor-1]} occupied.")
	print(f"The the Occupancy rate for Floor {floor} is {occupancyRate:.2f}\n")
	
#Calculate Totals by adding up all the numbers in the lists
totalHotelRooms = 0
totalOccupied = 0

# add all room counts from list together 
for rooms in totalRoomCount_List:
	totalHotelRooms += rooms
	
# add all occupied counts from list together 
for occupied in occupiedRoomCount_List:
	totalOccupied += occupied

# Get total hotel vacancies 	
totalVacancies = totalHotelRooms - totalOccupied

# Get Total Hotel Occupancy Rate
totalHotelOccupancy = occupancyRateCalc(totalOccupied, totalHotelRooms)

print(f"Altogether, the Hotel has {totalHotelRooms} Rooms, {totalOccupied} rooms are occupied, {totalVacancies} rooms are vacant.")
print(f"The overall occupancy rate for The Hotel is {totalHotelOccupancy:.2f}.")



	
