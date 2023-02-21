import traci

def floatupper(value):
    """
    소수점 에러 문자열로 처리
    """
    value = str(value)
    temp = value.split('.')
    if len(temp[1]) >= 2:
        value = temp[0] +'.'+ str(int(temp[0]) + 1)
    return float(value)

def avoidEdge(vehId, edgeId):
    """Sets an edge's travel time for a vehicle infinitely high, and reroutes the vehicle based on travel time.
    Args:
        vehId (Str): The ID of the vehicle to reroute.
        edgeId (Str): The ID of the edge to avoid.
    """
    traci.vehicle.setAdaptedTraveltime(
        vehId, edgeId, float('inf'))
    traci.vehicle.rerouteTraveltime(vehId)


def addControlledLanes(self, lanes):
        for lane in lanes:
            self._controlledLanes.add(lane)


def getAcceleration(self):
        return max([v.getAcceleration() for v in self.getAllVehicles()])


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

def flatten(l):
    # A basic function to flatten a list
    return [item for sublist in l for item in sublist]