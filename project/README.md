# Deep into Computer Science publications

# Abstract  
Our prject consists of analyzing the scene of computer science publications, its main journals and influential authors.  
The dataset that will be used is the [citation network dataset](https://aminer.org/citation), which contains citation data that is extracted from DBLP and ACM. We especially target the [DBLP-Citation-network V10](https://static.aminer.org/lab-datasets/citation/dblp.v10.zip) that include 3,079,007 papers and 25,166,994 citation relationships from 2010 to 2017 in a JSON-format.  
Through this work, we aim to highlight the major actors of the scientific publications scene over time and show the different social interactions within the network. Moreover, we want to inspect the tendency of co-authoring again with previous collaborators in order to learn more about the collaboration behavior of researchers such as the capacity of an author to collaborate with other colleagues that are new to the research field.  
What motivates us the most is the opportunity that we have to get deep insights on the publications in the computer science field and to see if clichés like needed connections to co-author with well-recognized researchers still hold in the course of the project.   


# Research questions
* What are the most cited authors ?
* Which journal has the most papers ?
* In how many journals do authors publish averagely? 
* Determine the number of collaborations between two authors ?
* Analyze author affiliation(university)?
* How does the network of publications look like ?
* Is the network marked by the presence of hubs or cliques ?

# Dataset
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.
As mentioned before, we will mostly use [DBLP-Citation-network V10](https://static.aminer.org/lab-datasets/citation/dblp.v10.zip) to get over 3 millions papers published between 2010 and 2017. Please find more details on the dataset [here](https://aminer.org/citation).  
The dataset contains files in JSON-format for each 1 million paper. Each entry in the file has the following structure:  

| Field Name | Field Type      | Description       | Example                                                                                                                                                           |
|------------|-----------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id         | string          | paper             | ID013ea675-bb58-42f8-a423-f5534546b2b1                                                                                                                            |
| title      | string          | paper title       | Prediction of consensus binding mode geometries for related chemical series of positive allosteric modulators of adenosine and muscarinic acetylcholine receptors |
| authors    | list of strings | paper authors     | ["Leon A. Sakkal", "Kyle Z. Rajkowski", "Roger S. Armen"]                                                                                                         |
| venue      | string          | paper venue       | Journal of Computational Chemistry                                                                                                                                |
| year       | int             | published year    | 2017                                                                                                                                                              |
| references | list of strings | citing papers' ID | ["4f4f200c-0764-4fef-9718-b8bccf303dba", "aa699fbf-fabe-40e4-bd68-46eaf333f7b1"]                                                                                  |
| abstract   | string          | abstract          | This paper studies ...                                                                                                                                            |  

We would like to enrich the initial dataset by adding valuable informations on the authors, such as, the affiliated university at the time of the publication. For this aim we will use at a first stage the [DBLP API](http://dblp.uni-trier.de/faq/How+to+use+the+dblp+search+API.html) to search for the affliation component of an author, which is not available for all authors. Therefore we would use other APIs such as [Elsevier Search API](https://dev.elsevier.com/api_docs.html), which can complete the missing affiliation information. 

# A list of internal milestones up until project milestone 2
Here is a list of internal tasks until the subsequent project milestone:  
*  Data collection: try to add useful informations about the authors such as affiliated university.
*  Data cleaning: complete missing informations as much as possible.
*  Data understanding: deepen our perception of the data and check for possible correlations.

# Questions for TAa
* Is it possible to use a ready python-module such as scholar.py to extract additional informations from Google Scholar about authors?
