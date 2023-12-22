# PoC

## Develop

1. Set up the env and install the dependencies

On windows using bash

```bash
source poc_env/Scripts/activate
pip install -r requirements.txt
```

2. Run a workerflow on the local dev server

```bash
temporal workflow start \
 --task-queue poc-task-queue \
 --type SayHello \
 --input '"555-55-5555"' \
 --namespace data_ingestion_platform
```

3. Run a worker

```bash
python -m poc.worker
```