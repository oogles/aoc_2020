import re

from ..aoc import Puzzle


class P(Puzzle):
    
    input_delimiter = '\n\n'  # individual entries are separated by blank lines
    
    def process_input_item(self, input_item):
        
        data = {}
        for pair in input_item.split():  # split on any whitespace, including newlines
            key, value = pair.split(':')
            data[key] = value
        
        return data
    
    def _part1(self, input_data):
        
        valid_passports = 0
        
        for passport in input_data:
            passport.pop('cid', None)  # ignore country ID
            
            # Cheat and just ensure there are 7 remaining fields, without
            # actually checking what they are
            num_fields = len(passport.keys())
            if num_fields == 7:
                valid_passports += 1
        
        return valid_passports
    
    def _part2(self, input_data):
        
        valid_passports = 0
        
        for passport in input_data:
            byr = int(passport.get('byr', 0))
            if not byr or not 1920 <= byr <= 2002:
                continue
            
            iyr = int(passport.get('iyr', 0))
            if not iyr or not 2010 <= iyr <= 2020:
                continue
            
            eyr = int(passport.get('eyr', 0))
            if not eyr or not 2020 <= eyr <= 2030:
                continue
            
            ecl = passport.get('ecl', None)
            if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                continue
            
            hgt = passport.get('hgt', '')
            hgt_unit = hgt[-2:]
            if hgt_unit == 'cm':
                if not 150 <= int(hgt[:-2]) <= 193:
                    continue
            elif hgt_unit == 'in':
                if not 59 <= int(hgt[:-2]) <= 76:
                    continue
            else:
                continue  # invalid unit
            
            hcl = passport.get('hcl', None)
            if not hcl or not re.match(r'^#[0-9a-f]{6}$', hcl):
                continue
            
            pid = passport.get('pid', None)
            if not pid or not re.match(r'^[0-9]{9}$', pid):
                continue
            
            valid_passports += 1
        
        return valid_passports
