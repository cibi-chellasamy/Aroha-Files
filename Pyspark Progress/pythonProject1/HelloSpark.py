import sys
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import *
from lib.logger import Log4J
from lib.utils import get_spark_app_config,load_surver_df
from lib.utils import get_spark_app_config

# if __name__ == "__main__":
#     # Load configuration for Spark
#     conf = get_spark_app_config()
#
#     # Initialize Spark session with configurations
#     spark = SparkSession.builder.config(conf=conf).getOrCreate()
#
#     # Use Spark's built-in logger
#     logger = spark._jvm.org.apache.log4j.LogManager.getLogger(__name__)
#
#     # Log start message
#     logger.info("Starting HelloSpark")
#
#     # Display current Spark configuration details
#     conf_out = spark.sparkContext.getConf()
#     logger.info(conf_out.toDebugString())
#
#     # Log finish message
#     logger.info("Finished HelloSpark")
#
#     # Stop the Spark session
#     #spark.stop()
if __name__ == "__main__":
    conf = get_spark_app_config()

    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    logger = spark._jvm.org.apache.log4j.LogManager.getLogger(__name__)

    logger.setLevel(spark._jvm.org.apache.log4j.Level.INFO)

    if len(sys.argv) != 2:
        logger.error("usage:HelloSpark<filename>")
        sys.exit(-1)
    logger.info("Starting HelloSpark")

    #conf_out = spark.sparkContext.getConf()
    #logger.info(conf_out.toDebugString())
    survey_df = load_surver_df(spark,sys.argv[1])
    survey_df.show()
    logger.info("Finished HelloSpark")

    spark.stop()