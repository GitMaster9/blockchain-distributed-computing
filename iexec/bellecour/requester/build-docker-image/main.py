import os
import argparse
import json
from radiation_transport import Simulation

def str2bool(v):
    return v.lower() in ('yes', 'true', 't', '1')

def main():
    IEXEC_OUT = os.getenv('IEXEC_OUT')
    if IEXEC_OUT is None:
        IEXEC_OUT = os.getcwd()

    parser = argparse.ArgumentParser(description="1D Radiation Transport Simulation")

    parser.add_argument("--config_file", type=str, default=None, help="Config file path")
    parser.add_argument("--num_photons", type=int, default=100_000, help="Number of photons to simulate")
    parser.add_argument("--slab_thickness", type=float, default=10.0, help="Thickness of the slab")
    parser.add_argument("--attenuation_coeff", type=float, default=0.1, help="Attenuation coefficient")
    parser.add_argument("--use_scatter", type=str2bool, default=False, help="Use scatter mode")
    parser.add_argument("--p_scatter", type=float, default=0.7, help="Scatter probability")
    parser.add_argument("--p_scatter_reverses_direction", type=float, default=0.5, help="Scatter reverses direction probability")
    parser.add_argument("--seed", type=int, default=1, help="Seed")
    parser.add_argument('--save_full_result', type=str2bool, default=False, help="Save full result file")

    args = parser.parse_args()

    if args.config_file:
        file_path = str(args.config_file)
        print(f"Loading simulation parameters from file: '{file_path}'. Ignoring other parameter arguments.")

        try:
            with open(file_path, "r") as f:
                params = json.load(f)
            
            num_photons = int(params["num_photons"])
            slab_thickness = float(params["slab_thickness"])
            attenuation_coeff = float(params["attenuation_coeff"])
            use_scatter = bool(params["use_scatter"])
            p_scatter = float(params["p_scatter"])
            p_scatter_reverses_direction = float(params["p_scatter_reverses_direction"])
            seed = int(params["seed"])
            save_full_result = bool(params["save_full_result"])
        
        except Exception as e:
            print(f"Error reading parameters from file {file_path}")
            print(e)
            
            computed_json = {'deterministic-output-path': IEXEC_OUT, 'error-message': 'Oops something went wrong'}
            with open(IEXEC_OUT + '/computed.json', 'w') as f:
                json.dump(computed_json, f)
            
            return
    
    else:
        print("No configuration file given. Loading simulation parameters.")

        num_photons = int(args.num_photons)
        slab_thickness = float(args.slab_thickness)
        attenuation_coeff = float(args.attenuation_coeff)
        use_scatter = bool(args.use_scatter)
        p_scatter = float(args.p_scatter)
        p_scatter_reverses_direction = float(args.p_scatter_reverses_direction)
        seed = int(args.seed)
        save_full_result = bool(args.save_full_result)

    simulation = Simulation(num_photons=num_photons,
                            slab_thickness=slab_thickness,
                            attenuation_coeff=attenuation_coeff,
                            use_scatter=use_scatter,
                            p_scatter=p_scatter,
                            p_scatter_reverses_direction=p_scatter_reverses_direction,
                            seed=seed)
    
    simulation.run_simulation()

    output_file_name = IEXEC_OUT + '/output'
    
    simulation.save_to_file(output_file_name, save_full_result)

    computed_json = {'deterministic-output-path': output_file_name + '.h5'}
    with open(IEXEC_OUT + '/computed.json', 'w') as f:
        json.dump(computed_json, f)

if __name__ == "__main__":
    main()