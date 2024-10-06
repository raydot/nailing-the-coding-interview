def longest_unique_substring(s):
  longest = 0
  for i in range(len(s)):
    for j in range(i + 1, len(s)):
      if len(set(s[i:j])) == j - i:
        if j - i > longest:
          longest = j - i
  return longest

someVar = "abbcaabcbb"
print(longest_unique_substring(someVar))
