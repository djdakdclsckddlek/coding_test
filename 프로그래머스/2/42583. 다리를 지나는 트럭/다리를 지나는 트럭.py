from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    time = 0
    sum_trucks = 0
    while truck_weights:
        sum_trucks -= bridge.popleft()
        if sum_trucks + truck_weights[0] <= weight:
            sum_trucks += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else: bridge.append(0)
        time += 1

    return time + len(bridge)