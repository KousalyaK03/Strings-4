# Enum to represent API responses
class Response(Enum):
    HOTTER = 1   # Moving closer to the target
    COLDER = 2   # Moving farther from the target
    SAME = 3     # Same distance from the target
    EXACT = 4    # Reached the destination

# Approach:
# 1. Start from a random position on the grid.
# 2. Use the getResponse API to determine if the new position is closer (HOTTER) or farther (COLDER).
# 3. Move in different directions (up, down, left, right) based on responses.
# 4. Continue exploring until the API returns EXACT, indicating the target is found.
# 5. Use a controlled search strategy (like binary search-inspired movement) to minimize API calls.

class FindTarget:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.target = self.find_target_position()  # For simulation only

    def find_target_position(self):
        # Find the target object's coordinates (for internal simulation only)
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 'x':
                    return (r, c)
        return None

    def getResponse(self, row, col):
        # Simulated getResponse function (in real use, this would be a black-box API)
        if (row, col) == self.target:
            return Response.EXACT
        old_dist = self.manhattan_distance(self.prev_pos, self.target)
        new_dist = self.manhattan_distance((row, col), self.target)

        if new_dist < old_dist:
            return Response.HOTTER
        elif new_dist > old_dist:
            return Response.COLDER
        else:
            return Response.SAME

    def manhattan_distance(self, p1, p2):
        # Calculate Manhattan distance
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def find_object(self):
        # Start from a random position
        row, col = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
        self.prev_pos = (row, col)  # Store previous position
        response = self.getResponse(row, col)

        if response == Response.EXACT:
            return [row, col]

        # Try moving in different directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                new_response = self.getResponse(new_row, new_col)
                if new_response == Response.EXACT:
                    return [new_row, new_col]
                elif new_response == Response.HOTTER:
                    self.prev_pos = (new_row, new_col)
                    return self.find_object()  # Recursively continue searching

        return []

# Time Complexity: O(N * M) in the worst case, but typically much better using directional hints.
# Space Complexity: O(1), since we are using only a few extra variables.
