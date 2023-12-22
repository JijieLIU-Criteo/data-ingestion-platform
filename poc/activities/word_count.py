from temporalio import activity
from pyspark.sql import SparkSession


@activity.defn
def word_count() -> int:
    # Create a SparkSession
    spark = SparkSession.builder.appName("WordCount").getOrCreate()

    # Hard-coded input data
    data = ["Hello world", "Hello Spark", "Spark is awesome"]

    # Create an RDD from the input data
    rdd = spark.sparkContext.parallelize(data)

    # Perform word count
    word_counts = rdd.flatMap(lambda line: line.split(" ")) \
                     .map(lambda word: (word, 1)) \
                     .reduceByKey(lambda a, b: a + b)

    # Get the total count
    total_count = word_counts.count()

    # Stop the SparkSession
    spark.stop()

    # Return the result
    return total_count
