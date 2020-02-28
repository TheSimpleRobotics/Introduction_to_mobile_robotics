#!/usr/bin/env python
__copyright__ = """
Copyright (c) 2020 Tananaev Denis, Tananaev Vladislav
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom
the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall
be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import json
import numpy as np
import matplotlib.pyplot as plt
from scan_parser import ScanParser

data_filename = "../00_data/room_walk.json"

def visualize_range(ax, raw_ranges, cartesian_ranges):
    ax[0].clear()
    ax[0].set_title("Raw range data")
    ax[0].plot(raw_ranges)
    ax[1].clear()
    ax[1].set_title("Euclidean space")
    ax[1].scatter(*cartesian_ranges, 1)
    ax[1].axis('equal')
    plt.pause(0.1)
    plt.show()

def load_data(data_filename):
	with open(data_filename, 'r') as f:
		data = json.load(f)
		return data


def visualize_laser_scans(data_filename):
	data = load_data(data_filename)
	scan_parser = ScanParser()

	# Display range
	plt.ion()  # interactive display
	fig, ax = plt.subplots(2, 1, False)
	for timestamp in data:
		raw_ranges = np.asarray(data[timestamp]["scan"])
		cartesian_ranges = np.asarray(scan_parser.ranges_to_cartesian_coordinates(raw_ranges))
		visualize_range(ax, raw_ranges, cartesian_ranges)



if __name__ == "__main__":
	visualize_laser_scans(data_filename)