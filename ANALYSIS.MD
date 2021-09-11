# Analytical Report

## We performed three tasks in this Assignment

1. Install HDFS and MapReduce
2. Run the vanilla WordCount program given in the hadoop (tutorial)[https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html] on three datasets.
3. Run a MapReduce based TopN program to find top 100 words across an entire corpus, for different sizes of corpus.

Installation of Hadoop is covered in `README.MD`. So we will only cover the analysis of second and third tasks in this report. 

Showing a sample WordCount Run:

![Sample WordCount Run on 5 Files](https://github.com/SaurabSS/BDSAssg1/blob/main/Screenshots/Screen%20Shot%202021-09-10%20at%205.59.56%20PM.png)

## WordCount in MapReduce Paradigm

We ran the vanilla WordCount program over 5,10,15,20 files of similar sizes to observe the scaling trend followed by MapReduce programs in general.

|Words|Mappers Runtime|Reducers Runtime|
|----|----|
|3000|23328|3019|
|6000|56345|5224|
|9000|86295|5787|
|12000|102106|10909|

## 

|Words|Mappers Runtime|Reducers Runtime|
|----|----|
|80000|28335|3329|
|160000|52939|4773|
|240000|85551|5411|
|320000|110659|11860|