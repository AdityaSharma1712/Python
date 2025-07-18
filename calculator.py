# Input total bottles and bottles per day
total_bottles = int(input("Enter total water bottles: "))
bottles_per_day = int(input("Enter bottles you drink per day: "))

day = 1

while total_bottles > 0:
    print(f"Day {day}:", end=' ')
    if total_bottles >= bottles_per_day:
        total_bottles -= bottles_per_day
        print(f"Drank {bottles_per_day} bottles. {total_bottles} left.")
    else:
        print(f"Drank {total_bottles} bottle(s). 0 left.")
        total_bottles = 0
    day += 1

if total_bottles == 0:
    print("No more bottles left.")