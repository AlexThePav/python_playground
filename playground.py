def signFunc(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def arraySign(nums: list[int]) -> int:
    prod = 1
    for num in nums:
        prod = prod * num
    return signFunc(prod)


if __name__ == "__main__":
    nums = [-1,-2,-3,-4,3,2,1]
    print(arraySign(nums))
    
