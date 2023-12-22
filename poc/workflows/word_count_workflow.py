from datetime import timedelta
from temporalio import workflow

@workflow.defn
class WorCountflow:
    @workflow.run
    async def run(self) -> bool:
        await workflow.execute_activity(
            word_count,
            schedule_to_close_timeout=timedelta(seconds=5)
        )

        return True