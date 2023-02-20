import cv2
import numpy as np
import random
import time
import math
class timer():
    def __init__(self):
        self.time = 0
    def timeflow(self):
        self.time = self.time+1

class car():
    def __init__(self,shape,reservation_time = 1000,speed = 1):
        self.misson_mode = random.randint(1,16)
        self.shape = shape
        self.time = 0
        self.accel = 0
        self.reservation_time = reservation_time
        self.speed = speed
        
        self.course= {
            1 : [self.shape[0]-1,int(self.shape[1]*0.424)],
            3 : [int(self.shape[0]*0.574),self.shape[1]-1],
            2 : [self.shape[0]-1,int(self.shape[1]*0.473)],
            4 : [int(self.shape[0]*0.522),self.shape[1]-1],
            5 : [1,int(self.shape[1]*0.576)],
            6 : [1,int(self.shape[1]*0.527)],
            7 : [int(self.shape[0]*0.426),1],
            8 : [int(self.shape[0]*0.478),1], #여기까지 직진
            9 : [1,int(self.shape[1]*0.527)],  #좌회전
            10 : [self.shape[0]-1,int(self.shape[1]*0.473)], #좌회전
            11 : [int(self.shape[0]*0.478),1], #좌회전
            12 : [int(self.shape[0]*0.522),self.shape[1]-1], #좌회전
            13 : [self.shape[0]-1,int(self.shape[1]*0.424)], #우회전
            14 : [int(self.shape[0]*0.574),self.shape[1]-1],  #우회전
            15 : [1,int(self.shape[1]*0.576)], #우회전
            16 : [int(self.shape[0]*0.426),1] #우회전
        }
    #함
    def move_course1(self,image):
        if self.misson_mode == 1:
            cv2.circle(image,tuple(self.course[1]),10,(255,255,255), -1)
            self.time = self.time + 1
            if self.time >= 2*self.reservation_time:
                    self.course[1][0] = self.course[1][0] - 10
            else:
                    self.course[1][0] = self.course[1][0] - 1
            self.time = self.time + 1
                                                                # 0.4*self.shape[0]/reservation_time = 0.1초당 가야되는 픽셀
                                                                # 1speed = 2pixel  요구 스피드 = int(floor(0.4*self.shape[0]/reservation_time/2))
        #속도 10기준 교차로 통과 시간 => 넉넉하게 200칸 이라 가정 1초
        if self.misson_mode == 3:
            cv2.circle(image,self.course[3],10,(0,0,0), -1)
            if self.time >= 2*self.reservation_time:
                self.course[3][1] = self.course[3][1] - 10
            else:
                self.course[3][1] = self.course[3][1] - 1 
            self.time = self.time + 1
            
        if self.misson_mode == 2:
            cv2.circle(image,self.course[2],10,(255,0,255), -1)
            if self.time >= 2*self.reservation_time:
                self.course[2][0] = self.course[2][0] - 10
            else:
                self.course[2][0] = self.course[2][0] - 1
            self.time = self.time + 1
            
            
        if self.misson_mode == 4:
            cv2.circle(image,self.course[4],10,(0,0,0), -1)
            if self.time >= 2*self.reservation_time:
                self.course[4][1] = self.course[4][1] - 10                    
            else:
                self.course[4][1] = self.course[4][1] - 1        
            self.time = self.time + 1
            
        if self.misson_mode == 5:
            cv2.circle(image,self.course[5],10,(55,55,55), -1)
            if self.time >= 2*self.reservation_time:
                self.course[5][0] = self.course[5][0] + 10
            else: 
                self.course[5][0] = self.course[5][0] + 1   
            self.time = self.time + 1
            
        if self.misson_mode == 6:
            cv2.circle(image,self.course[6],10,(25,150,255), -1)
            if self.time >= 2*self.reservation_time:
                self.course[6][0] = self.course[6][0] + 10
            else:
                self.course[6][0] = self.course[6][0] + 1    
            self.time = self.time + 1
            
        if self.misson_mode == 7:
            cv2.circle(image,self.course[7],10,(0,0,0), -1)
            if self.time >= 2*self.reservation_time:
                self.course[7][1] = self.course[7][1] + 10
            else:
                self.course[7][1] = self.course[7][1] + 1
            self.time = self.time + 1 
        
        if self.misson_mode == 8:
            cv2.circle(image,self.course[8],10,(0,0,0), -1)
            if self.time >= 2*self.reservation_time:
                self.course[8][1] = self.course[8][1] + 10
            else:
                self.course[8][1] = self.course[8][1] + 1
            self.time = self.time + 1
        #함   
        if self.misson_mode == 9:
            cv2.circle(image,self.course[9],10,(150,80,0), -1)
            if(self.course[9][0]<0.4*(self.shape[0])):
                    if self.time >= 2*self.reservation_time:
                        self.course[9][0] = self.course[9][0] + 10
                    else:
                        self.course[9][0] = self.course[9][0] + 1
            else:
                if(self.course[9][0]<int(self.shape[0]*0.522)):
                    self.course[9][0] = self.course[9][0] +7
                    self.course[9][1] = self.course[9][1] -7
                else:
                    self.course[9][1] = self.course[9][1] -10
            self.time = self.time + 1
            
        if self.misson_mode == 10:
            cv2.circle(image,self.course[10],10,(160,0,255), -1)
            if(self.course[10][0]>0.6*(self.shape[0])):
                if self.time >= 2*self.reservation_time:
                    self.course[10][0] = self.course[10][0] - 10
                else:
                    self.course[10][0] = self.course[10][0] - 1
            else:
                if(self.course[10][0]>int(self.shape[0]*0.478)):
                    self.course[10][0] = self.course[10][0] -7
                    self.course[10][1] = self.course[10][1] +7
                else:
                    self.course[10][1] = self.course[10][1] + 10
            self.time = self.time + 1
        #함
        if self.misson_mode == 11:
            cv2.circle(image,self.course[11],10,(160,0,255), -1)
            if(self.course[11][1]<int(self.shape[1]*0.4)):
                if self.time >= 2*self.reservation_time:
                    self.course[11][1] = self.course[11][1] + 10
                else:
                    self.course[11][1] = self.course[11][1] + 1
                    
            else:
                if(self.course[11][1]<int(self.shape[1]*0.527)):
                    self.course[11][0] = self.course[11][0] +7
                    self.course[11][1] = self.course[11][1] +7
                else:
                    self.course[11][0] = self.course[11][0] + 10
            self.time = self.time + 1
        if self.misson_mode == 12:
            cv2.circle(image,self.course[12],10,(160,0,255), -1)
            if(self.course[12][1]>0.6*(self.shape[1])):
                if self.time >= 2*self.reservation_time:
                    self.course[12][1] = self.course[12][1] - 10
                else:
                    self.course[12][1] = self.course[12][1] - 1
            else:
                if(self.course[12][1]>int(self.shape[1]*0.473)):
                    self.course[12][0] = self.course[12][0] - 7
                    self.course[12][1] = self.course[12][1] - 7
                else:
                    self.course[12][0] = self.course[12][0] - 10
            self.time = self.time + 1
        if self.misson_mode == 13:
            cv2.circle(image,self.course[13],10,(160,0,255), -1)
            if self.time >= 2*self.reservation_time:
                if(self.course[13][0]>int(self.shape[0]*0.574)):            
                    self.course[13][0] = self.course[13][0] - 10
                else:
                    self.course[13][1] = self.course[13][1] - 10
            else:
                if(self.course[13][0]>int(self.shape[0]*0.574)):            
                    self.course[13][0] = self.course[13][0] - 1
                else:
                    self.course[13][1] = self.course[13][1] - 1
            self.time = self.time + 1
        if self.misson_mode == 14:
            cv2.circle(image,self.course[14],10,(160,0,255), -1)
            if self.time >= 2*self.reservation_time:
                if(self.course[14][1]>int(self.shape[1]*0.576)):            
                    self.course[14][1] = self.course[14][1] - 10
                else:
                    self.course[14][0] = self.course[14][0] + 10
            else:    
                if(self.course[14][1]>int(self.shape[1]*0.576)):            
                    self.course[14][1] = self.course[14][1] - 1
                else:
                    self.course[14][0] = self.course[14][0] + 1  
            self.time = self.time + 1  
        if self.misson_mode == 15:
            cv2.circle(image,self.course[15],10,(160,0,255), -1)
            if self.time >= 2*self.reservation_time:
                if(self.course[15][0]<int(self.shape[0]*0.426)):            
                    self.course[15][0] = self.course[15][0] + 10
                else:
                    self.course[15][1] = self.course[15][1] + 10
            else:
                if(self.course[15][0]<int(self.shape[0]*0.426)):            
                    self.course[15][0] = self.course[15][0] + 1
                else:
                    self.course[15][1] = self.course[15][1] + 1
            self.time = self.time + 1
        if self.misson_mode == 16:
            
            cv2.circle(image,self.course[16],10,(160,0,255), -1)
            if self.time >= 2*self.reservation_time:
                if(self.course[16][1]<int(self.shape[1]*0.424)):            
                    self.course[16][1] = self.course[16][1] + 10
                else:
                    self.course[16][0] = self.course[16][0] - 10
            else:
                if(self.course[16][0]<int(self.shape[0]*0.426)):            
                    self.course[16][0] = self.course[16][0] + 1
                else:
                    self.course[16][1] = self.course[16][1] + 1
            self.time = self.time + 1
    
    def initialize(self,list):
        if len(list)<2:
            list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        if self.course[self.misson_mode][0]<=0 or self.course[self.misson_mode][0]>=self.shape[0]\
            or self.course[self.misson_mode][1]<=0 or self.course[self.misson_mode][1]>=self.shape[1]:  #
            random.shuffle(list)
            self.misson_mode = list.pop()
            self.time = 0
            self.accel = 0
            self.reservation_time = random.randint(1,100)
            self.course= {
            1 : [self.shape[0]-1,int(self.shape[1]*0.424)],
            3 : [int(self.shape[0]*0.574),self.shape[1]-1],
            2 : [self.shape[0]-1,int(self.shape[1]*0.473)],
            4 : [int(self.shape[0]*0.522),self.shape[1]-1],
            5 : [1,int(self.shape[1]*0.576)],
            6 : [1,int(self.shape[1]*0.527)],
            7 : [int(self.shape[0]*0.426),1],
            8 : [int(self.shape[0]*0.478),1], #여기까지 직진
            9 : [1,int(self.shape[1]*0.527)],  #좌회전
            10 : [self.shape[0]-1,int(self.shape[1]*0.473)], #좌회전
            11 : [int(self.shape[0]*0.478),1], #좌회전
            12 : [int(self.shape[0]*0.522),self.shape[1]-1], #좌회전
            13 : [self.shape[0]-1,int(self.shape[1]*0.424)], #우회전
            14 : [int(self.shape[0]*0.574),self.shape[1]-1],  #우회전
            15 : [1,int(self.shape[1]*0.576)], #우회전
            16 : [int(self.shape[0]*0.426),1] #우회전
        }
        return list
    
        
