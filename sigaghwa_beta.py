import cv2
import numpy as np

    

class car():
    def __init__(self,shape,speed = 1):
        self.time = 0
        self.accel = 0
        self.speed = speed
        self.shape = shape
        self.course1 = [shape[0],int(shape[1]*0.424)]
        self.course3 = [int(shape[0]*0.574),shape[1]]
        self.course2 = [shape[0],int(shape[1]*0.473)]
        self.course4 = [int(shape[0]*0.522),shape[1]]
        self.course5 = [0,int(shape[1]*0.576)]
        self.course6 = [0,int(shape[1]*0.527)]
        self.course7 = [int(shape[0]*0.426),0]
        self.course8 = [int(shape[0]*0.478),0] #여기까지 직진
        self.course9 = [0,int(shape[1]*0.527)]  #좌회전
        self.course10= [shape[0],int(shape[1]*0.473)] #좌회전
        self.course11= [int(shape[0]*0.478),0] #좌회전
        self.course12= [int(shape[0]*0.522),shape[1]] #좌회전
        self.course13 = [shape[0],int(shape[1]*0.424)] #우회전
        self.course14 = [int(shape[0]*0.574),shape[1]]  #우회전
        self.course15 = [0,int(shape[1]*0.576)] #우회전
        self.course16 = [int(shape[0]*0.426),0] #우회전
    def move_course1(self,image):
        cv2.circle(image,self.course1,15,(255,255,255), -1)
        self.time = self.time + 1
        self.course1[0] = self.course1[0] - self.speed 
    def move_course3(self,image):
        cv2.circle(image,self.course3,15,(0,0,0), -1)
        self.time = self.time + 1
        self.course3[1] = self.course3[1] - self.speed 
    def move_course2(self,image):
        cv2.circle(image,self.course2,15,(255,0,255), -1)
        self.time = self.time + 1
        self.course2[0] = self.course2[0] - self.speed
    def move_course4(self,image):
        cv2.circle(image,self.course4,15,(0,255,255), -1)
        self.time = self.time + 1
        self.course4[1] = self.course4[1] - self.speed
    def move_course5(self,image):
        cv2.circle(image,self.course5,15,(55,55,55), -1)
        self.time = self.time + 1
        self.course5[0] = self.course5[0] + self.speed
    def move_course6(self,image):
        cv2.circle(image,self.course6,15,(25,150,255), -1)
        self.time = self.time + 1
        self.course6[0] = (self.course6[0] + self.speed)
    def move_course7(self,image):
        cv2.circle(image,self.course7,15,(0,0,0), -1)
        self.time = self.time + 1
        self.course7[1] = self.course7[1] + self.speed 
    def move_course8(self,image):
        cv2.circle(image,self.course8,15,(0,0,0), -1)
        self.time = self.time + 1
        self.course8[1] = self.course8[1] + self.speed
    def move_course9(self,image):
        cv2.circle(image,self.course9,15,(150,80,0), -1)
        if(self.course9[0]<0.4*(self.shape[0])):
            self.course9[0] = self.course9[0] + self.speed
        else:
            if(self.course9[0]<int(self.shape[0]*0.522)):
                self.course9[0] = self.course9[0] +self.speed
                self.course9[1] = self.course9[1] -self.speed
            else:
                self.course9[1] = self.course9[1] -self.speed
        self.time = self.time + 1
        
    def move_course10(self,image):
        cv2.circle(image,self.course10,15,(160,0,255), -1)
        if(self.course10[0]>0.6*(self.shape[0])):
            self.course10[0] = self.course10[0] - self.speed
        else:
            if(self.course10[0]>int(self.shape[0]*0.478)):
                self.course10[0] = self.course10[0] -self.speed
                self.course10[1] = self.course10[1] +self.speed
            else:
                self.course10[1] = self.course10[1] + self.speed
        self.time = self.time + 1
        
    def move_course11(self,image):
        cv2.circle(image,self.course11,15,(160,0,255), -1)
        if(self.course11[1]<0.4*(self.shape[1])):
            self.course11[1] = self.course11[1] + self.speed
        else:
            if(self.course11[1]<int(self.shape[1]*0.527)):
                self.course11[0] = self.course11[0] +self.speed
                self.course11[1] = self.course11[1] +self.speed
            else:
                self.course11[0] = self.course11[0] + self.speed
        self.time = self.time + 1
    def move_course12(self,image):
        cv2.circle(image,self.course12,15,(160,0,255), -1)
        if(self.course12[1]>0.6*(self.shape[1])):
            self.course12[1] = self.course12[1] - self.speed
        else:
            if(self.course12[1]>int(self.shape[1]*0.473)):
                self.course12[0] = self.course12[0] - self.speed
                self.course12[1] = self.course12[1] - self.speed
            else:
                self.course12[0] = self.course12[0] - self.speed
        self.time = self.time + 1
    def move_course13(self,image):
        cv2.circle(image,self.course13,15,(160,0,255), -1)
        if(self.course13[0]>int(self.shape[0]*0.574)):            
            self.course13[0] = self.course13[0] - self.speed
        else:
            self.course13[1] = self.course13[1] - self.speed
    
    def move_course14(self,image):
        cv2.circle(image,self.course14,15,(160,0,255), -1)
        if(self.course14[1]>int(self.shape[1]*0.576)):            
            self.course14[1] = self.course14[1] - self.speed
        else:
            self.course14[0] = self.course14[0] + self.speed
    
    def move_course15(self,image):
        cv2.circle(image,self.course15,15,(160,0,255), -1)
        if(self.course15[0]<int(self.shape[0]*0.426)):            
            self.course15[0] = self.course15[0] + self.speed
        else:
            self.course15[1] = self.course15[1] + self.speed
    
    def move_course16(self,image):
        cv2.circle(image,self.course16,15,(160,0,255), -1)
        if(self.course16[1]<int(self.shape[1]*0.424)):            
            self.course16[1] = self.course16[1] + self.speed
        else:
            self.course16[0] = self.course16[0] - self.speed

