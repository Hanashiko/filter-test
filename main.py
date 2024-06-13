def check_even(number: int) -> int:
    if number % 2 == 0:
        return True
    return False
numbers: list[int] = [1,2,3,4,5,6,7,8,9,10]
print(*list(filter(check_even, numbers)))

def check_5(number: int) -> int:
    if number % 5 == 0:
        return True
    return False
numbers: list[int] = [1,2,3,4,5,6,7,8,9,10]
print(*list(filter(check_5, numbers)))

def filter_vowels(letter: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False
letters = ['c','o','n','n','e','c','t']
print(*list(filter(filter_vowels, letters)))

numbers: list[int] = [1,2,3,4,5,6,7,8,9,10]
print(*list(filter(lambda x: (x % 2 == 0), numbers)))

random_list: list[str] = [1, 'a', 0, False, True, '0']
print(*list(filter(None, random_list)))

ages = [5,12,17,18,24,32]
print(*list(filter(lambda x: x < 18, ages)))
print(*list(filter(lambda x: x >= 18, ages)))

numbers: list[int] = [1,2,3,4,5,6,7,8,9,10]
print(*list(filter(lambda x: x % 3 == 0, numbers)))
