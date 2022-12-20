# SatisfaTweet - HEG Project for Distributed System
Satisfaction search from Tweeter about World Cup 2022

Prerequisite :
- Cloudera HDP Sandbox 2.6.5 (VM)
- Python 3
- Twitter developper account (Elevated)

Goal :
- Gather information from Twitter
- Analyse sentiment from each Tweet
- Send data on HDFS
- Use Apache Hive to visualize results

Difficulties :
- We tried to use Apache Flume to get Stream from Twitter API v2.
- We tried to use Apache Kafka to get data.
  - We configured Producer and Consumer to gather informations.
- We tried to use Spark to analyse results
- We tried to use PySpark to transfer to Spark the data collected through our python script
