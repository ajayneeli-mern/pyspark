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


Run it from the Jupyter terminal with:

 /spark/bin/spark-submit --master spark://bd-spark-master:7077 /home/jupyter/spark-apps/job1.py

 8080 = Cluster UI 🏢

4040 = Application UI 🔬