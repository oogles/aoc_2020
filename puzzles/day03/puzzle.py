from ..aoc import Puzzle


class P(Puzzle):
    
    def count_trees(self, tree_map, move_right, move_down):
        
        map_width = len(tree_map[0])
        map_height = len(tree_map)
        
        x, y = 0, 0
        num_trees = 0
        
        while y < map_height - 1:
            x += move_right
            y += move_down
            
            # The pattern provided by the tree map continues to the right
            # infinitely. Thus the square indicated by the x-coordinate can be
            # found using the modulus of that coordinate with the width of the
            # given map area.
            map_square = tree_map[y][x % map_width]
            
            if map_square == '#':
                num_trees += 1
        
        return num_trees
    
    def _part1(self, input_data):
        
        return self.count_trees(input_data, 3, 1)
    
    def _part2(self, input_data):
        
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        
        product = 1
        for move_right, move_down in slopes:
            product *= self.count_trees(input_data, move_right, move_down)
        
        return product
