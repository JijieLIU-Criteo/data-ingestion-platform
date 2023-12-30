from dataclasses import dataclass
from temporalio import activity


@dataclass
class RunSparkJobParams:
    job_id: str


@activity.defn
def run_spark_job(params: RunSparkJobParams) -> str:
    return f"Spark job: {params.job_id} run!"