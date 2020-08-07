def has_negatives(a):
    result = []
    dataset = {}

    for number in a:
        change_neg_to_pos = abs(number)
        if change_neg_to_pos in dataset:
            dataset[change_neg_to_pos] += 1
        else:
            dataset[change_neg_to_pos] = 1
            
    sorted_dataset = sorted(dataset.items(), key = lambda pair: pair[1], reverse = True)
    for pair in sorted_dataset:
        if pair[1] > 1:
            result.append(pair[0])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
