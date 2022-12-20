# SatisfaTweet - HEG Project for Distributed System
Satisfaction search from Tweeter about World Cup 2022

## Prerequisite :
- Cloudera HDP Sandbox 2.6.5 (VM)
- Python 3
- Twitter developper account (Elevated)

## Goal :
- Gather information from Twitter
- Analyse sentiment from each Tweet
- Send data on HDFS
- Use Apache Hive to visualize results

## Difficulties :
- We tried to use Apache Flume to get Stream from Twitter API v2.
- We tried to use Apache Kafka to get data.
  - We configured Producer and Consumer to gather informations.
- We tried to use Spark to analyse results
  - We tried to use PySpark to transfer to Spark the data collected through our python script
### Troubles
- When launching : | flume-ng agent --conf ./conf/ -f conf/flume_logs.conf Dflume.root.logger=DEBUG,console -n TwitterAgent |
  We had an error... from what we found it was due to a .jar file beeing obsolete.
  The exemple provided by the course is almost 10 years old. Thus explaining the obsolete jar file.
  
  We tried to replace it with updated jars, but the new files created dependencies errors.
  
 - While trying to use Kafka, Spark and Pyspark to query the Twitter API streams we faced some difficulties.
    We launched several Web SSH windows to run our Zookeeper server, our Kafka Producer, our Kafka Consumers 
    and finally a window for Pyspark to launch our main.py file.
 

## Sources

- https://github.com/cloudera/cdh-twitter-example
- https://cloudxlab.com/blog/streaming-twitter-data-using-flume/
- https://medium.com/mcd-unison/twitter-sentiment-analysis-using-zookeeper-kafka-and-pyspark-live-streaming-on-windows-10-in-2022-ada7757097a2
