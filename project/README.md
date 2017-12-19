# Deep into Computer Science publications

# Abstract  

Our prject consists of analyzing the scene of computer science publications and the different interactions within its main communities. The dataset that will be used is the [citation network dataset](https://aminer.org/citation), which contains citation data that is extracted from DBLP(the Digital Bibliography & Library Project). We especially target the [DBLP-Citation-network V10](https://aminer.org/citation) that include 3,079,007 papers and 25,166,994 citation relationships of papers that were published until October 2017 in a JSON-format.  
    
Through this work, we aim to detect the major communities in the scientific publications scene and study the main interactions between these. Moreover, we want to uncover the most influential papers in DBLP using Page-Rank. The Two text-mining measures TFIDF and GloVe vectors will be used to cluster the dataset. An important question to pose here, is whether the obtained clusters match the existing communities in the network. Depending on the graph topology, a more far-reaching challenge that can be tackled, is the ability to classify newcomers by position(Professor, Post-doc, PhD) through the knowledge that we can get on the actual positions of the authors in the network. However this requires an extension of the initial dataset with additional informations such as the actual position or affliation of a certain author. **UPDATE: It turns out from our experience while discovering the data that it is very hard to get the affliation of an author. That is why the last mentionned task will be beyond the scope of our project** 
    
What motivates us the most is the opportunity that we have to get deep insights on the publications in the computer science field and to  discover the present communities in order to unreveal potential concealed patterns. Given the interesting results that we can get, our project might ba a good attraction for the visitors of the Applied Machine Learning Days.


# Research questions  

* Can a collaboration take place between two specific authors?  
* What are the communities of the DBLP network?  
* What are the key words of a certain paper?
* What are the clusters of the network based on the key words? 
* What are the key words of a certain paper?

# Dataset  

As mentioned before, we will mostly use [DBLP-Citation-network V10](https://aminer.org/citation) to get over 3 millions papers published until October 2017. 
The dataset has a "manageable" size of 1.7Gb and contains files in JSON-format for each 1 million paper. Each entry in the file has the following structure:  

| Field Name | Field Type      | Description       | Example                                                                                                                                                           |
|------------|-----------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id         | string          | paper ID             | 013ea675-bb58-42f8-a423-f5534546b2b1                                                                                                                            |
| title      | string          | paper title       | Prediction of consensus binding mode geometries for related chemical series of positive allosteric modulators of adenosine and muscarinic acetylcholine receptors |
| authors    | list of strings | paper authors     | ["Leon A. Sakkal", "Kyle Z. Rajkowski", "Roger S. Armen"]                                                                                                         |
| venue      | string          | paper venue       | Journal of Computational Chemistry                                                                                                                                |
| year       | int             | published year    | 2017                                                                                                                                                              |
| references | list of strings | citing papers' ID | ["4f4f200c-0764-4fef-9718-b8bccf303dba", "aa699fbf-fabe-40e4-bd68-46eaf333f7b1"]                                                                                  |
| abstract   | string          | abstract          | This paper studies ...                                                                                                                                            |  

We would like to enrich the initial dataset by adding valuable informations on the authors, such as, the affiliated university at the time of the publication. For this aim, we will use at a first stage the [DBLP API](http://dblp.uni-trier.de/faq/How+to+use+the+dblp+search+API.html) to search for the affliation component of an author, which is not available for all authors. Therefore we would use other APIs such as [Elsevier Search API](https://dev.elsevier.com/api_docs.html), which can complete the missing affiliation information. Since our computers have a limited computational power, we would like to use the cluster by firstly uploading the dataset and then by using a Spark library named Graphx, which offers a wide range of functions that can be used for the sake of the project.

# A list of internal milestones up until project milestone 2  

Here is a list of internal tasks until the subsequent project milestone:  
*  Data collection: try to add useful informations about the authors such as affiliated university and position.
*  Data cleaning: complete missing informations as much as possible.
*  Data understanding: deepen our perception of the data and check for possible correlations.
*  Getting started with the cluster: upload the dataset and try the first Spark job with Graphx

# A list of internal milestones up until project milestone 3  

Here is a list of internal tasks until the subsequent project milestone:  
*  Complete the data acquisition by completing the missing values and adding more informations on the papers as well as the authors using the DBLP API and the CrossRef API.
*  Complete the graph analysis by computing basic graph measures(Degree Distributions, Clustering Coefficient) and centrality measure(Betweenness Centrality, Page-Rank/HITS).
*  Find the communities in both netwokrs(publications and authors).
*  Extract the keywords of the papers and then apply clustering algorithms based on these
Match the found communities with the clusters.

# Questions for TAa  

* Regarding your experience, do you have any further suggestions or recommendations for our project?  
* Are there any particular algorithms that you can recommend to us regarding community detection and keyword extraction?

We are looking forward for your feedback :)
