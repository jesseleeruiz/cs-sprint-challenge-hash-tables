def intersection(arrays):
    dataset = {}
    result = []

    for lists in arrays:
        for number in lists:
            if number in dataset:
                dataset[number] += 1
            else:
                dataset[number] = 1

    sorted_dataset = sorted(dataset.items(), key = lambda pair: pair[1], reverse = True)
    for pair in sorted_dataset:
        if pair[1] > 1:
            result.append(pair[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
