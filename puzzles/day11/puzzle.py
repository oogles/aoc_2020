from copy import deepcopy

from ..aoc import Puzzle


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        # Conver the string to a list to support item assignment
        return list(input_item)
    
    def _part1(self, input_data):
        
        # Snapshot the initial state of the seating layout. This is used to
        # both lookup adjacent seats during each round (so decisions are not
        # based on seats already processed in that round) and to compare to the
        # results at the end of the round (to detect if any changes were made).
        initial_state = deepcopy(input_data)
        
        # Get the index of the right-most seating position
        rightmost_seat_index = len(input_data[0]) - 1
        
        while True:
            for i, row in enumerate(initial_state):
                prev_row = i - 1
                if prev_row >= 0:
                    prev_row = initial_state[prev_row]
                else:  # in the first row
                    prev_row = None
                
                try:
                    next_row = initial_state[i + 1]
                except IndexError:  # in the last row
                    next_row = None
                
                for j, seat in enumerate(row):
                    if seat == '.':  # not a seat at all!
                        continue
                    
                    prev_seat = max(0, j - 1)  # account for being in left-most seat
                    next_seat = min(rightmost_seat_index, j + 1)  # account for being in right-most seat
                    
                    occupied_adjacent_seats = 0
                    if prev_seat != j and row[prev_seat] == '#':
                        occupied_adjacent_seats += 1
                    if next_seat != j and row[next_seat] == '#':
                        occupied_adjacent_seats += 1
                    if prev_row:
                        occupied_adjacent_seats += prev_row[prev_seat:next_seat + 1].count('#')
                    if next_row:
                        occupied_adjacent_seats += next_row[prev_seat:next_seat + 1].count('#')
                    
                    if occupied_adjacent_seats == 0:
                        input_data[i][j] = '#'
                    elif occupied_adjacent_seats >= 4:
                        input_data[i][j] = 'L'
            
            if input_data == initial_state:
                break
            
            # Snapshot the state for the next round
            initial_state = deepcopy(input_data)
        
        # Count the number of occupied seats
        return sum([r.count('#') for r in input_data])
    
    def _part2(self, input_data):
        
        pass
