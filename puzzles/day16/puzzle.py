from ..aoc import Puzzle


class P(Puzzle):
    
    input_delimiter = None
    
    def process_input_data(self, input_data):
        
        rule_block, own_ticket_block, nearby_ticket_block = input_data.split('\n\n')
        
        rules = {}
        for r in rule_block.split('\n'):
            rule_name, rule_ranges = r.split(': ')
            rule_ranges = rule_ranges.split(' or ')
            for i, rule_range in enumerate(rule_ranges):
                start, end = rule_range.split('-')
                rule_ranges[i] = (int(start), int(end))
            
            rules[rule_name] = rule_ranges
        
        self.rules = rules
        self.own_ticket = [int(i) for i in own_ticket_block.split('\n')[1].split(',')]
        
        nearby_tickets = []
        for ticket in nearby_ticket_block.split('\n')[1:]:
            nearby_tickets.append([int(i) for i in ticket.split(',')])
        
        return nearby_tickets
    
    def _part1(self, input_data):
        
        rules = self.rules
        error_rate = 0
        
        def is_valid(value):
            
            for rule in rules.values():
                for rule_range in rule:
                    if rule_range[0] <= value <= rule_range[1]:
                        return True
            
            return False
        
        for ticket in input_data:
            for field_value in ticket:
                if not is_valid(field_value):
                    error_rate += field_value
                    break
        
        return error_rate
    
    def _part2(self, input_data):
        
        pass
