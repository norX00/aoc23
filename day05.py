# from functools import reduce

with open("day5.txt", "r") as of:
    data = of.read().strip()

seeds, *maps = data.split("\n\n")
seed_nums = [int(num) for num in seeds.split(" ")[1:]]


# Part one - functional programming approach fails: hash-maps too large
# def parse_map(map_str):
#     map_dct = dict()
#     for ln in map_str.split("\n")[1:]:
#         dest_start, src_start, range_len = [int(num) for num in ln.split(" ")]
#         for i in range(range_len):
#             map_dct[src_start + i] = dest_start + i
#     return map_dct
# maps_lst = [parse_map(m) for m in maps]
# print(min([reduce(lambda arg, m: m.get(arg, arg), maps_lst, seed) for seed in seed_nums]))

# Part one - iterative if/else approach
for i, sn in enumerate(seed_nums):
    current = sn
    for m in maps:
        for ln in m.split("\n")[1:]:
            dest_start, src_start, range_len = [int(num) for num in ln.split(" ")]
            if src_start <= current <= src_start + range_len:
                current += dest_start - src_start
                break
    seed_nums[i] = current
print(min(seed_nums))

# Part two
seed_nums = [int(num) for num in seeds.split(" ")[1:]]
min_location = max(seed_nums)
for i in range(0, len(seed_nums), 2):
    seed_low = seed_nums[i]
    max_len = n = seed_nums[i + 1]
    seed_next = seed_low
    while seed_next <= seed_low + n:
        current = seed_next
        for m in maps:
            for ln in m.split("\n")[1:]:
                dest_start, src_start, range_len = [int(num) for num in ln.split(" ")]
                if src_start <= current <= src_start + range_len:
                    # maps are monotonically increasing within their preimage which is an interval of at most max_len
                    max_len = max(min(max_len, src_start + range_len - current), 1)
                    current += dest_start - src_start
                    break
        min_location = min(min_location, current)
        seed_next += max_len
        max_len = n - seed_next + seed_low
print(min_location)
