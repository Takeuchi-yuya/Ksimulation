import unittest
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from MainCode import Calculation as Cal



class CalcTestCase(unittest.TestCase):
    def  setUp(self):
        print("setUp!!")

    def tearDown(self):
        print("tearDown!!")

    def test_set_force(self):
        test ={
            "name"  : "粒子二つ",
            "in" : [
                {
                "ID"    : "粒子１",
                "pos"   :{"x":0.0,"y":0.0,"z":0.0},
                "vec"   :{"x":0.0,"y":0.0,"z":0.0},
                "Q"     :5.0
                },
                {
                "ID"    : "粒子2",
                "pos"   :{"x":5.0,"y":0.0,"z":0.0},
                "vec"   :{"x":0.0,"y":0.0,"z":0.0},
                "Q"     :10.0
                }

            ],
            "want" :[[-1.7975103574736355*10**10, 0.00000000, 0.00000000],[1.7975103574736355*10**10, 0.00000000, 0.00000000]]
        }
        pl = []
        for IN in test["in"]:
            pl.append(Cal.Calculation(IN["ID"],IN["pos"],IN["vec"],IN["Q"]))
        self.assertTrue(pl[0].set_force(pl) == test["want"][0])
