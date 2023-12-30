import asyncio
import concurrent.futures
from temporalio.client import Client
from temporalio.worker import Worker


from poc.activities.copy_file_to_container import copy_file_to_container
from poc.activities.run_spark_job import run_spark_job
from poc.activities.say_hello import say_hello

from poc.workflows.simple_workflow import SimpleWorkflow
from poc.workflows.spark_workflow import Sparkflow




async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233", namespace="data_ingestion_platform")

    # Run the worker
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as activity_executor:
        worker = Worker(
            client,
            task_queue="poc-task-queue",
            workflows=[SimpleWorkflow, Sparkflow],
            activities=[say_hello, copy_file_to_container, run_spark_job],
            activity_executor=activity_executor,
        )
        print("Starting worker...")
        await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
