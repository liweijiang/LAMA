# Filename: different_queries.py
# Author: Liwei Jiang
# Description: Code for understanding how the performance of a pretrained language 
# model varies with different ways of querying for a particular fact
# Date: 02/25/2020

import jsonlines
import random
import os.path
from os import path
import utils

NUM_EVIDENCE = 10

def load_relations():
	"""
	Load the relations 
	"""
	relations = {}
	with jsonlines.open('../data/relations.jsonl') as reader:
		for obj in reader:
			relations[obj['relation']] = obj['label']
	return relations


def load_data_with_relation(relation_id):
	"""
	Load the data with the given relation id
	"""
	data = []
	data_path = '../data/TREx/' + relation_id + '.jsonl'
	if path.exists(data_path):
		with jsonlines.open(data_path) as reader:
			for obj in reader:
				random.shuffle(obj['evidences'])
				data.append(obj['evidences'])
		# Filter out the facts with less than NUM_EVIDENCE evidence sentences
		data_filtered = [d[:NUM_EVIDENCE] for d in data if len(d) >= NUM_EVIDENCE]
		# Randomly keep at most 100 facts
		random.shuffle(data_filtered)
		return data_filtered[:100]
	else:
		return None


def reformat_data(data):
	"""
	Reformat the data
	"""
	all_data = []
	for fact in data:
		json = {'subject': fact[0]['sub_surface'], 'object': fact[0]['obj_surface'], 'evidences': []}
		for e in fact:
			json['evidences'].append(e['masked_sentence'])
		all_data.append(json)
	return all_data


def parse_facts():
	"""
	Parse the fact data
	"""
	sampled_facts = []
	relations = load_relations()

	for (id, label) in relations.items():
		data = load_data_with_relation(id)
		if data is not None:
			reformatted_data = reformat_data(data)
			print(len(reformatted_data))
			sampled_facts.extend(reformatted_data)
	utils.save_data_to_jsonl("data/different_queries.jsonl", sampled_facts)
	return sampled_facts


if __name__ == "__main__":
	facts = parse_facts()
