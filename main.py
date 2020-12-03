import day_one
import day_two
import time


def main():
    t0 = time.time()
    #day_one.d1()  # Run d1 function from day_one.py file
    day_two.d2()  # Run d2 function from day_two.py file
    day_two.d2b()  # Run d2b function from day_two.py file
    t1 = time.time()
    #print(f"TOTAL TIME: {t1-t0}")


if __name__ == "__main__":
    main()
