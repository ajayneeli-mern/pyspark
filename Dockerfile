FROM easewithdata/pyspark-jupyter-lab-old:latest

ENV SPARK_HOME=/spark
ENV PATH="${SPARK_HOME}/bin:${PATH}"
