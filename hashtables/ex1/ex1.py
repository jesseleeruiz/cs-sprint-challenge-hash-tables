def get_indices_of_item_weights(weights, length, limit):
    dataset = {}

    for weight in range(len(weights)):
        target = limit - weights[weight]
        if target in dataset:
            result = (weight, dataset[target])
            return result
        else:
            dataset[weights[weight]] = weight

    return None
