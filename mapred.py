from pyspark import SparkContext
sc = SparkContext()
import csv


#Reading text file into RDD
rdd=sc.textFile("SM.csv")						

#Mapping the csv file into seperate RDD records
rdd1=rdd.map(lambda line:line.split(","))

#Collecting the last four values of RDD required to calculate profit into another RDD
rdd2=rdd1.map(lambda x:(x[3],x[4],x[5],x[6]))

#Calculating profit for each record in the RDD
rdd3=rdd2.map(lambda x:((int(x[0])*int(x[2]))-(int(x[1])*int(x[3]))))

#Finding the total profit using reduce() function
from operator import add
profit=rdd3.reduce(add)/rdd3.count()

fd=open('ans.csv','r')
row_count=sum(1 for row in fd)
fd.close()

fd=open('ans.csv','a')
wr=csv.writer(fd)
pair=(row_count,profit)
wr.writerow(pair)
fd.close()






