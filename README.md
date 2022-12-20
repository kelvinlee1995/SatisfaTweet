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
  - WARN NetworkClient: [Consumer clientId=consumer-spark-kafka-source-75885867-c7ae-4096-a8f9-34f8374feb11-1761795238-driver-0-1, groupId=spark-kafka-source-75885867-c7ae-4096-a8f9-34f8374feb11-1761795238-driver-0] Connection to node -1 (localhost/127.0.0.1:9092) could not be established. Broker may not be available.
  - We tried to search on different sites but none of the solutions worked.
 - Thinking it might be the VM's fault we tried it on our local machine
  - We did everything as instructed but we faced a problem at the Launching step.
    - <img width="960" alt="image" src="https://user-images.githubusercontent.com/71258875/208780378-f74c0db8-5b9f-4012-a2ac-b53d9730a6fa.png">
  - We can see that there is a problem with the Windows version I'm using.
  - We couldn't move any further.
  
 

## Sources

- https://github.com/cloudera/cdh-twitter-example
- https://cloudxlab.com/blog/streaming-twitter-data-using-flume/
- https://medium.com/mcd-unison/twitter-sentiment-analysis-using-zookeeper-kafka-and-pyspark-live-streaming-on-windows-10-in-2022-ada7757097a2
