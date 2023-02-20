import utils

# Match with vehicle.py
#  Start and Finish
#       3
#     2   1
#       4 
# 
#  SLOT
#  0 1
#  2 3
# 
#  Direction
#  S=0, L=1, R=2

# Match with reservation.py
dt = 0.1
T = 10


######################### FUNCTION #########################
# use for reserve multiple slot for each car
def reserve_car_by_car(car):
    '''check multiple reservation is possible for each car
    '''
    global slots
    # use for multiple slot
    car_timeline = [0 for _ in range(int(T/dt))]
    for slot in car.slot_to_reserve():
        # check time of slot after ETA
        can_times = slots[slot].check_reservation(eta=length/car.current_speed())
        for can_time in can_times:
            #  if given time exceed time for pass through crosssection
            if can_time[2] >= passtime:
                for t in range(int(can_time[0]/dt), int(can_time[1]/dt)+1):
                    car_timeline[t] += 1
    cnt = 0
    for time in range(len(car_timeline)):
        # if all slot that car have to reserve can be reserved by sucessively(continuously)
        if car_timeline[time] == len(car.slot_to_reserve()):
            cnt += 1
        else:
            cnt = 0
        # if given time exceed time for passing crossseciton
        if cnt>=passtime/dt:
            for slot in car.slot_to_reserve():
                slots[slot].reserve(time*dt - passtime, time*dt, car.car_no)
            break

def time_pass(time_passed = 1):
    '''update reservation list by time pass
    '''
    global slots
    for slot in slots:
        slot.time_passed_dt(time_passed = time_passed)
######################### FUNCTION #########################

######################### initialization #########################
# slot initialization
slot0 = utils.Reservation()
slot1 = utils.Reservation()
slot2 = utils.Reservation()
slot3 = utils.Reservation()
slots = [slot0, slot1, slot2, slot3]

# vehicle initialization
car_1 = utils.Vehicle(car_no=1, speed=2, start = 1, direction = 2)
car_2 = utils.Vehicle(car_no=2, speed=4, start = 2, direction = 0)
car_3 = utils.Vehicle(car_no=3, speed=2, start = 3, direction = 0)
car_4 = utils.Vehicle(car_no=4, speed=1, start = 4, direction = 1)
######################### initialization #########################


######################### setting #########################
# use for calculate ETA
length = 8
# time for pass crosssection
passtime = 1
######################### setting #########################

if __name__=='__main__':
    ######################### reserve each car #########################
    reserve_car_by_car(car = car_1)
    time_pass(time_passed=2)
    reserve_car_by_car(car = car_2)
    time_pass(time_passed=15)
    reserve_car_by_car(car = car_3)
    time_pass(time_passed=30)
    reserve_car_by_car(car = car_4)
    ######################### reserve each car #########################



    ######################### print reservation list #########################
    print(slot0.timeline)
    print(slot1.timeline)
    print(slot2.timeline)
    print(slot3.timeline, '\n')
    ######################### print reservation list #########################