def mean(x):
    return sum(x) / len(x)


def median(x):
    center = len(x) // 2
    return (
        sorted(x)[center]
        if len(x) % 2 != 0
        else mean(sorted(x)[center - 1 : center + 1])
    )
