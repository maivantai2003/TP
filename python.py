from typing import List, Typer, Generic
T = TypeVar("T")
def reverse(items: List[T])->List[T]:
    return items[::-1]
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse(numbers)
print(reversed_numbers)

fruits = ['apple', 'banana', 'cherry']
reversed_fruits = reverse(fruits)
print(reversed_fruits)
