class Vehicle:
    def __init__(self, car_no, speed, position):
        self.car_no = car_no
        self.speed = speed
        self.position = position
        
    def change_speed(self, speed):
        """
        Args:
            speed (list): [dx, dy]
        """
        self.speed = speed
    
    def whereiscar(self):
        return self.position[0], self.position[1] 
    
    def time_passed_dt(self):
        """if time flowed as dt, car move as speed.
        """
        self.position[0] = self.position[0] + self.speed[0]
        self.position[1] = self.position[1] + self.speed[1]