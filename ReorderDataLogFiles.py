# Approach:
# 1. Separate the logs into two categories: letter-logs and digit-logs.
# 2. Letter-logs should be sorted lexicographically by content. If two logs have the same content, sort them by identifier.
# 3. Digit-logs should maintain their relative ordering.
# 4. Concatenate sorted letter-logs with unchanged digit-logs and return the result.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Step 1: Define sorting logic
        def get_sort_key(log):
            identifier, content = log.split(" ", 1)  # Split the log into identifier and content
            return (content, identifier)  # Sort letter-logs by content first, then by identifier
        
        # Step 2: Separate logs into letter-logs and digit-logs
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            if log.split()[1].isdigit():  # Check if the second element is a digit
                digit_logs.append(log)  # Store digit-logs separately
            else:
                letter_logs.append(log)  # Store letter-logs separately
        
        # Step 3: Sort letter-logs based on content and identifier
        letter_logs.sort(key=get_sort_key)
        
        # Step 4: Maintain relative order of digit-logs and concatenate results
        return letter_logs + digit_logs

# Time Complexity: O(M log M), where M is the number of letter-logs.
# - We iterate through all logs once (O(N)).
# - Sorting letter-logs takes O(M log M), where M is the number of letter-logs.
# - Since digit-logs remain in order, their processing is O(N).
# - Overall complexity is O(N + M log M), which simplifies to O(M log M).

# Space Complexity: O(N), where N is the total number of logs.
# - We store letter-logs and digit-logs separately, resulting in O(N) space usage.
