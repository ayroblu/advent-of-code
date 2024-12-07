from utils.file import read_input

contents = read_input(__file__)
lines = contents.strip().splitlines()


def valid(expected: int, nums: list[int], operators: list[str] = []) -> bool:
    if len(operators) == len(nums) - 1:
        result = nums[0]
        for i, operator in enumerate(operators):
            if operator == "+":
                result += nums[i + 1]
            elif operator == "*":
                result *= nums[i + 1]
        return result == expected
    return valid(expected, nums, operators + ["+"]) or valid(
        expected, nums, operators + ["*"]
    )


total = 0
for line in lines:
    expected, rest = line.split(": ")
    expected = int(expected)
    nums = map(int, rest.split(" "))
    if valid(expected, list(nums)):
        total += expected

print(total)
