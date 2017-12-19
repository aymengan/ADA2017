#from pyspark.sql import *
from pyspark import SparkContext,SQLContext
import json 
import numpy as np 
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.ml.clustering import KMeans
import pickle
#import networkx as nx
from tqdm import tqdm
from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql.types import StructField, StringType, IntegerType, StructType

sc = SparkContext.getOrCreate()
sqlContext=SQLContext.getOrCreate(sc)



path = "hdfs:///datasets/dblp-ref/dblp-ref-*.json"

df = sqlContext.read.json(path)

df=df.fillna({'abstract':'', 'title':''})


#all_papers = df.select('id')

#all_papers = all_papers.collect()

#all_papers = list(map(lambda row: row.id, all_papers))

#G=nx.Graph()

#indexes = df.count()

#references = [row.references for row in REFERENCES.rdd.toLocalIterator()]

#references = list(map(lambda row: row.references,df.select('references').collect()))

#references = df.select('references')

#references = references.collect()

#references = list(map(lambda row: row.references, references))

#references_2 = list(map(lambda row: row.references, references.head(indexes)))

#for i in tqdm(range(indexes)):
#	if references[i] is not None:
#		for paper in references[i]:
#			if all_papers.__contains__(paper):
#				G.add_edge(all_papers[i],paper)	

df = df.withColumn('ind', monotonically_increasing_id())


id_to_ind_dict = {}

for row in df.rdd.toLocalIterator():
	id_to_ind_dict[row.id]=row.ind



def create_edge(row,ls):
	refs = row.references
	this_index = row.ind
	if refs is not None:
		for id_ in refs:
			that_index = id_to_ind_dict.get(id_)
			if that_index is not None:
				ls.append((this_index, that_index))

list_tuples = []
list_vertices = []

#df.foreach(lambda row: create_edge(row,list_tuples))

for row in df.rdd.toLocalIterator():
	list_vertices.append(row.ind)
	create_edge(row, list_tuples)

		



data_schema_edge = [StructField('src_id',IntegerType(), False), StructField('dest_id',IntegerType(), False)]
data_schema_vert = [StructField('id',IntegerType(), False)]


final_struc_edge = StructType(fields=data_schema_edge)	
final_struc_vert = StructType(fields=data_schema_vert)

v = sqlContext.createDataFrame(sc.parallelize(list_vertices),final_struc_vert)

v.write.save('id_vertices')

def divide_to_dict_intern(ls, n_step, curr_step, step,my_dict):
	if curr_step == n_step:
		my_dict['e_'+str(curr_step)] = ls
		return my_dict
	elif curr_step < n_step:
		my_dict['e_'+str(curr_step)] = ls[:step]
		return divide_to_dict_intern(ls[step:], n_step, curr_step+1, step, my_dict)
	else:
		return {}

def divide_to_dict(ls, n_step):
	return divide_to_dict_intern(ls, n_step, 1,int(len(ls)/n_step),{})

e_dict = divide_to_dict(list_tuples,4)

e = sqlContext.createDataFrame(sc.parallelize(e_dict.pop('e_1')), final_struc_edge)

for name in e_dict.keys():
	e=e.unionAll(sqlContext.createDataFrame(sc.parallelize(e_dict.pop(name)), final_struc_edge))

e.write.save('refs_edges')