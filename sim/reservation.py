import traci
from utils import *


class Reservation():

    def __init__(self, dt = 0.1, T = 10):
        # lanes = traci.trafficlight.getControlledLanes(intersection) # getControlledLanes(x) :x에 의해 제어되는 차선 목록 반환
        # self.lanesServed = set(lanes)       # 신호등과 연결되어있는 차선id set
        # self.name = intersection            # 신호등 있는 교차로 id
        self.T = T
        self.dt = dt
        self.passtime = 3
        self.timeline = [0 for _ in range(int(self.T/self.dt))]

    def check_reserve(self, eta, can_advance=0):
        """Return time when you can reserve

        Args:
            eta (float): Estimated time of arrival
            can_advance (float) : time that you can advance by acceleration
        """
        start = -1
        can_reserve = []
        for t in range(int((eta - can_advance)/self.dt), int(self.T/self.dt)):
            if start==-1 and self.timeline[t]==0:   # self.timeline[t]에 예약이 차있으면 t가 계속 넘어감
                start = t
                # print(start)
            if start!=-1 and self.timeline[t]!=0:
                # t가 끝(9.9초)에 도달하거나 그 전에 예약이 잡혀있는 경우(1이 있는 경우)
                # 예약 가능한 끝시간 부여
                finish = t - self.dt
                interval = finish*self.dt - start*self.dt
                can_reserve.append([floatupper(start*self.dt), floatupper(finish*self.dt), floatupper(interval)])
                # print(f'start : {floatupper(start*self.dt)}')
                # print(f'finish : {floatupper(finish*self.dt)}')
                start = -1
        if start!=-1:
            interval = int(self.T/self.dt-self.dt)*self.dt - start*self.dt
            can_reserve.append([floatupper(start*self.dt), floatupper(int(self.T/self.dt-self.dt)*self.dt), floatupper(interval)])
        return can_reserve

    # def calculate_eta(self, v):
        # pass

    
    def reserve(self, start, finish, car):
        """Reserve start to finish in timeline
        """
        for t in range(int(start/self.dt), int(finish/self.dt), ):
            if self.timeline[t]==0:
                self.timeline[t] = car

            else:
                # print(f'ERROR : time converge with {self.timeline[t]}')
                return

    def time_passed_dt(self):
        """if time flowed as dt, list move leftside.
        """
        self.timeline.pop(0)
        self.timeline.append(0)



    

    # def time_pass(time_passed = 1):
    #     '''update reservation list by time pass
    #     '''
    #     global slots
    #     for slot in slots:
    #         slot.time_passed_dt(time_passed = time_passed)
    # def update(self):
    #     """
    #     Performs various functions to update the junction's state.
    #     1. Ensures that all vehicles being managed by the junction, have thier automatic
    #        stopping behaviour deactived (otherwise they are too cautious at the intersection)
    #     2. Removes platoons that are no longer in the sphere of influence of the function
    #     3. Updates the speed of all platoons being managed by the controller.
    #     """
    #     # 다양한 기능을 수행하여 교차로 상태를 업데이트합니다.
    #     # 1. 교차로에 의해 관리되는 모든 차량의 자동 정지 동작이 비활성화되었는지 확인합니다(그렇지 않을 경우 교차로에서 너무 조심함)
    #     # 2. 더 이상 기능의 영향권에 속하지 않는 소대를 제거합니다
    #     # 3. 컨트롤러가 관리하는 모든 플랫폼의 속도를 업데이트합니다.

    #     reservedTime = 0
    #     if self.zip:
    #         self._generatePlatoonZips()
    #         for v in self.getVehicleZipOrderThroughJunc():
    #             if v.isActive() and v.getLane() in self.lanesServed:
    #                 speed = self.getNewSpeed(v, reservedTime)
    #                 v.setSpeed(speed)
    #                 reservedTime = self.calculateNewReservedTime(v, reservedTime)
    #     else:
    #         for p in self.platoons:
    #             # Update the speeds of the platoon if it has not passed the junction
    #             if p.getLane() in self.lanesServed:
    #                 speed = self.getNewSpeed(p, reservedTime)
    #                 if speed == -1:
    #                     p.removeTargetSpeed()
    #                 else:
    #                     p.setTargetSpeed(speed)
    #                 reservedTime = self.calculateNewReservedTime(p, reservedTime)
    #     self._logIntersectionStatus(reservedTime)

    

    # def calculateNewReservedTime(self, pv, reservedTime):
    #     """
    #     Calculates the time that is needed to be reserved for a given platoon or vehicle (pv)
    #     """
    #     # If this platoon is the first to post a reservation, the distance to the junction needs to be included
    #     if reservedTime == 0:
    #         lenThruJunc = self._getLanePosition(pv) + pv.getLength()
    #     else:
    #         lenThruJunc = pv.getLength() * 2 if self.zip else 1
    #     return (0.5 if self.zip else 1.5) + reservedTime + (lenThruJunc / (pv.getSpeed() or 1))


   

        # def getNewSpeed(self, pv, reservedTime):
        #     """
        #     Gets the speed the platoon or vehicle should adhere to in order to pass through the intersection safely
        #     """
        #     distanceToTravel = self._getLanePosition(pv)
        #     currentSpeed = pv.getSpeed()
        #     # If we are in the last 20 metres, we assume no more vehicles will join the platoon
        #     # and then set the speed to be constant. This is because if we did not speed tends
        #     # towards 0 (as the distance we give is to the junction and not to the end of the platoon's
        #     # route.
        #     if distanceToTravel > 20:
        #         pv.setSpeedMode(23)
        #         speed = distanceToTravel / (reservedTime or 1)
        #         speed = max([speed, 0.5])
        #         if speed >= currentSpeed:
        #             speed = pv.getMaxSpeed()
        #     elif currentSpeed == 0:
        #         speed = pv.getMaxSpeed()
        #     else:
        #         return pv.getMaxSpeed()
        #     if reservedTime == 0:
        #         return pv.getMaxSpeed()
        #     return speed
    
