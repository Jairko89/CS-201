import sys

def compute_temperatures(initial_temp):
    temperatures = [initial_temp]
    for i in range(1, 5):
        new_temp = temperatures[-1] + (27 - temperatures[-1]) * 0.2
        temperatures.append(new_temp)
    return temperatures[1:]

def main():
    try:
        # Read the first line of input from stdin, which is expected to be the temperature
        initial_temp = float(input().strip())
        results = compute_temperatures(initial_temp)
        for result in results:
            print(f"{result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
