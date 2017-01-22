#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test de los LEDs de la tarjeta F2."""

from rcr.robots.scribbler2.Scribbler2 import Scribbler2
from rcr.utils import Utils

def main():
    """Realiza las pruebas de los LEDs de la tarjeta F2.

    Las pruebas consideran:
        robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
        f2LEDs = robot.getF2LEDs()

        f2LEDs.setBrightLed()

    """
    robot = Scribbler2( "/dev/rfcomm2", 9600, 500 )
    f2LEDs = robot.getF2LEDs()

    print( "setBrightLed: " )
    f2LEDs.setBrightLed( 255 )
    Utils.pause( 2000 )
    print( "setBrightLed: " )
    f2LEDs.setBrightLed( 128 )
    Utils.pause( 2000 )
    print( "setBrightLed: " )
    f2LEDs.setBrightLed( 0 )

    robot.close()


if( __name__ == "__main__" ):
    main()
