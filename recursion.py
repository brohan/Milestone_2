def recursive_unwind(x):
    if x < 0:
        print('found negative x!')
        return x
    else:
        x -= 1
        print('in else: x: {}'.format(x))
        return recursive_unwind(x)


if __name__ == "__main__":
    print(recursive_unwind(1))