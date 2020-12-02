from ..aoc import Puzzle


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        policy, password = input_item.split(': ')
        nums, char = policy.split(' ')
        num1, num2 = nums.split('-')
        
        return int(num1), int(num2), char, password
    
    def _part1(self, input_data):
        
        valid_passwords = 0
        
        for char_min, char_max, char, password in input_data:
            char_count = password.count(char)
            if char_min <= char_count <= char_max:
                valid_passwords += 1
        
        return valid_passwords
    
    def _part2(self, input_data):
        
        valid_passwords = 0
        
        for pos1, pos2, char, password in input_data:
            # Check if the character at the two given positions in the password
            # match the target character, accounting for Toboggan Corporate
            # Policies having no concept of "index zero"
            pos1_match = password[pos1 - 1] == char
            pos2_match = password[pos2 - 1] == char
            
            # Use logical XOR to check for passwords with one and only one match
            if pos1_match ^ pos2_match:
                valid_passwords += 1
        
        return valid_passwords
