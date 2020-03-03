import random as rand
import time


class Human:
    def __init__(self, sut, money, zp):
        self.sut = sut
        self.money = money
        self.day = 0
        self.hours = 0
        self.zp = zp
        self.isDead = False

    def die(self):
        self.isDead = True
        print('I am so sorry, but i am dead')

    def live(self):
        if not self.isDead:
            self.hours = rand.randint(6, 8)
            print('Now is', self.day, 'day and', self.hours, 'hours\n', 'money:', self.money, 'sut:', self.sut)
            do = rand.randrange(4)
            if do == 0:
                self.money += self.zp
                hours = rand.randint(6, 10)
                self.hours += hours
                sut = rand.randint(30, 50)
                self.sut -= sut
                print('I go to work. Please wait for', hours, 'sec. +', self.zp, 'money; -', sut, 'sut.')
                time.sleep(hours)
            elif do == 1:
                money = rand.randint(100, 500)
                hours = rand.randint(1, 3)
                sut = rand.randint(10, 20)
                self.money -= money
                self.hours += hours
                self.sut -= sut
                print('I go to buy food. Please wait for', hours, 'sec. -', money, 'money; -', sut, 'sut.')
                time.sleep(hours)
            elif do == 2:
                hours = rand.randint(1, 2)
                sut = rand.randint(30, 60)
                self.hours += hours
                self.sut += sut
                print('I go to cook and eat. Please wait for', hours, 'sec. +', sut, 'sut.')
                time.sleep(hours)
            elif do == 3:
                hours = rand.randint(1, 4)
                sut = rand.randint(10, 25)
                self.hours += hours
                self.sut -= sut
                print('I go fun. Please wait for ', hours, ' sec. -', sut, ' sut.')
                time.sleep(hours)
            if self.sut < 0:
                self.die()


Me = Human(100, 3000, 1200)

while not Me.isDead:
    Me.live()
