from sumolib import checkBinary
import traci
from vehicle_sim import Vehicle
from reservation_copy import Reservation

sumoBinary = checkBinary('sumo-gui')

RED = [255, 0, 0]
EDGE_ID = 'closed'

slot0 = Reservation()
slot1 = Reservation()
slot2 = Reservation()
slot3 = Reservation()
slot4 = Reservation()
slot5 = Reservation()
slot6 = Reservation()
slot7 = Reservation()
slot8 = Reservation()
slot9 = Reservation()
slot10 = Reservation()
slot11 = Reservation()
slot12 = Reservation()
slot13 = Reservation()
slot14 = Reservation()
slot15 = Reservation()

slots = [slot0, slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15]

# Match with reservation.py
dt = 0.1
T = 1000

def reserve_car_by_car(car, vehID, eta, can_advance=0):
    '''check multiple reservation is possible for each car
    '''
    global slots
    ######################### setting #########################
    # time for pass crosssection
    passtime = 5
    ######################### setting #########################
    # use for multiple slot
    car_timeline = [0 for _ in range(int(T/dt))]
    for slot in car.slot_to_reserve():
        # check time of slot after ETA
        can_times = slots[slot].check_reservation(eta=eta, can_advance=can_advance)
        for can_time in can_times:
            #  if given time exceed time for pass through crosssection
            if can_time[2] >= passtime:
                for t in range(int(can_time[0]/dt)+1, int(can_time[1]/dt)+1):
                    car_timeline[t] += 1
    cnt = 0
    for time in range(len(car_timeline)):
        # if all slot that car have to reserve can be reserved by sucessively(continuously)
        if car_timeline[time] == len(car.slot_to_reserve()):
            cnt += 1
        else:
            cnt = 0
        # if given time exceed time for passing crossseciton
        if cnt>=int(passtime/dt):
            print(f'car_no {vehID} is reserved in {time*dt - passtime} to {time*dt} at {car.slot_to_reserve()}')
            for slot in car.slot_to_reserve():
                slots[slot].reserve(time*dt - passtime, time*dt, vehID)
            return time*dt - passtime
            # break

def time_pass(time_passed = 1):
    '''update reservation list by time pass
    '''
    global slots
    for slot in slots:
        slot.time_passed_dt(time_passed = time_passed)

# main 함수 = simulmanager 클래스
def main():
    startSim()
    vehicles = []   # 존재하는 모든 차량 관리
    while shouldContinueSim():
        VEHICLES = traci.vehicle.getIDList()    # 시뮬레이터 안에 있는 차량 관리
        newVeh = traci.simulation.getDepartedIDList()

        for vehID in newVeh:
            traci.vehicle.setSpeedMode(vehID, 0)
            car = Vehicle(vehID)
            # 
            # traci.vehicle.setSpeed(vehID, 20)
            # traci.vehicle.setAccel(vehID, 9999)
            # 
            # print(f'speed : {vehicle._speed}')
            new_eta = reserve_car_by_car(car, vehID, eta=car.get_eta(), can_advance=0)
            traci.vehicle.setSpeed(vehID, car.getLength()/new_eta)
            vehicles.append(car)

        # print(slot8.timeline)
        for v in vehicles:
            if v._carID not in VEHICLES:
                # print(v._carID)
                vehicles.pop(vehicles.index(v))
        time_pass(time_passed = 1)
        traci.simulationStep()
    traci.close()



def startSim():
    """Starts the simulation."""
    traci.start(
        [
            sumoBinary,
            '--net-file', './config/network.net.xml',
            '--route-files', './config/trips.trips.xml',
            '--step-length', '0.1',
            '--delay', '50',
            '--gui-settings-file', './config/viewSettings.xml',
            '--start'

        ])


def shouldContinueSim():
    """Checks that the simulation should continue running.
    Returns:
        bool: `True` if vehicles exist on network. `False` otherwise.
    """
    numVehicles = traci.simulation.getMinExpectedNumber()
    return True if numVehicles > 0 else False


def setVehColor(vehId, color):
    """Changes a vehicle's color.
    Args:
        vehId (String): The vehicle to color.
        color ([Int, Int, Int]): The RGB color to apply.
    """
    traci.vehicle.setColor(vehId, color)


def avoidEdge(vehId, edgeId):
    """Sets an edge's travel time for a vehicle infinitely high, and reroutes the vehicle based on travel time.
    Args:
        vehId (Str): The ID of the vehicle to reroute.
        edgeId (Str): The ID of the edge to avoid.
    """
    traci.vehicle.setAdaptedTraveltime(
        vehId, edgeId, float('inf'))
    traci.vehicle.rerouteTraveltime(vehId)


def getOurDeparted(filterIds=[]):
    """Returns a set of filtered vehicle IDs that departed onto the network during this simulation step.
    Args:
        filterIds ([String]): The set of vehicle IDs to filter for.
    Returns:
        [String]: A set of vehicle IDs.
    """
    newlyDepartedIds = traci.simulation.getDepartedIDList()
    filteredDepartedIds = newlyDepartedIds if len(
        filterIds) == 0 else set(newlyDepartedIds).intersection(filterIds)
    return filteredDepartedIds


if __name__ == "__main__":
    main()
