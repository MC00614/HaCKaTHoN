import traci

class Vehicle():
    def __init__(self, vehicle):
        self._carID = vehicle                           # 차량 id
        self._speed = 20   # 현재 속도
        # traci.vehicle.setSpeed(self._speed)
        self._acceleration = 0 # 가속
        self._route = traci.vehicle.getRoute(vehicle)   # 지나갈 경로들 id list
        self._edge = self.getEdge()     # 현재 위치한 차선id
        self._active = True                             # 차량 attribute가 바뀌었는지 아닌지 정보
        self.passtime = 1
        # self._direection = 
        self._previouslySetValues = dict()

        self.startIndex = traci.vehicle.getLaneIndex(self._carID)
        if self._route[0] == '-E3' and self._route[-1] == 'E4':
            self.direction = 'r'
        elif self._route[0] == '-E3' and self._route[-1] == 'E5':
            self.direction = 'l'
        elif self._route[0] == '-E3' and self._route[-1] == 'E6':
            self.direction = 's'
        elif self._route[0] == '-E4' and self._route[-1] == 'E3':
            self.direction = 'l'
        elif self._route[0] == '-E4' and self._route[-1] == 'E5':
            self.direction = 's'
        elif self._route[0] == '-E4' and self._route[-1] == 'E6':
            self.direction = 'r'
        elif self._route[0] == '-E5' and self._route[-1] == 'E3':
            self.direction = 'r'
        elif self._route[0] == '-E5' and self._route[-1] == 'E4':
            self.direction = 's'
        elif self._route[0] == '-E5' and self._route[-1] == 'E6':
            self.direction = 'l'
        elif self._route[0] == '-E6' and self._route[-1] == 'E3':
            self.direction = 's'
        elif self._route[0] == '-E6' and self._route[-1] == 'E4':
            self.direction = 'l'
        elif self._route[0] == '-E6' and self._route[-1] == 'E5':
            self.direction = 'r'
        

        # 변수 후보군
        self._carlength = traci.vehicle.getLength(vehicle)
        self._lanelength = traci.lane.getLength(self.getLane())        
        self._maxSpeed = traci.vehicle.getMaxSpeed(vehicle)


    def time_passed_dt(self):
        """if time flowed as dt, car move as speed.
        """
        self.position = self.position + self._speed

    # 
    # def check_timetable(self, car):   
        


    def slot_to_reserve(self):
        '''return slots for cross2x2
        '''
        direction = self.direction
        if self._route[0] == '-E3':
            if self.startIndex == 0:
                if direction == 's':
                    return [0,4,8,12]
                else: return [0]

            elif self.startIndex == 1:
                if direction == 's':
                    return [1,5,9,13]
                else: return [1,5,9,10,11]

        elif self._route[0] == '-E4':
            if self.startIndex == 0:
                if direction == 's':
                    return [12,13,14,15]
                else: return [12]

            elif self.startIndex == 1:
                if direction == 's':
                    return [8,9,10,11]
                else: return [2,6,8,9,10]

        elif self._route[0] == '-E5':
            if self.startIndex == 0:
                if direction == 's':
                    return [0,1,2,3]
                else: return [3]
            elif self.startIndex == 1:
                if direction == 's':
                    return [4,5,6,7]
                else: return [5,6,7,9,13]
                
        elif self._route[0] == '-E6':
            if self.startIndex == 0:
                if direction == 's':
                    return [3,7,11,15]
                else: return [15]

            elif self.startIndex == 1:
                if direction == 's':
                    return [2,6,10,14]
                else: return [4,5,6,10,14]
            
    def get_eta(self):
        value = str(round(self.getLength()/self._speed, 2))
        # print(f'length : {self.getLength()}')
        temp = value.split('.')
        # print(f'value : {value}')
        if len(temp[1]) >= 2:
            value = value[:-2] + str(int(value[-2]) + 1)
            # print(f'after : {value}')
        return float(value)

    def getAcceleration(self):
        return self._acceleration

    def isActive(self):
        return self._active
    
    def getEdge(self):              # 현재 차량이 위치한 경로
        return traci.vehicle.getRoadID(self.getName())

    def getLane(self):              # 현재 차량이 위치한 차선(Edge보다 더 상세) ?? 왜 똑같다 나오지
        return traci.vehicle.getLaneID(self.getName())

    def getLaneIndex(self):         # 몇차로인지 알려줌. 
        return traci.vehicle.getLaneIndex(self.getName())

    def getLanePosition(self):      # 현재 위치하는 차선의 시작점부터 차 위치까지 거리 [m]
        return traci.vehicle.getLanePosition(self.getName())

    def getLanePositionFromFront(self):
        return traci.lane.getLength(self.getLane()) - self.getLanePosition()

    def getLeader(self):
        return traci.vehicle.getLeader(self.getName(), 20)

    def getLength(self):            # 차선 길이 반환.
        return self._lanelength

    def getMaxSpeed(self):
        return self._maxSpeed

    def getName(self):
        return self._carID

    def getRemainingRoute(self):
        return self._route[traci.vehicle.getRouteIndex(self.getName()):]

    def getRoute(self):             # 차량이 지나갈 경로 튜플
        return self._route

    def getSpeed(self):
        return traci.vehicle.getSpeed(self.getName())

    def setColor(self, color):
        self._setAttr("setColor", color)

    def setInActive(self):
        self._active = False

    def setMinGap(self, minGap):
        self._setAttr("setMinGap", minGap)

    def setTargetLane(self, lane):
        traci.vehicle.changeLane(self.getName(), lane, 0.5)

    def getAcceleration(self, acceleration):
        return self._acceleration

    def setSpeedMode(self, speedMode):
        self._setAttr("setSpeedMode", speedMode)

    def setSpeedFactor(self, speedFactor):
        self._setAttr("setSpeedFactor", speedFactor)

    def _setAttr(self, attr, arg):
        # Only set an attribute if the value is different from the previous value set
        # This improves performance
        if self.isActive():
            if attr in self._previouslySetValues:
                if self._previouslySetValues[attr] == arg:
                    return
            self._previouslySetValues[attr] = arg
            getattr(traci.vehicle, attr)(self.getName(), arg)

