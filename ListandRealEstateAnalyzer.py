def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("enter a positive >0 .")
            else:
                return value
        except ValueError:
            print("enter a number >0.")

def getMedian(data):
    data.sort()
    list_length = len(data)
    if list_length % 2 == 0:
        mid1 = data[list_length // 2 - 1]
        mid2 = data[list_length // 2]
        median = (mid1 + mid2) / 2
    else:
        median = data[list_length // 2]
    return median

def calculate():
    sales_values = []
    while True:
        sales_price = getFloatInput("Enter the sales price: ")
        sales_values.append(sales_price)

        while True:
            continue_loop = input("Enter another value (Y/N)? ").upper()
            if continue_loop in ('Y', 'N'):
                break
            else:
                print("enter Y or N.")

        if continue_loop == 'N':
            break

    sales_values.sort()
    print("Sorted Sales Values:")
    for value in sales_values:
        print(f"${value:.2f}")

    minimum = min(sales_values)
    maximum = max(sales_values)
    total = sum(sales_values)
    average = total / len(sales_values)
    median = getMedian(sales_values)
    commission = total * 0.03

    print(f"Minimum Value: ${minimum:.2f}")
    print(f"Maximum Value: ${maximum:.2f}")
    print(f"Total Value: ${total:.2f}")
    print(f"Average Value: ${average:.2f}")
    print(f"Median Value: ${median:.2f}")
    print(f"Commission: ${commission:.2f}")

if __name__ == "__main__":
    calculate()
