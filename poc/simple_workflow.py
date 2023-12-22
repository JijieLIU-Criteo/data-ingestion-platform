from datetime import timedelta
from temporalio import workflow

# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    from poc.activities.say_hello import say_hello, SayHelloParams


@workflow.defn
class SimpleWorkflow:
    @workflow.run
    async def run(self, name: str) -> bool:
        await workflow.execute_activity(
            say_hello, 
            SayHelloParams(greeting="First", name=name),
            schedule_to_close_timeout=timedelta(seconds=5)
        )

        await workflow.execute_activity(
            say_hello, 
            SayHelloParams(greeting="Second", name=name),
            schedule_to_close_timeout=timedelta(seconds=5)
        )

        return True
