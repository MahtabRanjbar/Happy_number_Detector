import argparse


def is_happy(n: int) -> bool:
    """Determine if a number is a happy number."""
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


def batch_check(file_path: str):
    """Batch check happy numbers from a file."""
    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return {}
    except ValueError:
        print(f"Error: The file '{file_path}' contains non-integer values.")
        return {}

    results = {number: is_happy(number) for number in numbers}
    return results


def main():
    parser = argparse.ArgumentParser(description="Check if a number (or numbers from a file) are happy numbers.")
    parser.add_argument("-n", "--number", type=int, help="The number to check if it is happy.")
    parser.add_argument("-f", "--file", type=str, help="Path to the file containing numbers to batch check.")
    args = parser.parse_args()

    if args.number is not None:
        # Single number check mode
        if is_happy(args.number):
            print(f"{args.number} is a happy number.")
        else:
            print(f"{args.number} is not a happy number.")
    elif args.file is not None:
        # Batch check mode
        results = batch_check(args.file)
        if results:
            for number, happy in results.items():
                print(f"{number} is {'a happy' if happy else 'not a happy'} number.")
    else:
        print("Error: You must specify either a number with --number or a file path with --file.")
        parser.print_help()


if __name__ == "__main__":
    main()
