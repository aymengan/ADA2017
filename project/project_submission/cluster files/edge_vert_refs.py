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
#import graphframes
#from graphframes import GraphFrame

sc = SparkContext.getOrCreate()
sqlContext=SQLContext.getOrCreate(sc)



path = "hdfs:///datasets/dblp-ref/dblp-ref-*.json"

df = sqlContext.read.json(path)

df=df.fillna({'abstract':'', 'title':''})


def create_edge(row):
	list_edges = []
	authors = row.authors
	if authors is not None:
		for i in range(len(authors)):
			if i+1<len(authors):
				for j in range(i+1,len(authors)):
						list_edges.append(Row(edge = (authors[i] , authors[j])))
	return list_edges
			
result = df.flatMap(lambda row: create_edge(row)).filter(lambda x: x.edge != [])

result = result.toDF()



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

		



data_schema_edge = [StructField('src_id',IntegerType(), True), StructField('dest_id',IntegerType(), True)]
data_schema_vert = [StructField('id',IntegerType(), True)]


final_struc_edge = StructType(fields=data_schema_edge)	
final_struc_vert = StructType(fields=data_schema_vert)

## 

#with open('final_vertices_id.pkl', 'wb') as file:3
#	pickle.dump(list_vertices, file)

#with open('refs_edges.pkl', 'wb') as file:
#	pickle.dump(list_tuples, file)

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

#e_dict = divide_to_dict(list_tuples,4)

#e = sqlContext.createDataFrame(sc.parallelize(e_dict.pop('e_1')), final_struc_edge)

#for name in e_dict.keys():
#	e=e.unionAll(sqlContext.createDataFrame(sc.parallelize(e_dict.pop(name)), final_struc_edge))

#e.write.save('refs_edges_df')

#v = sqlContext.createDataFrame(sc.parallelize(list_vertices),final_struc_vert)





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
#import graphframes
from graphframes import GraphFrame

sc = SparkContext.getOrCreate()
sqlContext=SQLContext.getOrCreate(sc)

vertices = sqlContext.read.parquet('vertices.parquet')
edges = sqlContext.read.parquet('edges.parquet')

graph = GraphFrame(vertices, edges)

comm = graph.labelPropagation(3)



data_schema_edge = [StructField('src',IntegerType(), True), StructField('dst',IntegerType(), True)]
data_schema_vert = [StructField('id',IntegerType(), True)]


final_struc_edge = StructType(fields=data_schema_edge)	
final_struc_vert = StructType(fields=data_schema_vert)


with open ('final_vertices_id.pkl','rb') as file:
	vertices = pickle.load(file)

with open ('refs_edges.pkl','rb') as file:
	edges = pickle.load(file)

vertices = list(map(lambda x: (x,), vertices))

vertices = sc.parallelize(vertices)
vertices = sqlContext.createDataFrame(vertices,final_struc_vert)
#edges = sqlContext.createDataFrame(edges,final_struc_edge)

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

e_dict = divide_to_dict(edges,4)


edges = sc.parallelize(edges)
edges = sqlContext.createDataFrame(edges,final_struc_edge)

e = sqlContext.createDataFrame(sc.parallelize(e_dict.pop('e_1')), final_struc_edge)
e = e.unionAll(sqlContext.createDataFrame(sc.parallelize(e_dict.pop('e_2')), final_struc_edge).unionAll(sqlContext.createDataFrame(sc.parallelize(e_dict.pop('e_3')), final_struc_edge)))
#e = e.unionAll(sqlContext.createDataFrame(sc.parallelize(e_dict.pop('e_4')))

df.registerTempTable('df')

def create_edge(row):
	ls = []
	references = row.references
	if references is not None:
		for ref in references:
			ls.append(Row(src=str(row.id), dst=str(ref)))
	return ls


edges = df.rdd.flatMap(lambda row: create_edge(row))

new_edges = edges.map(lambda row: Row(src=row.src, dst=))



def create_edge_authors(row):
	ls = []
	authors = row.authors
	if authors is not None:
		if len(authors) > 1:
			for auth_1 in authors:
				for auth_2 in authors:
					if auth_2 != auth_1:
						ls.append(Row(src=auth_1, dst=auth_2))
	return ls

edge_authors = df.rdd.flatMap(lambda row: create_edge_authors(row)).toDF()

vertices_authors = edge_authors.rdd.map(lambda row: Row(author=row.src)).toDF().dropDuplicates()

