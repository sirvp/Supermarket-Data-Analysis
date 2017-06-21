# Supermarket-Data-Analysis
Using the transactions in a supermarket to calculate the profit using MapReduction and Apache Spark


Steps:
  
1.  Install Apache Spark and build it using sbt, Maven, etc. This project can be run in standalone mode or in a cluster. 
      In my project, Apache Spark was built on sbt.
      
      https://www.youtube.com/watch?v=eQ0nPdfVfc0.
      
      Familarizing Apache Spark can be done by using video tutorials in YouTube
      
2.  Create databases of transactions for a day. To obtain large number of random transactions, the ranodmize module in python can be used inside a loop.

3.  Calculate profit for the day and append it to a separate database. The profit is calculated by submitting the python file to Spark for faster processing.

4.  Repeat steps 2 and 3 in a loop for the number of days required.

5.  Plot the graph


Reference links:

1.  Apache Spark tutorials: https://www.tutorialspoint.com/apache_spark/

2.  Map Reduction tutorials: https://www.tutorialspoint.com/map_reduce/

3.  Map Reduction tutorials: http://www.journaldev.com/8848/mapreduce-algorithm-example

4.  https://www.dezyre.com/apache-spark-tutorial/spark-tutorial

5.  https://edureka.com
