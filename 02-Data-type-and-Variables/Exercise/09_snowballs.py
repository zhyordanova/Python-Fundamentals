import sys
n = int(input())

max_snowball_value = - sys.maxsize
c_snowball_snow = None
c_snowball_time = None
c_snowball_quality = None

for ball in range(1, n + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow // snowball_time) ** snowball_quality

    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        c_snowball_snow = snowball_snow
        c_snowball_time = snowball_time
        c_snowball_quality = snowball_quality

print(f'{c_snowball_snow} : {c_snowball_time} = {max_snowball_value} ({c_snowball_quality})')