image = cv2.imread("1111.jpg",cv2.IMREAD_UNCHANGED)
image = cv2.pyrUp(image)
timecheak = timer() 
car1 = car( image.shape,reservation_time=30)  #time 1 = 0.1s
car2 = car( image.shape,reservation_time=20)
car3 = car( image.shape,reservation_time=40)
car4 = car( image.shape,reservation_time=70)
car5 = car( image.shape,reservation_time=20)
car6 = car( image.shape,reservation_time=30)
car7 = car( image.shape,reservation_time=50)
car8 = car( image.shape,reservation_time=100)
car9 = car(image.shape,reservation_time=60)
car10 = car(image.shape,reservation_time=50)
car11 = car(image.shape,reservation_time=80)
car12 = car(image.shape,reservation_time=110)
car13 = car(image.shape,reservation_time=90)
car14 = car(image.shape,reservation_time=70)
car15 = car(image.shape,reservation_time=10)
car16 = car(image.shape,reservation_time=0)

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

while cv2.waitKey(50) < 0:  # speed 1기준 50ms 당 1pixel  -> 1초당 20 pixel
    image = cv2.imread("1111.jpg",cv2.IMREAD_UNCHANGED)
    image = cv2.pyrUp(image)
    car1.move_course1(image)
    timecheak.timeflow()
    #시간차로 공 나오게 하기 최초에 나온 순서대로 예약 우선권 부여하면 될듯
    if  timecheak.time > 20:
        car11.move_course1(image)
    if timecheak.time>40:
        car3.move_course1(image)
    if timecheak.time>60:
        car6.move_course1(image)
    if timecheak.time>80:
        car10.move_course1(image)
    if timecheak.time>100:
        car16.move_course1(image)
    if timecheak.time>120:
        car2.move_course1(image)
    if timecheak.time>140:
        car4.move_course1(image)
    if timecheak.time>160:
        car5.move_course1(image)
    if timecheak.time>180:
        car13.move_course1(image)
    if timecheak.time>200:
        car9.move_course1(image)
    if timecheak.time>220:
        car8.move_course1(image)
    if timecheak.time>240:
        car7.move_course1(image)
    if timecheak.time>260:
        car15.move_course1(image)
    list = car1.initialize(list)
    list = car2.initialize(list)
    list = car3.initialize(list)
    list = car4.initialize(list)
    list = car5.initialize(list)
    list = car6.initialize(list)
    list = car7.initialize(list)
    list = car8.initialize(list)
    list = car9.initialize(list)
    list = car10.initialize(list)
    list = car11.initialize(list)
    #list = car12.initialize(list)
    list = car13.initialize(list)
    #list = car14.initialize(list)
    list = car15.initialize(list)
    #list = car16.initialize(list)    
    cv2.imshow('image circle', image)
    
    
cv2.waitKey()
