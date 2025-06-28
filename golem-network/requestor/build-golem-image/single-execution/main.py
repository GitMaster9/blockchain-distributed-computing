import argparse
import json
from radiation_transport import Simulation

def main():
    parser = argparse.ArgumentParser(description="1D Radiation Transport Simulation")

    parser.add_argument("--config_file", type=str, default=None, help="Config file path")
    parser.add_argument("--num_photons", type=int, default=100_000, help="Number of photons to simulate")
    parser.add_argument("--slab_thickness", type=float, default=10.0, help="Thickness of the slab")
    parser.add_argument("--attenuation_coeff", type=float, default=0.1, help="Attenuation coefficient")
    parser.add_argument("--use_scatter", type=bool, default=False, help="Use scatter mode")
    parser.add_argument("--p_scatter", type=float, default=0.7, help="Scatter probability")
    parser.add_argument("--p_scatter_reverses_direction", type=float, default=0.5, help="Scatter probability")
    parser.add_argument("--seed", type=int, default=1, help="Scatter probability")
    parser.add_argument("--save_full_result", type=bool, default=True, help="Save full result file")

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
    simulation.save_to_file("output", save_full_result)

if __name__ == "__main__":
    main()