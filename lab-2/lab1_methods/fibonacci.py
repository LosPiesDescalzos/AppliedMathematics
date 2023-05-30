def fibonacci(function, left, right, eps):
    eps = float(eps)
    fib_nums = [0, 1]
    last_number = 1
    n = 2
    while last_number < (right - left) / eps:
        fib_nums.append(last_number)
        n += 1
        last_number = fib_nums[n - 1] + fib_nums[n - 2]
    fib_nums.append(last_number)
    n += 1
    a = left
    b = right

    d = eps / 2

    x1 = a + fib_nums[n - 3] / fib_nums[n - 1] * (b - a)
    x2 = a + fib_nums[n - 2] / fib_nums[n - 1] * (b - a)

    first_value = function(x1)
    second_value = function(x2)

    k = 1
    while k != n:
        if first_value > second_value:
            a = x1
            x1 = x2
            x2 = a + fib_nums[n - 2 - k] / fib_nums[n - k - 1] * (b - a)
            first_value = second_value
            second_value = function(x2)

            if k == n - 3:
                x2 = x1 + d
                first_value = function(x1)
                second_value = function(x2)

                if first_value > second_value:
                    a = x1
                else:
                    b = x1
                break
            else:
                k += 1
        else:
            b = x2
            x2 = x1
            x1 = a + fib_nums[n - k - 3] / fib_nums[n - k - 1] * (b - a)
            second_value = first_value
            first_value = function(x1)

            if k == n - 3:
                x2 = x1 + d
                first_value = function(x1)
                second_value = function(x2)

                if first_value > second_value:
                    a = x1
                else:
                    b = x1
                break
            else:
                k += 1
    return a, b, k
