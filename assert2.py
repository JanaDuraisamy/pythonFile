def average(number):
    assert len(number) > 0, "list numbers should not be empty"
    assert all(isinstance(num, int) for num in number), "all elements should be only integer"
    total = sum(number)
    average = total/len(number)
    return average
result = average([5, 10, 15, 20, 25])
print(result)
result = average([112,110])
print(result)
result = average([1, 2, 3,"four"])
print(result)
