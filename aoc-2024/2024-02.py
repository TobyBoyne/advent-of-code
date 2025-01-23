import numpy as np

with open("day02.txt") as f:
    data = [np.array(line.split(), dtype=int) for line in f.readlines()]
    data = [x - x.min() for x in data]

def report_is_safe(report):
    diff = np.diff(report)
    monotone = (diff > 0).all() | (diff < 0).all()
    steady = ((np.abs(diff) > 0) & (np.abs(diff) < 4)).all()
    return steady & monotone

def report_is_safe_dampened(report, flip=False):
    diff = np.diff(report)
    dampened = False

    # always consider increasing reports
    if (diff > 0).sum() < len(report) // 2:
        diff = - diff

    descending = diff <= 0
    if descending.sum() > 1:
        # too much wrong direction
        return False
    elif descending.sum() == 1:
        dampened = True
        idx = np.argwhere(descending).item()
        removed_diff = diff[idx]
        diff = np.concatenate([diff[:idx], diff[idx+1:]])
        if idx < len(diff):
            diff[idx] += removed_diff

    unsteady = np.abs(diff) > 3
    # due to monotonicity, unsteadiness can only be fixed at the extreme values
    if unsteady.sum() > 1:
        return False
    elif unsteady.sum() == 1:
        return not dampened and unsteady[1:-1].sum() == 0
        
    return True

def report_is_safe_lazy(report):
    # lazy way with dampening
    combinations = [np.concatenate((report[:i], report[i+1:])) for i in range(len(report))]
    combinations.append(report)
    return any(map(report_is_safe, combinations))


safe_reports = 0
for report in data:
    safe_reports += report_is_safe(report)

print(safe_reports)

safe_dampen_reports = 0
for report in data:
    if not report_is_safe_dampened(report) and report_is_safe_lazy(report):
        print(report)
    safe_dampen_reports += report_is_safe_dampened(report)

print(safe_dampen_reports)

safe_reports_lazy = 0
for report in data:
    safe_reports_lazy += report_is_safe_lazy(report)

print(safe_reports_lazy)
