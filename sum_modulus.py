#!/usr/bin/env python3
# Created By: Kent Gatera
# Created: Nov 13, 2022
# This program adds several numbers together using a modulus.


def main():

    try:
        max_num_Range = int(input("What is the range from 0?: "))
        new_int = 0
        loop_count = 0

        # Main loop
        while True:
            old_int = 0
            # This section retrieves all the number from 0-user wished number
            # That is divisible by 3 or 5 and adds it
            for i in range(0, max_num_Range, 1):
                if (i % 3 == 0) or (i % 5 == 0):
                    new_int += i
                    print(f"{i}+{old_int} = {new_int}")
                    loop_count += 1
                    old_int = new_int

            # The program breaks and goes on forever if the break number is not odd.
            if i == (max_num_Range - 1):
                break
    except:
        print(f"Your input is not a number. (e.g 50)")


# Running the program
if __name__ == "__main__":
    main()
