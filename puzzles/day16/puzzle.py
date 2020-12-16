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
        
        rules = self.rules
        
        def find_matching_fields(value):
            
            matches = []
            
            for rule_name, rule_ranges in rules.items():
                for rule_range in rule_ranges:
                    if rule_range[0] <= value <= rule_range[1]:
                        matches.append(rule_name)
            
            return matches
        
        # All field positions start corresponding to potentially any field
        rule_names = set(rules.keys())
        field_possibilities = {i: rule_names.copy() for i in range(len(rules))}
        
        # Narrow each position down to a subset of possible fields using nearby tickets
        for ticket in input_data:
            ticket_fields = {}
            
            for i, field_value in enumerate(ticket):
                matching_fields = find_matching_fields(field_value)
                if not matching_fields:
                    break
                else:
                    ticket_fields[i] = matching_fields
            else:
                # All fields in the ticket were valid
                for i, fields in ticket_fields.items():
                    field_possibilities[i] = field_possibilities[i].intersection(fields)
        
        # Finally, use the confirmed fields (where there is only a single
        # possibility) to clarify any remaining unconfirmed fields
        known_fields = {}
        while field_possibilities:
            for i, fields in field_possibilities.copy().items():
                fields = fields.difference(known_fields.values())
                if len(fields) == 1:
                    known_fields[i] = fields.pop()
                    del field_possibilities[i]
        
        # Multiply together "departure*" fields from own ticket
        result = 1
        for i, field in known_fields.items():
            if field.startswith('departure'):
                result *= self.own_ticket[i]
        
        return result
