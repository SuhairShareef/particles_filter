import numpy as np

def rchoose(list1, weights):
    '''
    list1   :    list of elements you're picking from.
    weights :    list of weights. Has to be in the same order as the 
                 elements of list1. It can be given as the number of counts 
                 or as a probability.
    '''

    # sorting the normalized weights and the desired list simultaneously
    weights_normalized, list1 = zip(*sorted(zip(weights_normalized, list1)))

    # bringing the sorted tuples back to being lists
    weights_normalized = list(weights_normalized)
    list1 = list(list1)

    # finalizing the weight normalization
    dummy = []; count = 0
    for item in weights_normalized:
        count += item
        dummy.append(count)
    weights_normalized = dummy

    # testing which interval the uniform random number falls in
    random_number = np.random.uniform(0, 1)
    for idx, w in enumerate(weights_normalized[:-1]):
        if random_number <= w:
            return list1[idx]

    return list1[-1]

print(rchoose([]))