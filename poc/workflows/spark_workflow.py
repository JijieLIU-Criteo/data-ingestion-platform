from datetime import timedelta
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from poc.activities.copy_file_to_container import (
        copy_file_to_container,
        CopyFileToContainerParams,
    )
    from poc.activities.run_spark_job import run_spark_job, RunSparkJobParams


@workflow.defn
class Sparkflow:
    @workflow.run
    async def run(self, job_file: str) -> bool:
        container_name = "spark-spark-1"
        container_path_prefix = "/opt/bitnami/spark"
        job_file_prefix = "spark-jobs"

        await workflow.execute_activity(
            copy_file_to_container,
            CopyFileToContainerParams(
                job_file=f"{job_file_prefix}/{job_file}",
                container_name=container_name,
                container_path=f"{container_path_prefix}/{job_file}",
            ),
            schedule_to_close_timeout=timedelta(minutes=1),
        )

        await workflow.execute_activity(
            run_spark_job,
            RunSparkJobParams(container_name=container_name, job_file=job_file),
            schedule_to_close_timeout=timedelta(minutes=1),
        )

        return True
