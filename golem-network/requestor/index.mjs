import { Command } from 'commander';
import { TaskExecutor } from "@golem-sdk/task-executor";
import { pinoPrettyLogger } from "@golem-sdk/pino-logger";
import { OfferProposalFilterFactory } from "@golem-sdk/golem-js";

const INPUT_FILE = "/golem/tmp/input.txt";
const OUTPUT_FILE = "/golem/tmp/output.txt";

const DEFAULT_PROVIDERS_WHITELIST = ["testnet-c1-0", "testnet-c1-1"];

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
        imageHash: "18901b10914cabab1d0ca3495b3dfeac182c28e9d90651df682233f1",
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

  try {
    const result = await executor.run(async (exe) => {
      return (
        await exe
          .beginBatch()
          .uploadFile("./input.txt", INPUT_FILE)
          .run(`python /golem/main.py ${INPUT_FILE} > ${OUTPUT_FILE}`)
          .run(`cat ${OUTPUT_FILE}`)
          .downloadFile(OUTPUT_FILE, "./output.txt")
          .end()
      );
    });

    console.log(result[2]?.stdout);
  } catch (error) {
    console.error("Computation failed:", error);
  } finally {
    await executor.shutdown();
  }
})();
