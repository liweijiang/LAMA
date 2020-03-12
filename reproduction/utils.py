# Filename: utils.py
# Author: Liwei Jiang
# Description: Helper functions
# Date: 02/25/2020

import jsonlines

def save_data_to_jsonl(output_file, data):
	"""
	Save the data to a jsonl file
	"""
	with jsonlines.open(output_file, mode='w') as writer:
		writer.write(data)
