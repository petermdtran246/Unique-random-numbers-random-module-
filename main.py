import random

retries = 0

def unique_random_ints(how_many, max_num):
    """Return a list of how_many unique randomly generated numbers from
    0 to max_num (inclusive) using seed to initialize the random module"""
    global retries
    random_list = []
    while len(random_list) < how_many:
        random_number = random.randint(0, max_num)
        if random_number not in random_list:
            random_list.append(random_number)
        else:
            retries += 1
    return random_list


if __name__ == '__main__':
    seed = int(input())
    random.seed(seed)
    how_many = int(input())
    max_num = int(input())

    random_ints = unique_random_ints(how_many, max_num)
    print(' '.join(str(x) for x in random_ints), f"retries={retries}")