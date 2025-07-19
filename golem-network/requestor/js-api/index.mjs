import { Command } from 'commander';
import { TaskExecutor } from "@golem-sdk/task-executor";
import { pinoPrettyLogger } from "@golem-sdk/pino-logger";
import { OfferProposalFilterFactory } from "@golem-sdk/golem-js";

const INPUT_FILE = "/golem/tmp/simulation_config.json";
const OUTPUT_FILE = "/golem/tmp/output.h5";

const DEFAULT_PROVIDERS_WHITELIST = ["riteh-benchmark-1"];

const program = new Command();

program
  .option('--whitelist-disable', 'Disable provider whitelist')
  .option('--whitelist-providers <names>', 'Comma-separated list of whitelisted provider names');

program.parse(process.argv);

const options = program.opts();

const useWhitelist = !(options.whitelistDisable || false);
const whitelistProviders = options.whitelistProviders
  ? options.whitelistProviders.split(',').map(name => name.trim())
  : DEFAULT_PROVIDERS_WHITELIST;

(async () => {
  const executor = await TaskExecutor.create({
    logger: pinoPrettyLogger(),
    api: { key: "try_golem" },
    demand: {
      workload: {
        imageHash: "ed4668e5310aa40ef954637ced7fdb9755e25404a2606a8417c1812a",
      },
    },
    market: {
      rentHours: 0.5,
      pricing: {
        model: "linear",
        maxStartPrice: 0.5,
        maxCpuPerHourPrice: 1.0,
        maxEnvPerHourPrice: 0.5,
      },
      ...(useWhitelist && whitelistProviders.length > 0
        ? { offerProposalFilter: OfferProposalFilterFactory.allowProvidersByName(whitelistProviders) }
        : {}),
    }
  });

  const start_time = performance.now();

  try {
    const result = await executor.run(async (exe) => {
      return (
        await exe
          .beginBatch()
          .uploadFile("./simulation_config.json", INPUT_FILE)
          .run(`python /golem/main.py --config_file ${INPUT_FILE}`)
          .downloadFile(OUTPUT_FILE, "./output.h5")
          .end()
      );
    }, {
      timeout: 3600000 // 60 minutes in milliseconds
    });

    console.log(result[1]?.stdout);
  } catch (error) {
    console.error("Computation failed:", error);
  } finally {
    await executor.shutdown();

    const end_time = performance.now();
    const timeNeeded = (end_time - start_time) / 1000;
    console.log(`Time needed: ${timeNeeded.toFixed(2)} s`);
  }
})();
