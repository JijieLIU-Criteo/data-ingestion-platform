from datetime import timedelta
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from poc.activities.run_spark_job import run_spark_job, RunSparkJobParams

@workflow.defn
class Sparkflow:
    @workflow.run
    async def run(self, job_id: str) -> bool:
        await workflow.execute_activity(
            run_spark_job,
            RunSparkJobParams(job_id=job_id),
            schedule_to_close_timeout=timedelta(seconds=5)
        )

        return True