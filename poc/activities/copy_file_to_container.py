from dataclasses import dataclass
import subprocess
from temporalio import activity


@dataclass
class CopyFileToContainerParams:
    job_file: str
    container_name: str
    container_path: str

@activity.defn
def copy_file_to_container(params: CopyFileToContainerParams) -> None:
    command = ["docker", "cp", params.job_file, f"{params.container_name}:{params.container_path}"]
    subprocess.run(command, check=True)