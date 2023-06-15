def has_unique_characters(data):
    unique_data = set(data)
    return len(data) == len(unique_data)

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
