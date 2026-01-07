def main():
    while True:
        user_data = user_input()
        number, unit = user_data
        unit = unit.lower()
        if unit =="c":
            result = c_to_f(number)
            print(f"{number}°C -> {result:.2f}°F")
        elif unit == "f":
            result = f_to_c(number)
            print(f"{number}°F -> {result:.2f}°C")
        else:
            print("Invalid unit! Use C or F only.")
            continue

        again = input("\nConvert Another? (y/n): ").lower()
        if again != 'y':
            print("Exiting...")
            break

def user_input():
    while True:
        user_in = input("Enter Temperature: ").strip().upper()
        if not user_in:
            print("Input Can't be empty!!!")
            continue
        number_str = ""
        unit_str = ""
        for char in user_in:
            if char.isdigit() or char == ".":
                number_str += char
            else:
                unit_str += char


        try:
            number = float(number_str)
        except ValueError:
            print("Temperature Must be a number!!!")
            continue
        unit = unit_str
        return number,unit
    

def c_to_f(c):
    return c *(9/5) + 32

def f_to_c(f):
    return (f -32) * 5/9


if __name__ == "__main__":
    main()