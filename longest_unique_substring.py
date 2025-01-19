def longest_substring_without_repeating(s):
    if not s:
        return ""

    start = 0  # Start index of the current substring
    max_length = 0  # Length of the longest substring without repeating characters
    char_index_map = {}  # Dictionary to store the last index of each character

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            # If the character is repeated and its last occurrence is after the start index
            start = char_index_map[s[end]] + 1

        char_index_map[s[end]] = end  # Update the last index of the character
        current_length = end - start + 1

        if current_length > max_length:
            max_length = current_length

    return s[start:start + max_length]

# Example usage:
input_string = "iaminvincibleandnooneisabovemeratherweallmovesidebyside"
print(longest_substring_without_repeating(input_string))
