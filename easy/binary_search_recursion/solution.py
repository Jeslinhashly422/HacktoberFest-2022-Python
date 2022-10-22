def solution(arr='',target=float('-inf')):
    if target==float('-inf'):return -1
    mid = len(arr) // 2
    if len(arr) == 1:
        return mid if arr[mid] == target else -1
    elif arr[mid] == target:
        return mid
    else:
        if arr[mid] < target:
            callback_response = solution((arr[mid:]), target)
            return mid + callback_response if callback_response is not -1 else -1
        else:
            return solution((arr[:mid]), target)