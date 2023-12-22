from dataclasses import dataclass
from temporalio import activity


@dataclass
class SayHelloParams:
    greeting: str
    name: str


@activity.defn
def say_hello(params: SayHelloParams) -> str:
    return f"{params.greeting}, {params.name}!"
