import day_one
import time


def main():
    t0 = time.time()
    day_one.d1()  # Run d1 function from day_one.py file
    t1 = time.time()
    print(f"TOTAL TIME: {t1-t0}")


if __name__ == "__main__":
    main()
