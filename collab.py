import utils
import cv2
import sigaghwa_beta as si
import cross2x2 as crs
import random

def link(car_1):
    car1 = si.car(speed=car_1.speed, shape=image.shape)
    return car1


def collab(car_1,car1,image):
    if car_1.start==1 and car_1.direction==0:
        car1.move_course1(image)
    if car_1.start == 1 and car_1.direction == 1:
        car1.move_course10(image)
    if car_1.start == 1 and car_1.direction == 2:
        car1.move_course13(image)
    if car_1.start == 2 and car_1.direction == 0:
        car1.move_course6(image)
    if car_1.start == 2 and car_1.direction == 1:
        car1.move_course9(image)
    if car_1.start == 2 and car_1.direction == 2:
        car1.move_course15(image)
    if car_1.start == 3 and car_1.direction == 0:
        car1.move_course8(image)
    if car_1.start == 3 and car_1.direction == 1:
        car1.move_course11(image)
    if car_1.start == 3 and car_1.direction == 2:
        car1.move_course16(image)
    if car_1.start==4 and car_1.direction==0:
        car1.move_course4(image)
    if car_1.start==4 and car_1.direction==1:
        car1.move_course12(image)
    if car_1.start==4 and car_1.direction==2:
        car1.move_course14(image)
    # slots0 = list(dict.fromkeys(crs.slots[0].timeline))
    # slots1 = list(dict.fromkeys(crs.slots[1].timeline))
    # slots2 = list(dict.fromkeys(crs.slots[2].timeline))
    # slots3 = list(dict.fromkeys(crs.slots[3].timeline))
    # if car_1.start == 1 and car_1.direction == 0:
    #     if car_1.car_no == slots0[0] and car_1.car_no == slots1[0]:
    #         car1.move_course1(image)
    # if car_1.start == 1 and car_1.direction == 1:
    #     if car_1.car_no == slots1[0] and car_1.car_no == slots2[0] and car_1.car_no == slots3[0]:
    #         car1.move_course10(image)
    # if car_1.start == 1 and car_1.direction == 2:
    #     if car_1.car_no == slots1[0]:
    #         car1.move_course13(image)
    # if car_1.start == 2 and car_1.direction == 0:
    #     if car_1.car_no == slots2[0] and car_1.car_no == slots3[0]:
    #         car1.move_course6(image)
    # if car_1.start == 2 and car_1.direction == 1:
    #     if car_1.car_no == slots0[0] and car_1.car_no == slots1[0] and car_1.car_no == slots0[0]:
    #         car1.move_course9(image)
    # if car_1.start == 2 and car_1.direction == 2:
    #     if car_1.car_no == slots2[0]:
    #         car1.move_course15(image)
    # if car_1.start == 3 and car_1.direction == 0:
    #     if car_1.car_no == slots0[0] and car_1.car_no == slots2[0]:
    #         car1.move_course8(image)
    # if car_1.start == 3 and car_1.direction == 1:
    #     if car_1.car_no == slots0[0] and car_1.car_no == slots1[0] and car_1.car_no == slots3[0]:
    #         car1.move_course11(image)
    # if car_1.start == 3 and car_1.direction == 2:
    #     if car_1.car_no == slots0[0]:
    #         car1.move_course16(image)
    # if car_1.start == 4 and car_1.direction == 0:
    #     if car_1.car_no == slots1[0] and car_1.car_no == slots3[0]:
    #         car1.move_course4(image)
    # if car_1.start == 4 and car_1.direction == 1:
    #     if car_1.car_no == slots0[0] and car_1.car_no == slots2[0] and car_1.car_no == slots3[0]:
    #         car1.move_course12(image)
    # if car_1.start == 4 and car_1.direction == 2:
    #     if car_1.car_no == slots3[0]:
    #         car1.move_course14(image)



if __name__=='__main__':
    image = cv2.imread("background.jpg", cv2.IMREAD_UNCHANGED)
    image = cv2.pyrUp(image)
    slots=crs.slots

    car_1 = utils.Vehicle(car_no=1, speed=random.randint(5,10), start =random.randint(1,4), direction = random.randint(0,2))
    car1=link(car_1)
    crs.reserve_car_by_car(car=car_1)
    car_2 = utils.Vehicle(car_no=2, speed=random.randint(5, 10), start=random.randint(1, 4),
                          direction=random.randint(0, 2))
    car2 = link(car_2)
    car_3 = utils.Vehicle(car_no=3, speed=random.randint(5, 10), start=random.randint(1, 4),
                          direction=random.randint(0, 2))
    car3 = link(car_3)
    car_4 = utils.Vehicle(car_no=4, speed=random.randint(5, 10), start=random.randint(1, 4),
                          direction=random.randint(0, 2))
    car4 = link(car_4)
    car_5 = utils.Vehicle(car_no=5, speed=random.randint(5, 10), start=random.randint(1, 4),
                          direction=random.randint(0, 2))
    car5 = link(car_5)
    car_6 = utils.Vehicle(car_no=6, speed=random.randint(5, 10), start=random.randint(1, 4),
                          direction=random.randint(0, 2))
    car6 = link(car_6)
    car_7 = utils.Vehicle(car_no=7, speed=random.randint(5, 10), start=random.randint(1, 4),
                          direction=random.randint(0, 2))
    car7 = link(car_7)
    car_8 = utils.Vehicle(car_no=8, speed=random.randint(5, 10), start=random.randint(1, 4),
                          direction=random.randint(0, 2))
    car8 = link(car_8)

    while cv2.waitKey(33)<0:
        image = cv2.imread("background.jpg", cv2.IMREAD_UNCHANGED)
        image = cv2.pyrUp(image)
        collab(car_1,car1,image)
        collab(car_2,car2, image)
        collab(car_3, car3, image)
        collab(car_4, car4, image)
        collab(car_5, car5, image)
        collab(car_6, car6, image)
        collab(car_7, car7, image)
        collab(car_8, car8, image)
        cv2.imshow('collab', image)
        crs.time_pass()
    cv2.waitKey()