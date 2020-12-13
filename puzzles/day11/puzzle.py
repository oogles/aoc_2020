from copy import deepcopy

from ..aoc import Puzzle


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        # Convert the string to a list to support item assignment
        return list(input_item)
    
    def _part1(self, input_data):
        
        # Take an initial deep copy so changes don't affect part 2
        layout = deepcopy(input_data)
        
        # Snapshot the initial state of the seating layout. This is used to
        # both lookup adjacent seats during each round (so decisions are not
        # based on seats already processed in that round) and to compare to the
        # results at the end of the round (to detect if any changes were made).
        initial_state = deepcopy(layout)
        
        # Get the index of the right-most seating position
        rightmost_seat_index = len(layout[0]) - 1
        
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
                        layout[i][j] = '#'
                    elif occupied_adjacent_seats >= 4:
                        layout[i][j] = 'L'
            
            if layout == initial_state:
                break
            
            # Snapshot the state for the next round
            initial_state = deepcopy(layout)
        
        # Count the number of occupied seats
        return sum([r.count('#') for r in layout])
    
    def _part2(self, input_data):
        
        # Snapshot the initial state of the seating layout. This is used to
        # both lookup adjacent seats during each round (so decisions are not
        # based on seats already processed in that round) and to compare to the
        # results at the end of the round (to detect if any changes were made).
        initial_state = deepcopy(input_data)
        
        # Get the index of the right-most seating position
        rightmost_seat_index = len(input_data[0]) - 1
        
        def look_up(layout, row, col, distance, seen_seats):
            
            prev_row = row - distance
            if prev_row < 0:  # in the first row
                return seen_seats
            
            prev_row = layout[prev_row]
            keep_looking = False
            
            if not seen_seats[0]:
                # No seat in the upper left direction has been seen
                left = col - distance
                if left < 0:
                    # Can't look any further left
                    seen_seats[0] = '-'
                elif prev_row[left] != '.':
                    seen_seats[0] = prev_row[left]
                else:
                    keep_looking = True
            
            if not seen_seats[1]:
                # No seat directly upward has been seen
                if prev_row[col] != '.':
                    seen_seats[1] = prev_row[col]
                else:
                    keep_looking = True
            
            if not seen_seats[2]:
                # No seat in the upper left direction has been seen
                right = col + distance
                if right > rightmost_seat_index:
                    # Can't look any further right
                    seen_seats[2] = '-'
                elif prev_row[right] != '.':
                    seen_seats[2] = prev_row[right]
                else:
                    keep_looking = True
            
            if keep_looking:
                look_up(layout, row, col, distance + 1, seen_seats)
            
            return seen_seats
        
        def look_down(layout, row, col, distance, seen_seats):
            
            try:
                next_row = layout[row + distance]
            except IndexError:  # in the last row
                return seen_seats
            
            keep_looking = False
            
            if not seen_seats[0]:
                # No seat in the upper left direction has been seen
                left = col - distance
                if left < 0:
                    # Can't look any further left
                    seen_seats[0] = '-'
                elif next_row[left] != '.':
                    seen_seats[0] = next_row[left]
                else:
                    keep_looking = True
            
            if not seen_seats[1]:
                # No seat directly upward has been seen
                if next_row[col] != '.':
                    seen_seats[1] = next_row[col]
                else:
                    keep_looking = True
            
            if not seen_seats[2]:
                # No seat in the upper left direction has been seen
                right = col + distance
                if right > rightmost_seat_index:
                    # Can't look any further right
                    seen_seats[2] = '-'
                elif next_row[right] != '.':
                    seen_seats[2] = next_row[right]
                else:
                    keep_looking = True
            
            if keep_looking:
                look_down(layout, row, col, distance + 1, seen_seats)
            
            return seen_seats
        
        while True:
            for i, row in enumerate(initial_state):
                for j, seat in enumerate(row):
                    if seat == '.':  # not a seat at all!
                        continue
                    
                    # Look to the left
                    left_seat = None
                    k = j - 1
                    while k >= 0:
                        if row[k] != '.':
                            left_seat = row[k]
                            break
                        
                        k -= 1
                    
                    # Look to the right
                    right_seat = None
                    k = j + 1
                    while k <= rightmost_seat_index:
                        if row[k] != '.':
                            right_seat = row[k]
                            break
                        
                        k += 1
                    
                    # Look up and down
                    upper_seats = look_up(initial_state, i, j, 1, [None, None, None])
                    lower_seats = look_down(initial_state, i, j, 1, [None, None, None])
                    
                    occupied_seats = 0
                    if left_seat == '#':
                        occupied_seats += 1
                    if right_seat == '#':
                        occupied_seats += 1
                    
                    occupied_seats += upper_seats.count('#')
                    occupied_seats += lower_seats.count('#')
                    
                    if occupied_seats == 0:
                        input_data[i][j] = '#'
                    elif occupied_seats >= 5:
                        input_data[i][j] = 'L'
            
            if input_data == initial_state:
                break
            
            # Snapshot the state for the next round
            initial_state = deepcopy(input_data)
        
        # Count the number of occupied seats
        return sum([r.count('#') for r in input_data])
