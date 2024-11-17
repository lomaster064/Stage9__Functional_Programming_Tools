def is_prime(func):
    def wrapper(*args):
        res = func(*args)

        sost = 0

        for i in range(2, res):
            if res % i == 0:
                # print('Делится на', i)
                sost = 1

        if sost == 1:
            print('Составное')
        else:
            print('Простое')

        return res

    return wrapper


@is_prime
def sum_three(*args):
    summary = 0
    for i in args:
        summary += i

    return summary


result = sum_three(121, 0, 0)

print(result)
