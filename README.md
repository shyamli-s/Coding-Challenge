# Boarding Pass Seat Decoder 

## Program Overview

This Python program decodes a list of boarding passes that have been provided as an input to the program and calculates the unique seat IDs of each boarding pass. It finally provides the highest seat ID and the user’s missing seat ID as an output. 

The seat IDs have been calculated based on a binary space partitioning algorithm, where each half of a boarding pass, i.e the row (first seven values) and the column (last three values), has been converted to binary numbers first. Then, the row and column binary values are converted to their integer (decimal) counterparts individually. The algorithm provided in the problem statement (multiply the row by 8, then add the column) is then used to find the unique seat ID. 

The highest seat ID is obtained as the maximum value in the list of seat IDs calculated in the prior step.

The user’s seat ID, which is the missing value in the list of calculated seat IDs, is obtained by subtracting the calculated set of sorted seat IDs from a set of range of seat IDs (12 to 871) that are present in the aircraft.

## Problem Statement 

In an aircraft, the seating arrangement follows a binary space partitioning algorithm, where the boarding passes provide information about the seat's location. Each boarding pass is a string of characters representing the row and column of the seat. 

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in; The characters 'F' and 'B' indicate the front and back halves of the rows. The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7); Where the characters 'L' and 'R' indicate the left and right halves of the columns. Every seat also has a unique seat ID: multiply the row by 8, then add the column.

It is a completely full flight, so the user’s seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft. Find the highest seat ID on a boarding pass and find the user’s missing seat ID.

## Installation and Usage

This program has been coded using the python 3.11 version, in Jupyter Notebook. This code will work for lower versions of python as well. 

To run this program and obtain the required output, follow these steps:

1. Clone this repository to your local folder:

   ```
   git clone https://github.com/your-username/boarding-pass-seat-decoder.git

2. Change to your local project directory:

   ```
   cd boarding-pass-seat-decoder
   ```

3. Run the script

   ```
   python seat_decoder.py
   ```

Before running the python script “seat_decoder.py”, make sure that your local folder has the “input.txt” file within the same directory as your python file. 

The python script will then display the highest seat ID and the missing seat ID as the output.

## Functions Used in the Program

``` calculate_seat_id(boarding_pass): ```

Calculates the seat ID for each boarding pass and returns a list of all seat IDs.

``` find_highest_seat_id(seat_ids): ```

Finds the highest seat ID from a list of seat IDs.

``` find_missing_seat_id(seat_ids): ```

Finds the user’s missing seat ID from a list of seat IDs.

## Copyright and Licensing

This project is maintained by: Shyamli Suneesh (shyamli.suneesh@gmail.com)
