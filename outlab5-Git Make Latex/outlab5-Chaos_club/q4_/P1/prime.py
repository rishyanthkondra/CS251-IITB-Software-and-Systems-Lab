import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--check-prime", type=int)
    parser.add_argument("--range", nargs=2, type=int)

    args = parser.parse_args()

    if not (args.check_prime or args.range):
        print("Error : At least one of the following arguments are required: --check_prime, --range")
        exit(-1)

    if args.range:
        if args.range[0] < 1 or args.range[1] > 1000:
            print("Error: Please enter a value between 1 and 1000 only")
            exit(-1)

    if args.check_prime:
        if args.check_prime < 1 or args.check_prime > 1000:
            print("Error: Please enter a value between 1 and 1000 only")
            exit(-1)

        if is_prime(args.check_prime):
            print("Yes", end=" ")
        else:
            print("No", end=" ")

    if args.range:
        count = 0
        for i in range(args.range[0], args.range[1]+1):
            if is_prime(i):
                count += 1
        print(count)


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True


if __name__ == '__main__':
    main()
