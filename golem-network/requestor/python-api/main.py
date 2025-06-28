import argparse
from datetime import timedelta
import asyncio
from typing import AsyncIterable

from yapapi import Golem, Task, WorkContext
from yapapi.log import enable_default_logger
from yapapi.payload import vm
from yapapi.strategy import MarketStrategy, SCORE_TRUSTED, SCORE_REJECTED

INPUT_FILE = "/golem/tmp/simulation_config.json"
OUTPUT_FILE = "/golem/tmp/output.h5"
TASK_TIMEOUT = timedelta(hours=2)

class CustomProviderStrategy(MarketStrategy):
    def __init__(self, trusted_providers):
        self.trusted_providers = trusted_providers

    async def score_offer(self, offer):
        provider_id = offer.props.get("golem.node.id.name")
        if provider_id in self.trusted_providers:
            return SCORE_TRUSTED
        return SCORE_REJECTED

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
        image_hash="aa05b7d19cd6adbb5e7197b40df82b9aae012eefc3557a83792a8138",
    )

    tasks = [Task(data=None)]

    parser = argparse.ArgumentParser(description="1D Radiation Transport Simulation")
    parser.add_argument("--whitelist_providers", nargs="+", default=[], help="Add provider to whitelist")
    args = parser.parse_args()

    providers = list(args.whitelist_providers)
    if providers:
        print("Using providers from whitelist:")
        print(providers)
        strategy = CustomProviderStrategy(providers)

        async with Golem(budget=1.0, subnet_tag="public", strategy=strategy) as golem:
            async for completed in golem.execute_tasks(worker, tasks, payload=package, timeout=TASK_TIMEOUT):
                print(completed.result.stdout)
    else:
        print("No providers whitelisted. Using any provider...")
        async with Golem(budget=1.0, subnet_tag="public") as golem:
            async for completed in golem.execute_tasks(worker, tasks, payload=package, timeout=TASK_TIMEOUT):
                print(completed.result.stdout)

if __name__ == "__main__":
    enable_default_logger(log_file="requestor.log")

    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_until_complete(task)
