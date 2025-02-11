class Solution:
    def myAtoi(self, s: str) -> int:
        # Approach:
        # 1. Trim leading whitespaces.
        # 2. Determine the sign of the number.
        # 3. Read digits until a non-digit character is encountered.
        # 4. Convert the extracted digits into an integer.
        # 5. Clamp the integer within the 32-bit signed integer range [-2^31, 2^31 - 1].
        # 6. Return the final integer.

        # Constants for 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Trim leading whitespaces
        s = s.lstrip()
        if not s:
            return 0  # If empty after stripping, return 0

        # Step 2: Determine the sign
        sign = 1  # Default is positive
        index = 0  # Pointer to traverse the string
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        # Step 3: Read digits and build the number
        num = 0
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])  # Convert char to int and build number
            index += 1

        # Step 4: Apply the sign
        num *= sign

        # Step 5: Clamp within the 32-bit integer range
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        # Step 6: Return the final integer
        return num

# Time Complexity: O(N), where N is the length of the input string.
# - We traverse the string once to process it, leading to linear complexity.

# Space Complexity: O(1), since we use only a few extra variables.