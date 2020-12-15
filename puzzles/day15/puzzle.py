from ..aoc import Puzzle


class P(Puzzle):
    
    input_delimiter = ','
    
    def process_input_item(self, input_item):
        
        return int(input_item)
    
    def _part1(self, input_data):
        
        # Map each spoken number to the previous turn it was spoken
        history = {n: i for i, n in enumerate(input_data)}
        
        last_number = input_data[-1]
        
        for i in range(len(input_data), 2020):
            last_spoken = history.get(last_number, -1)
            
            # Now that the *previous* time the number was spoken has been
            # pulled from the history, record that it was *last* spoken on
            # the previous turn
            history[last_number] = i - 1
            
            if last_spoken in (-1, i - 1):
                # First time being spoken
                last_number = 0
            else:
                last_number = i - 1 - last_spoken
        
        return last_number
    
    def _part2(self, input_data):
        
        pass
