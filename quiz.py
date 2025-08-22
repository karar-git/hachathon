def find_missing_range(frames: list[int]) -> dict:
    result = {'gaps': []}
    result['longest_gap'] = []
    result['missing_count'] = 0

    if not frames:
        return result

    asset = set(frames)

    first = last = 0
    for i in range(1, max(frames) +1):
        if i not in asset: 
            if first == 0: 
                first = last = i
            elif last + 1 != i: 
                result['gaps'].append([first, last])
                first = last = i
            else:
                last = i
        else:
            if first != 0:
                result['gaps'].append([first, last])
                first = last = 0

    result['longest_gap'] = result['gaps'][0]
    for i in result['gaps']:
        result['missing_count'] += i[1] +1 - i[0]
        if i[1] - i[0] > result['longest_gap'][1] - result['longest_gap'][0] : result['longest_gap'] = i

    return result
