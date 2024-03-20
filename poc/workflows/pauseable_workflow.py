from datetime import timedelta
from typing import Optional
from temporalio import workflow

# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    from poc.activities.say_hello import say_hello, SayHelloParams


@workflow.defn
class PauseableWorkflow:
    def __init__(self) -> None:
        self._signal: bool = False
    
    @workflow.run
    async def run(self) -> bool:
        await workflow.execute_activity(
            say_hello, 
            SayHelloParams(greeting="First", name='Alice'),
            schedule_to_close_timeout=timedelta(seconds=5)
        )

        await workflow.wait_condition(lambda: self._signal is True, timeout=timedelta(seconds=10))

        await workflow.execute_activity(
            say_hello, 
            SayHelloParams(greeting="Second", name='Bob'),
            schedule_to_close_timeout=timedelta(seconds=5)
        )

        return True
    
    @workflow.signal(name='continue')
    def continue_signal(self) -> None:
        self._signal = True