from sumolib import checkBinary
import traci
from vehicle_sim import Vehicle
from reservation import Reservation

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

# main 함수 = simulmanager 클래스
def main():
    startSim()
    vehicles = []   # 존재하는 모든 차량 관리
    while shouldContinueSim():
        VEHICLES = traci.vehicle.getIDList()    # 시뮬레이터 안에 있는 차량 관리
        newVeh = traci.simulation.getDepartedIDList()
        for vehID in newVeh:
            vehicle = Vehicle(vehID)
            print(f'speed : {vehicle._speed}')
            # vehicle.reserve_car_by_car(slots)
            vehicles.append(vehicle)
        
        
        for v in vehicles:
            if v._carID not in VEHICLES:
                # print(v._carID)
                vehicles.pop(vehicles.index(v))
            # print(vehicles.count(v))
        # print(vehicles)
        
        
        
            # print(vehicles)
        # try: print(vehicles[0].getSpeed())
        # except: pass

        # print(vehicle)

            
            # avoidEdge(vehId, EDGE_ID)

        # for v in vehicle:
        #     if vehicle[0] == v:
        #         print(traci.vehicle.getLaneID(v))
                
        
        traci.simulationStep()
       

    traci.close()



def startSim():
    """Starts the simulation."""
    traci.start(
        [
            sumoBinary,
            '--net-file', './config/network.net.xml',
            '--route-files', './config/trips.trips.xml',
            '--step-length', '0.5',
            '--delay', '100',
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
