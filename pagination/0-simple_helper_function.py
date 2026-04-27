#!/usr/bin/env python3
def index_range(a, b):
	"""returns a tuple of size two containing a start index and an end index
	corresponding to the range of indexes to return in a list for those
	particular pagination parameters.
	"""
	start_index = (a - 1) * b
	end_index = a * b
	return (start_index, end_index)
