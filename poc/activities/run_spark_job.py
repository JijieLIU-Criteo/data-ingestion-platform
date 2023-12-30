from dataclasses import dataclass
import subprocess
from temporalio import activity


@dataclass
class RunSparkJobParams:
    container_name: str
    job_file: str


@activity.defn
def run_spark_job(params: RunSparkJobParams) -> str:
    command = ["docker", "exec", params.container_name, "spark-submit", params.job_file]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout