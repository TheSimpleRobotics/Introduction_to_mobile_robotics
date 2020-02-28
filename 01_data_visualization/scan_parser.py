#!/usr/bin/env python

import numpy as np


class ScanParser(object):

    def __init__(self,
    	         angle_min=0.,
    	         angle_increment=0.0174532923847,
    	         angle_max=6.26573181152):
        """
        The default values for the angles coresponds to the specs of
        the turtlebot3 burger laser scan.
        """

        # Internal variables
        self.angle_min = angle_min
        self.angle_increment = angle_increment
        self.angle_max = angle_max
        # Caching
        self._num_scans = None
        self._angles = None

    def ranges_to_cartesian_coordinates(self, ranges):
        angles = self.compute_angles(len(ranges))
        # ToDo: compute x and y coordinate of each laser scan
        x = np.zeros_like(ranges)
        y = np.zeros_like(ranges)
        return x, y

    def ranges_to_polar_coordinates(self, ranges):
        angles = self.compute_angles(len(ranges))
        return angles, ranges

    def compute_angle(self, i):
        angle = self.normalize_angle(self.angle_min + i * self.angle_increment)
        if angle > self.angle_max:
        	msg = """The angle should be less or
        	         equal {} but it is {}""".format(self.angle_max, angle)
        	raise ValueError(msg)
        return angle

    def compute_angles(self, num_scans):
        if num_scans == self._num_scans and self._angles is not None:
            return self._angles
        self._angles = [self.compute_angle(i) for i in range(num_scans)]
        self._num_scans = num_scans
        return self._angles

    def normalize_angle(self, angle):
        # ToDo: normalize angle between -pi and pi
	    return angle
