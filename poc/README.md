# PoC

## Develop

1. Set up the env and install the dependencies

On windows using bash

```bash
cd poc
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

2. Run a worker

```bash
# under the root
python -m poc.worker
```

3. Run the Spark Infra

```bash
# under the root
cd infra/spark
docker compose up -d
```

4. Run a workerflow on the local dev server

```bash
temporal workflow start \
 --task-queue poc-task-queue \
 --type Sparkflow \
 --input '"dummy_job.py"' \
 --namespace data_ingestion_platform
```