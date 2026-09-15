def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"



def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone
    # of this age
    if 0< age <5:
        return 0
    elif 5<=age<=12:
        return 8
    elif 13<=age<=64:
        return  15
    elif age >= 65:
        return 10
    else:
        return f"{age} is not a valid age."



def sum_multiples(limit):
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    sum = 0
    for i in (range(limit)):
        if ((i % 3 == 0) or (i%5 == 0)):
            sum += i
    return sum


def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    sum = 0
    for i in (numbers):
        if i >0:
            sum += i
    return sum

def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    print(seconds_to_hms(3661))            # 1:01:01
    print(admission_price(10))             # 8
    print(sum_multiples(10))               # 23
    print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()
