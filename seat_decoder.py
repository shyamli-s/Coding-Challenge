"""
Created by Shyamli Suneesh
14.07.2023
"""


boarding_passes = [] #create an empty list of boarding passes

with open('input.txt') as file: #read the input.txt file into this program line by line
    bp = file.readlines()
for b in bp:
    boarding_passes.append(b.replace('\n', '')) #append each boarding pass to this list by removing the blank \n character at the end 

# =============================================================================

def calculate_seat_id(boarding_pass): #function to calculate the seat IDs
    row_binary = boarding_pass[:7].replace('F', '0').replace('B', '1')  # Convert row characters 'F' and 'B' to binary digits
    col_binary = boarding_pass[7:].replace('L', '0').replace('R', '1')  # Convert column characters 'R' and 'L' to binary digits

    row = int(row_binary, 2)  # Convert binary row representation to decimal (Applying Binary Space Partitioning)
    col = int(col_binary, 2)  # Convert binary column representation to decimal (Applying Binary Space Partitioning)

    seat_id = row * 8 + col  # Calculate the seat ID
    return seat_id

def find_highest_seat_id(seat_ids): #function to calculate the highest seat ID
    highest_seat_id = max(seat_ids)
    return highest_seat_id

def find_missing_seat_id(seat_ids): #function to find the missing seat ID
    seat_ids.sort()
    all_seats = set(range(min(seat_ids), max(seat_ids) + 1))
    missing_seat_id = list(all_seats - set(seat_ids))[0]
    return missing_seat_id

# =============================================================================

seat_ids = [calculate_seat_id(bp) for bp in boarding_passes] # variable to store the list of seat IDs 
highest_seat_id = find_highest_seat_id(seat_ids) # variable to store the highest seat ID 
missing_seat_id = find_missing_seat_id(seat_ids) # variable to store the missing seat ID 

print(f"The Highest Seat ID is: {highest_seat_id} and My Seat ID is: {missing_seat_id}")

# =============================================================================