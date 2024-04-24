#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

class FeladatServer():

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
        self.server = BluetoothMailboxServer()

    def csipog(self):
        self.ev3.speaker.beep()

    def indit(self):
        self.mbox = TextMailbox('greeting', self.server)

        # A szervert a kliens előtt kell elindítanod!
        print('vár a kapcsolódásra...')
        self.server.wait_for_connection()
        print('kapcsolat létrejött!')

        # A szerver vár az első üzent megérkezésére a klienstől,kiírja, majd válaszol neki.
        self.mbox.wait()
        print(self.mbox.read())
        self.mbox.send('Szia neked is!')

        