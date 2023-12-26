import random
def gen_random(num_count, begin, end):
    ans = [int(random.uniform(begin, end)) for i in range(num_count) ]
    return ans

print(gen_random(5, 1, 10))