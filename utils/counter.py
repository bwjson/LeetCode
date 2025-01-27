example_str = "dkaskkkkkkkkkk"
count_str = {}

for char in example_str:
    count_str[char] = count_str.get(char, 0) + 1

print(count_str)