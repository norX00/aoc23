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
