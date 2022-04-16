def removeKdigits(num: str, k: int) -> str:
    if k >= len(num):
        return 0
    
    smallest = float("inf")
    start, end = 0, k - 1
    
    while end < len(num):
        curr = int(num[:start] + num[end + 1:])
        if curr < smallest:
            smallest = curr
        start += 1
        end += 1
    
    return smallest

print(removeKdigits("1111111111111111111111111111111111111111111111111111111111154q4554666666666666666666666666666666646546546545654654654654654564654654654646545646545645640", 100))