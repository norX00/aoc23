with open("day19.txt", "r") as of:
    data = of.read().strip()

w, m = data.split("\n\n")
workflows = {key: values for key, values in [wf[:-1].split("{") for wf in w.split("\n")]}
machine_parts = [eval(s.replace("=", "':").replace(",", ",'").replace("{", "{'")) for s in m.split("\n")]


def check_acceptance(parts, workflow="in"):
    if workflow in "AR":
        return workflow == "A"
    for check in workflows[workflow].split(","):
        match check.split(":"):
            case remaining_wf,:
                return check_acceptance(parts, remaining_wf)
            case condition, remaining_wf:
                value = str(parts.get(condition[0]))
                inequality = condition[1:]
                if eval(value+inequality):
                    return check_acceptance(parts, remaining_wf)

# Part one
print(sum(sum(mp.values()) for mp in machine_parts if check_acceptance(mp)))
