class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: If there are no digits, return an empty list immediately
        if not digits:
            return []

        # Step 1: Create a dictionary to map each phone number to its letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []

        def backtracking(index, current_string):
            # 1. Goal: We have picked a letter for every single digit
            if index == len(digits):
                result.append(current_string)
                return

            # Get the letters associated with the current digit (e.g., "3" -> "def")
            current_digit = digits[index]
            letters = phone_map[current_digit]

            # 2. Choices: Loop through every available letter for this specific digit
            for letter in letters:
                # 3. Recurse: Move to the next digit (index + 1)
                # 4. Cleanse: Done automatically because strings are cloned on addition!
                backtracking(index + 1, current_string + letter)

        # Start at the first digit (index 0) with an empty string string
        backtracking(0, "")
        return result
