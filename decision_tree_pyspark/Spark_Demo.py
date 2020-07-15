from pyspark import SparkConf, SparkContext

sc = SparkContext(master = "local", appName = "Spark Demo")

print(sc.textFile("C:\\Users\Chetan\Downloads\deckofcards.txt").first())