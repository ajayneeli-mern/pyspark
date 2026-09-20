# Local PySpark Docker workspace

## Layout

- `spark-apps/`: PySpark scripts mounted at `/opt/spark-apps` in the master and workers.
- `notebooks/`: Jupyter notebooks mounted at `/home/jovyan/work`.
- `data/input/`: local CSV and Parquet sources mounted at `/opt/data/input` and `/home/jovyan/data/input`.
- `data/output/`: generated job output; only `.gitkeep` is tracked.
- `pdfs/` and `image/`: local reference assets, excluded from Git.

## Start and test

```powershell
docker compose up -d --build
docker compose exec -T bd-pyspark-jupyter spark-submit --master spark://bd-spark-master:7077 /home/jupyter/spark-apps/test.py
```

Save a script in VS Code and submit it again. The bind mounts make it available immediately without rebuilding images or restarting containers.

## UIs

- Spark master: http://localhost:8080
- Worker 1: http://localhost:8081
- Worker 2: http://localhost:8082
- Spark History Server: http://localhost:18081
- Active Job Spark UIs: http://localhost:4040 (and 4041-4045 for concurrent notebooks)
- JupyterLab: http://localhost:8888
- Kafka UI: http://localhost:8085


Run it from the Jupyter terminal with:

 /spark/bin/spark-submit --master spark://bd-spark-master:7077 /home/jupyter/spark-apps/job1.py

 8080 = Cluster UI ðŸ¢

4040 = Application UI ðŸ”¬
## Kafka

- Kafka UI: http://localhost:8085
- Kafka broker for Spark/Jupyter containers: `kafka:9092`
- Kafka broker for host clients: `localhost:9094`

Kafka UI shows topics, messages, consumer groups, and streaming consumer lag.
Start the stack with `docker compose up -d --build`, then create a topic if needed:

```powershell
docker compose exec kafka kafka-topics --bootstrap-server kafka:9092 --create --if-not-exists --topic events --partitions 1 --replication-factor 1
```

Use `kafka:9092` for `kafka.bootstrap.servers` in PySpark Structured Streaming.

## Kafka + Spark Structured Streaming

Live demo: `notebooks/28_kafka_structured_streaming.ipynb` produces a `rate` stream into Kafka topic `streaming_events` and reads it back with `readStream`/`writeStream`.

Run it:

1. Start the stack: `docker compose up -d --build`
2. (Optional, deterministic) create the topic from a terminal:

   ```powershell
   docker compose exec kafka kafka-topics --bootstrap-server kafka:9092 --create --if-not-exists --topic streaming_events --partitions 1 --replication-factor 1
   ```

3. Open JupyterLab http://localhost:8888 and run the notebook. First run needs internet once — Spark downloads the connector jar `org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0`.

What to look at while it streams:

- **Kafka UI** http://localhost:8085 → **Topics** → `streaming_events` → **Messages** shows live records and partitions; **Consumer Groups** → `spark-streaming-demo` shows the running group and lag.
- **Spark UI** http://localhost:4040 → **Streaming** tab shows both queries (producer + consumer), input rates, and batch durations.
- The notebook's `awaitAnyTermination` prints each console batch pulled from Kafka; the last cell stops all streams cleanly.
