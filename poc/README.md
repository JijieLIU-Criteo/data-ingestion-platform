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
python -m poc.worker
```


3. Run a workerflow on the local dev server

```bash
temporal workflow start \
 --task-queue poc-task-queue \
 --type SimpleWorkflow \
 --input '"temporal"' \
 --namespace data_ingestion_platform
```