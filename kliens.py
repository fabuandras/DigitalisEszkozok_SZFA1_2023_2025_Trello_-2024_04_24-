#!/usr/bin/env pybricks-micropython

# Mielőtt ezt a programot futtatnád párosítsd a két robotot, de ne legyen aktív kapcsolat köztük!
# A szervert a kliens előtt kell elindítanod!

from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# ez a szerver neve akiehz csatlakozni szeretnél
SERVER = 'r1'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('kapcsolódás...')
client.connect(SERVER)
print('Kapcsolat létrejött!')

# A kliens elküldi első üzenetét, majd vár a szerver  válaszára, és kiírja.
mbox.send('Szia!')
mbox.wait()
print(mbox.read())
