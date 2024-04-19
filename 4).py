def sort_by_length(strings):
    ascending = sorted(strings, key=len)
    descending = sorted(strings, key=len, reverse=True)
    return ascending, descending

strings = ["apple", "banana", "orange", "kiwi", "pear", "grapefruit"]
ascending_order, descending_order = sort_by_length(strings)

print("По возрастанию длины:")
print(ascending_order)

print("\nПо убыванию длины:")
print(descending_order)