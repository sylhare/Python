t = int(input().strip())

for _ in range(t):
    input_number = int(input().strip())
    result = 0

    # Basic
    for i in range(input_number):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    # Generator
    def find(number):
        for j in range(number):
            yield j * (j % 3 == 0 or j % 5 == 0)

    print(sum(find(input_number)))

    # One line
    sum([i * (i % 3 == 0 or i % 5 == 0) for i in range(input_number)])

    # Maths
    def sum_modulo(n, k):
        n = (n - 1) // k
        return k * n * (n + 1) // 2


    print(sum_modulo(input_number, 3) + sum_modulo(input_number, 5) - sum_modulo(input_number, 15))
