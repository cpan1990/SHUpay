n = 600851475143
i = 2
def compute():
    i = 2
    n = 600851475143
    while i * i < n:
        if n % i == 0:
            n = n / i
        i = i + 1

    else:
        return str(n)

if __name__ == "__main__":
	print(compute())

