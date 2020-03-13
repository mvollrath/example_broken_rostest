#!/usr/bin/env python3

import unittest
import rospy
import rostest
import sys

PKG = 'example_broken_rostest'
NAME = 'test_flush'


class TestFlush(unittest.TestCase):
    def test_fail(self):
        self.fail('x')

    def test_pass(self):
        pass


if __name__ == '__main__':
    rospy.init_node(NAME)
    rostest.rosrun(PKG, NAME, TestFlush, sys.argv)
