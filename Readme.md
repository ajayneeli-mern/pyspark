# Local PySpark Docker workspace

## Layout

- `spark-apps/`: PySpark scripts mounted at `/opt/spark-apps` in the master and workers.
- `notebooks/`: Jupyter notebooks mounted at `/home/jovyan/work`.
- `data/input/`: local CSV and Parquet sources mounted at `/opt/data/input` and `/home/jovyan/data/input`.
- `data/output/`: generated job output; only `.gitkeep` is tracked.
- `pdfs/` and `image/`: local reference assets, excluded from Git.

## Start and test

```powershell
docker compose up -d
docker compose exec -T bd-spark-master /spark/bin/spark-submit --master spark://bd-spark-master:7077 /opt/spark-apps/test.py
```

Save a script in VS Code and submit it again. The bind mounts make it available immediately without rebuilding images or restarting containers.

## UIs

- Spark master: http://localhost:8080
- Worker 1: http://localhost:8081
- Worker 2: http://localhost:8082
- JupyterLab: http://localhost:8888


data move command

docker cp sales.csv bd-pyspark-jupyter-lab:/home/jovyan/work/
