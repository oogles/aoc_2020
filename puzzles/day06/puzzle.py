from ..aoc import Puzzle


class P(Puzzle):
    
    input_delimiter = '\n\n'  # individual entries are separated by blank lines
    
    def process_input_item(self, input_item):
        
        return input_item.split('\n')
    
    def _part1(self, input_data):
        
        total = 0
        for group_answers in input_data:
            combined_answers = ''.join(group_answers)
            total += len(set(combined_answers))
        
        return total
    
    def _part2(self, input_data):
        
        total = 0
        for group_answers in input_data:
            num_people = len(group_answers)
            all_answers = ''.join(group_answers)
            
            for answer in set(all_answers):
                if all_answers.count(answer) == num_people:
                    total += 1
        
        return total
