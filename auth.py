#!/usr/bin/python
import logging
from os import environ
import bcrypt
import pyotp


def Google_Verify_Result(secret_key, verifycode):
    t = pyotp.TOTP(secret_key)

    result = t.verify(verifycode)  # 对输入验证码进行校验，正确返回True
    msg = result if result is True else False
    return msg


logFilePath = 'auth.log'

Username = environ['username']
Password = environ['password']

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

try:

    with open("psw-file") as f:
        lines = f.read().splitlines()

    for line in lines:
        words = line.split(":")
        if words[0][0] == '#':
            continue
        if words[0] != '' and words[1] != '' and words[0][0] != ' ' and words[1][0] != ' ':
            if words[0] == Username:
                gcode = Password[-6:]
                key = words[2]
                p = Password.split(gcode)[0]
                p = bytes(p, encoding="utf-8")
                passwd = bytes(words[1], encoding="utf-8")
                if bcrypt.hashpw(p, passwd) == passwd and Google_Verify_Result(key, gcode):
                    logging.info("User: " + words[0] + " - Sucessfully Authenticated")
                    exit(0)
                else:
                    logging.warning("User: "+words[0]+" - Password Did not Match")
                    exit(1)

    logging.warning("User: " + Username + " - User not Found")
    exit(1)

except Exception as e:
    logging.critical(str(e))
    exit(1)