image = cv2.imread("1111.jpg",cv2.IMREAD_UNCHANGED)
image = cv2.pyrUp(image)
car1 = car(speed = 3,shape = image.shape)
car2 = car(speed = 4,shape = image.shape)
car3 = car(speed = 1,shape = image.shape)
car4 = car(speed = 2,shape = image.shape)
car5 = car(speed = 2,shape = image.shape)
car6 = car(speed = 3,shape = image.shape)
car7 = car(speed = 2,shape = image.shape)
car8 = car(speed = 4,shape = image.shape)
car9 = car(speed = 4,shape=image.shape)
car10 = car(speed = 7,shape=image.shape)

car11 = car(speed = 3,shape=image.shape)
car12 = car(speed = 4,shape=image.shape)
car13 = car(speed = 8,shape=image.shape)
car14 = car(speed = 2,shape=image.shape)
car15 = car(speed = 6,shape=image.shape)

car16 = car(speed = 4,shape=image.shape)
#image = cv2.imread("1111.jpg",cv2.IMREAD_UNCHANGED

while cv2.waitKey(33) < 0:
    image = cv2.imread("1111.jpg",cv2.IMREAD_UNCHANGED)
    image = cv2.pyrUp(image)
    car2.move_course1(image)    
    car1.move_course2(image)
    car3.move_course3(image)
    car4.move_course4(image)
    car5.move_course5(image)
    car6.move_course6(image)
    car7.move_course7(image)
    car8.move_course8(image)
    car9.move_course9(image)
    car10.move_course10(image)
    car11.move_course11(image)
    
    car12.move_course12(image)
    
    car13.move_course13(image)
    
    car14.move_course14(image)
    
    car15.move_course15(image)
    
    car16.move_course16(image)
    cv2.imshow('image circle', image)
    
    
cv2.waitKey()



    
    
