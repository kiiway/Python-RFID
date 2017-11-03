#!/usr/bin/env python2

from pirc522 import RFID
rdr = RFID()

while True:
    rdr.wait_for_tag()
    (error, tag_type) = rdr.request()
    if not error:
        print("Badge detecter")
        (error, uid) = rdr.anticoll()
    if not error:
        print("Identifiant de la carte: " + str(uid))

        if not rdr.select_tag(uid):

            if not rdr.card_auth(rdr.auth_a, 10, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):

                print("Lecture du block memoire 10: " + str(rdr.read(10)))

                rdr.stop_crypto()

rdr.cleanup()