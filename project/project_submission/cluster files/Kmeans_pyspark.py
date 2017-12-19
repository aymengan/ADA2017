from pyspark.sql import *
from pyspark import SparkContext,SQLContext
import json 
import numpy as np 
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.ml.clustering import KMeans

sc = SparkContext.getOrCreate()
sqlContext=SQLContext.getOrCreate(sc)



path = "hdfs:///datasets/dblp-ref/dblp-ref-*.json"

df = sqlContext.read.json(path)

df=df.fillna({'abstract':'', 'title':''})

df.foreach(lambda row: row.abstract + ' ' + row.title)

df.registerTempTable('df')

temp = sqlContext.sql("SELECT CONCAT(abstract, ' ',  title) FROM df")

temp = temp.withColumnRenamed('_c0', 'text')

tokenizer = Tokenizer(inputCol="text", outputCol="words")

wordsData = tokenizer.transform(temp)

hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures")

featurizedData = hashingTF.transform(wordsData)

idf = IDF(inputCol="rawFeatures", outputCol="features")

idfModel = idf.fit(featurizedData)

rescaledData = idfModel.transform(featurizedData)

km = KMeans().setK(8)

km_model = km.fit(rescaledData)

clustered_data = km_model.transform(rescaledData)

clustered_data.write.save('labeled_km_8')

#clustered_data.registerTempTable('clustered_data')

#counts = sqlContext.sql("SELECT COUNT(*), PREDICTION FROM CLUSTERED_DATA GROUP BY PREDICTION")


## !!!!!!!!!!!!       ADD save for dataframes   	!!!!!!!!!!!!!!!!!!!!!!!!


#rdd = sqlContext.jsonFile(path).toJSON()

#rdd.take(2)

#json.loads()

#rdd.saveAsTextFile('hdfs:///user/cherif/saved')

