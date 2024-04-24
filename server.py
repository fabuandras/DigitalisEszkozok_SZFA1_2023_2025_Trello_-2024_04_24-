#!/usr/bin/env pybricks-micropython

# Mielőtt ezt a programot futtatnád párosítsd a két robotot, de ne legyen aktív kapcsolat köztük! 

# A szervert a kliens előtt kell elindítanod!

from pybricks.messaging import BluetoothMailboxServer, TextMailbox

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# A szervert a kliens előtt kell elindítanod!
print('vár a kapcsolódásra...')
server.wait_for_connection()
print('kapcsolat létrejött!')

# A szerver vár az első üzent megérkezésére a klienstől,kiírja, majd válaszol neki.
mbox.wait()
print(mbox.read())
mbox.send('Szia neked is!')
