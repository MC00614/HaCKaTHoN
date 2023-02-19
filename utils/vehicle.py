class Vehicle:
    def __init__(self, car_no, speed, start, direction):
        self.car_no = car_no
        self.speed = speed
        self.position = 0
        self.start = start
        self.direction = direction
    
    def current_speed(self):
        return self.speed
    
    def change_speed(self, speed):
        """speed (float): speed to change by reservation
        """
        self.speed = speed
        
    def time_passed_dt(self):
        """if time flowed as dt, car move as speed.
        """
        self.position = self.position + self.speed    

    def slot_to_reserve(self):
        start = self.start
        direction = self.direction
        if start == 1:
            if direction == 0:
                return [1,0]
            elif direction == 1:
                return [1,3,2]
            elif direction == 2:
                return [1]
    
        elif start == 2:
            if direction == 0:
                return [2,3]
            elif direction == 1:
                return [2,0,1]
            elif direction == 2:
                return [2]
        
        elif start == 3:
            if direction == 0:
                return [0,2]
            elif direction == 1:
                return [0,1,3]
            elif direction == 2:
                return [0]
            
        elif start == 4:
            if direction == 0:
                return [3,1]
            elif direction == 1:
                return [3,2,0]
            elif direction == 2:
                return [3]
        
