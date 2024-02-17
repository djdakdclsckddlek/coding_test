# 주차 요금 계산
import math
def solution(fees, records):
    parking = {}
    parkingtimes = {}
    result = []
    for i in records:
        time, car_n, inout = i.split(' ')
        if inout == 'IN':
            parking[car_n] = time
        
        if inout == 'OUT':
            intime = parking.pop(car_n)
            in_h, in_m = intime.split(':')
            out_h, out_m = time.split(':')
            parkingtime = (int(out_h) - int(in_h)) * 60 + (int(out_m) - int(in_m))
            
            if car_n not in parkingtimes:
                parkingtimes[car_n] = parkingtime
            else:
                parkingtimes[car_n] += parkingtime
    
    for car_n, intime in parking.items():
        in_h, in_m = intime.split(':')
        if car_n in parkingtimes:
            parkingtimes[car_n] += (24- int(in_h)) * 60 - int(in_m) - 1
        else:
            parkingtimes[car_n] = (24- int(in_h)) * 60 - int(in_m) - 1
            
    parkingtimes = dict(sorted(parkingtimes.items()))
    for time in parkingtimes.values():
        if time <= fees[0]:
            result.append(fees[1])
            continue

        ceiltime = math.ceil((time - fees[0]) / fees[2])
        totalfee = fees[1] + ceiltime * fees[3]
        result.append(totalfee)
        
    return result