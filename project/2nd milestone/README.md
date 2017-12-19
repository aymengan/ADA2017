# Deep into Computer Science publications

# Abstract  

Our prject consists of analyzing the scene of computer science publications and the different interactions within its main communities. The dataset that will be used is the [citation network dataset](https://aminer.org/citation), which contains citation data that is extracted from DBLP(the Digital Bibliography & Library Project). We especially target the [DBLP-Citation-network V10](https://aminer.org/citation) that include 3,079,007 papers and 25,166,994 citation relationships of papers that were published until October 2017 in a JSON-format.  
    
Through this work, we aim to detect the major communities in the scientific publications scene and study the main interactions between these. Moreover, we want to uncover the most influential papers in DBLP using Page-Rank. The Two text-mining measures TFIDF and GloVe vectors will be used to apply k-Means clustering on the abstract and title of the papers. Last but not least, this work hightlights the evolution of citation over the last decades.
    
What motivates us the most is the opportunity that we have to get deep insights on the publications in the computer science field and to  discover the present communities in order to unreveal potential concealed patterns. Given the interesting results that we can get, our project might ba a good attraction for the visitors of the Applied Machine Learning Days.


# Research questions  

* What are the communities of the DBLP social network of authors?
* Is it possible to cluster the citation network based on term similarity?
* What are the most influential publications in DBLP?
* How is the evolution of citations over the last decades?


# Dataset  

As mentioned before, we will mostly use [DBLP-Citation-network V10](https://aminer.org/citation) to get over 3 millions papers published until October 2017. 
The dataset has a "manageable" size of 4.1Gb and contains files in JSON-format for each 1 million paper. Each entry in the file has the following structure:  

| Field Name | Field Type      | Description       | Example                                                                                                                                                           |
|------------|-----------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id         | string          | paper ID             | 013ea675-bb58-42f8-a423-f5534546b2b1                                                                                                                            |
| title      | string          | paper title       | Prediction of consensus binding mode geometries for related chemical series of positive allosteric modulators of adenosine and muscarinic acetylcholine receptors |
| authors    | list of strings | paper authors     | ["Leon A. Sakkal", "Kyle Z. Rajkowski", "Roger S. Armen"]                                                                                                         |
| venue      | string          | paper venue       | Journal of Computational Chemistry                                                                                                                                |
| year       | int             | published year    | 2017                                                                                                                                                              |
| references | list of strings | citing papers' ID | ["4f4f200c-0764-4fef-9718-b8bccf303dba", "aa699fbf-fabe-40e4-bd68-46eaf333f7b1"]                                                                                  |
| abstract   | string          | abstract          | This paper studies ...                                                                                                                                            |  

We enriched the initial dataset by using the DBLP API and the complete DBLP dataset. In order to fill the missing values we used web scraping over many publisher websites to get the missing abstract of a certain paper.

# A list of internal milestones up until project milestone 2(!!DONE)

Here is a list of internal tasks until the subsequent project milestone:  
*  Data collection: try to add useful informations about the authors such as affiliated university and position.
*  Data cleaning: complete missing informations as much as possible.
*  Data understanding: deepen our perception of the data and check for possible correlations.
*  Getting started with the cluster: upload the dataset and try the first Spark job with Graphx

# A list of internal milestones up until project milestone 3(!!DONE)

Here is a list of internal tasks until the subsequent project milestone:  
*  Complete the data acquisition by completing the missing values and adding more informations on the papers as well as the authors using the DBLP API and the CrossRef API.
*  Complete the graph analysis by computing basic graph measures(Degree Distributions, Clustering Coefficient) and centrality measure(Betweenness Centrality, Page-Rank/HITS).
*  Find the communities in both netwokrs(publications and authors).
*  Extract the keywords of the papers and then apply clustering algorithms based on these
Match the found communities with the clusters.(Out of scope!)  

# Work contributions  
*  Aymen: Web scraping, XML parsing, Data cleaning, Report submission, (!will work on the presentation)  
*  Khalil: Network analysis, Cluste usage, Machine learning algorithms
*  Nour: Web scraping, Data visualization, Final jupyter submission  

# Acknowledgements  
We want to thank Mr. Tiziano Piccardi for his great support in the course of the project. Thanks a lot ! :)

We are looking forward for your feedback :)
