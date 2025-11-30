def hanoi(n, source, target, auxiliary, steps):
    if n == 1:
        steps.append(f"Перемістити диск 1 з {source} на {target}")
        return
    hanoi(n - 1, source, auxiliary, target, steps)
    steps.append(f"Перемістити диск {n} з {source} на {target}")
    hanoi(n - 1, auxiliary, target, source, steps)

def main():
    n = int(input("Введіть кількість дисків: "))
    steps = []
    hanoi(n, "A", "C", "B", steps)
    print("\n--- Послідовність переміщень ---")
    for step in steps:
        print(step)
    print(f"\nЗагальна кількість кроків: {len(steps)}")

if __name__ == "__main__":
    main()
