def longest_unique_substring(s):
    length_of_longest = 0
    start_index = 0
    longest_start_index = 0
    char_index_map = {}

    for end in range(len(s)):
        char = s[end]
        if char in char_index_map and char_index_map[char] >= start_index:
            start_index = char_index_map[char] + 1
        char_index_map[char] = end
        if end - start_index + 1 > length_of_longest:
            length_of_longest = end - start_index + 1
            longest_start_index = start_index

    return s[longest_start_index:longest_start_index + length_of_longest]

test_var = "abbcaabdcbb"
print(longest_unique_substring(test_var)) 