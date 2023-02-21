import utils
import cv2
import sigaghwa_beta as si
import cross2x2 as crs
import random


def link(car_1):
    car1 = si.car(speed=car_1.speed, shape=image.shape,dly=random.randint(0,2500))
    return car1


def collab(car_1, car1, image):
    if car_1.start == 1 and car_1.direction == 0:
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
    if car_1.start == 4 and car_1.direction == 0:
        car1.move_course4(image)
    if car_1.start == 4 and car_1.direction == 1:
        car1.move_course12(image)
    if car_1.start == 4 and car_1.direction == 2:
        car1.move_course14(image)



if __name__ == '__main__':
    while True:
    image = cv2.imread("background.jpg", cv2.IMREAD_UNCHANGED)
    image = cv2.pyrUp(image)
    slots = crs.slots
    cars = []
    dlys = []
    speeds = []
    objs = [utils.Vehicle(car_no=i, speed=random.randint(5, 10), start=random.randint(1, 4),
                          direction=random.randint(0, 2)) for i in range(1, 11)]
    cobjs = []
    for x in range(0, 10):
        cobjs.append(link(objs[x]))

    for i in cobjs:
        speeds.append(i.speed)
    for i in cobjs:
        dlys.append(i.dly)
    width = [cobjs[0].shape[0], cobjs[0].shape[1]]
    for _ in range((int)((max(dlys) + max(width)) / min(speeds))):
        if cv2.waitKey(33) < 0:
            image = cv2.imread("background.jpg", cv2.IMREAD_UNCHANGED)
            image = cv2.pyrUp(image)
            for i in range(0, 10):
                collab(objs[i], cobjs[i], image)
            cv2.imshow('collab', image)
            crs.time_pass()
v2.waitKey()