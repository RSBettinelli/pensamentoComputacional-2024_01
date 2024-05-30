#somaPares_RafaelSB2024_05_27.py
#if the sum of two numbers from a LIST return the INT = TRUE 
#if any sum of two numbers from a LIST return the INT = FALSE

def sum_pairs(numbers: list, target: int) -> bool:
    for num in numbers:
        for num2 in numbers:
            test = num2 + num
            if test == target:
                return True

    return False


print(sum_pairs([1, 2], 4))  # True 
print(sum_pairs([8], 1))  # False 
print(sum_pairs([8], 10))  # False 
print(sum_pairs([3, 4, 6], 9))  # True
print(sum_pairs([3, 4, 6], 7))  # True
