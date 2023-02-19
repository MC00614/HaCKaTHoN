# import numpy as np

# 1. 한 차량에 대해 예약리스트 체크 후 예약업데이트
# 2. 다음 차량에 같은 작업 수행
# 3. 예약리스트는 가능한 예약 시간을 보여주고, 차량 측에서 예약 시간 정하기
# 4. 가속을 고려하는 것은 어떻게 할지 고민해보자 
# (앞 시간대에 예약이 없을 때 가속할지, 가속을 고려해서 예약을 해놓을지 고민 필요)
# 일단은 가속을 고려해서 예약해보자 (예약이 없다고 가속해버리면, 따로 가속한 두 차량이 충돌 할 수도 있을까?)

# 지금처럼 하면, 10초 이내에서 한번 예약 후 예약이 실시간 업데이트 되지는 않음.
# 예약이 실시간으로 업데이트 되지 않아도 되려면, 가속 고려해서 예약하는 것이 좋을 것으로 예상 (eta와 time_advance 이용)

class Reservation:
    '''Reservation List for Divided Section
    '''
    def __init__(self, dt = 0.1, T = 10):
        self.dt = dt
        self.T = T
        self.timeline = [0 for _ in range(int(self.T/self.dt))]
        
    def check_reservation(self, eta, can_advance = 0):
        """Return time when you can reserve

        Args:
            eta (float): Estimated time of arrival
            can_advance (float) : time that you can advance by acceleration
        """
        start = -1
        can_reserve = []
        for t in range(int((eta - can_advance)/self.dt), int(self.T/self.dt)):
            if start==-1 and self.timeline[t]==0:
                start = t
            if start!=-1 and self.timeline[t]!=0:
                finish = t - self.dt
                interval = finish*self.dt - start*self.dt
                can_reserve.append([start*self.dt, finish*self.dt, interval])
                start = -1
        if start!=-1:
            interval = int(self.T/self.dt-self.dt)*self.dt - start*self.dt
            can_reserve.append([start*self.dt, int(self.T/self.dt-self.dt)*self.dt, interval])
        return can_reserve
                
                
    def reserve(self, start, finish, car_no):
        """Reserve start to finish in timeline
        """
        for t in range(int(start/self.dt), int(finish/self.dt)):
            if self.timeline[t]==0:
                self.timeline[t] = car_no
            else:
                print(f'ERROR : time converge with {self.timeline[t]}')
                print(start, finish, t)
                return
            
            
    def time_passed_dt(self):
        """if time flowed as dt, list move leftside.
        """
        self.timeline.pop(0)
        self.timeline.append(0)
        
        
if __name__== "__main__":
    #### 사용 예시 ####

    # 슬롯 초기화
    slot = Reservation()

    # 3초 뒤 도착할건데, 3초 뒤로 가능한 시간좀 보여주세요
    can_time = slot.check_reservation(eta = 3.0)
    print(can_time)

    for time in can_time:
        # 내 차는 지나가는데 3초가 필요합니다
        if time[1] - time[0] > 3:
            # 3초간 예약해주세요
            slot.reserve(time[0], time[0]+3, car_no=1)
            break
    print(slot.timeline)
    print(slot.timeline.count(1))

    # 한 시퀀스가 끝났으니 타임라인을 한 칸씩 옮길게요
    slot.time_passed_dt()
    print(slot.timeline)

    # 차량이 한 대 더 옵니다
    # 5초 뒤 도착할건데, 5초 뒤로 가능한 시간좀 보여주세요
    can_time = slot.check_reservation(eta = 5.0)
    print(can_time)

    for time in can_time:
        # 내 차는 지나가는데 2초가 필요합니다
        if time[1] - time[0] > 2:
            # 2초간 예약해주세요
            slot.reserve(time[0], time[0]+2, car_no=2)
            break
    print(slot.timeline)
    print(slot.timeline.count(2))

    # 한 시퀀스가 끝났으니 타임라인을 한 칸씩 옮길게요
    slot.time_passed_dt()
    print(slot.timeline)

    #### 사용 예시 ####
