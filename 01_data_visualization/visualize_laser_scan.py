#!/usr/bin/env python

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