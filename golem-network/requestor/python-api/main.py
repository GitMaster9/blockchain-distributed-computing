import asyncio
from typing import AsyncIterable

from yapapi import Golem, Task, WorkContext
from yapapi.log import enable_default_logger
from yapapi.payload import vm

INPUT_FILE = "/golem/tmp/simulation_config.json"
OUTPUT_FILE = "/golem/tmp/output.h5"

async def worker(context: WorkContext, tasks: AsyncIterable[Task]):
    async for task in tasks:
        script = context.new_script()
        
        script.upload_file("./simulation_config.json", INPUT_FILE)

        script_result = script.run("/bin/sh", "-c", f"python /golem/main.py --config_file {INPUT_FILE}") # RADI

        script.download_file(OUTPUT_FILE, "./output.h5")

        yield script

        task.accept_result(result=await script_result)

async def main():
    package = await vm.repo(
        image_hash="9e7947d1cfed03da910cd80941f3c704c86be35b552527da6e294e43",
    )

    tasks = [Task(data=None)]

    async with Golem(budget=1.0, subnet_tag="public") as golem:
        async for completed in golem.execute_tasks(worker, tasks, payload=package):
            print(completed.result.stdout)

if __name__ == "__main__":
    enable_default_logger(log_file="hello.log")

    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_until_complete(task)
