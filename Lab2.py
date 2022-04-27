def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    ave_temp = calc_average_temperature(num_list)
    max_min_list = calc_min_max_temperature(num_list)
    print(num_list)
    print(ave_temp)
    print(max_min_list)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g.5,67,32)")

def get_user_input():
    numberarray = input()
    numberarray = numberarray.split(",")
    numberarray = [float(i) for i in numberarray]
    return numberarray

def calc_average_temperature(numberarray):
    count = 0
    totalnumber = 0

    for i in numberarray:
        count = count + 1

    for i in numberarray:
        totalnumber = totalnumber + i

    averagetemp = totalnumber/count
    return averagetemp

def calc_min_max_temperature(numberarray):
    i = 0
    max = 0

    for i in numberarray:
        if i>max:
            max = i

    min = max

    for i in numberarray:
        if i<min:
            min = i

    maxminlist = [max,min]

    return maxminlist







if __name__ == "__main__":
    main()