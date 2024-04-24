#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxClient, TextMailbox


class FeladatKliens():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        # self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        #stopper óra
        self.ido = StopWatch()

        #szerver
        self.client = BluetoothMailboxClient()

    def csipog(self):
        self.ev3.speaker.beep()

    def indit(self, szerverNeve):
        SERVER = szerverNeve
        self.mbox = TextMailbox('greeting', SERVER)

        print('kapcsolódás...')
        self.client.connect(SERVER)
        print('Kapcsolat létrejött!')

        # A kliens elküldi első üzenetét, majd vár a szerver  válaszára, és kiírja.
        self.mbox.send('Szia!')
        self.mbox.wait()
        print(self.mbox.read())

    def start(self):
        SERVER = "r1"
        self.mbox = TextMailbox('greeting', self.client)

        print('kapcsolódás...')
        self.client.connect(SERVER)
        print('Kapcsolat létrejött!')

        # A kliens elküldi első üzenetét, majd vár a szerver  válaszára, és kiírja.
        
        self.mbox.send("Szia")
        self.mbox.wait()
        if (self.mbox.read() == "start"):
            self.robot.straight(100)
            wait(100)
        self.mbox.send("stop")
        
