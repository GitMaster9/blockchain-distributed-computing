import numpy as np
import matplotlib.pyplot as plt
import time

def run_simulation(num_photons = 1_000_000, slab_thickness = 10.0, attenuation_coeff = 0.1, use_scatter = False, p_scatter = 0.7, p_scatter_reverses_direction = 0.5, seed = 1):
    """
    Runs a Monte Carlo 1D radiation transport simulation.

    slab thickness [cm]
    
    linear attenuation coefficient (mu) [1/cm]
    """

    np.random.seed(seed)

    absorbed_positions = []
    escaped_count = 0

    print("Simulation parameters:")
    print(f"num_photons={num_photons}")
    print(f"slab_thickness={slab_thickness}")
    print(f"attenuation_coeff={attenuation_coeff}")
    print(f"use_scatter={use_scatter}")
    print(f"p_scatter={p_scatter}")
    print(f"p_scatter_reverses_direction={p_scatter_reverses_direction}")
    print(f"seed={seed}")

    start_time = time.perf_counter()

    for _ in range(num_photons):
        x = 0.0  # Photon starts at surface
        direction = 1  # +1 = forward, -1 = backward

        while True:
            # Sample a step from exponential distribution
            step = np.random.exponential(1 / attenuation_coeff)
            x += direction * step

            # Check if photon escapes
            if x < 0 or x > slab_thickness:
                escaped_count += 1
                break

            # Decide interaction outcome: scatter or absorb
            if use_scatter and np.random.rand() < p_scatter:
                # Scatter: reverse direction randomly
                direction = 1 if np.random.rand() < p_scatter_reverses_direction else -1
            else:
                # Absorbed at current location
                absorbed_positions.append(x)
                break

    end_time = time.perf_counter()

    time_needed = round(end_time - start_time, 2)

    print(f"Time needed: {time_needed} s")
    
    return absorbed_positions, time_needed

def get_simulation_statistics(num_photons: int, absorbed_positions: list):
    absorbed_count = len(absorbed_positions)
    escaped_count = num_photons - absorbed_count
    
    absorbed_fraction = absorbed_count / num_photons
    escaped_fraction = escaped_count / num_photons

    return absorbed_count, escaped_count, absorbed_fraction, escaped_fraction

num_photons = 1_000_000
absorbed_positions, time_needed = run_simulation(num_photons=num_photons)

absorbed_count, escaped_count, absorbed_fraction, escaped_fraction = get_simulation_statistics(num_photons, absorbed_positions)

print(f"Escaped photons: {escaped_count} ({escaped_fraction:.2%})")
print(f"Absorbed photons: {absorbed_count} ({absorbed_fraction:.2%})")

# Plot absorption depth histogram
plt.hist(absorbed_positions, bins=50, density=True, alpha=0.7, color='steelblue')
plt.title("1D Radiation Transport with Scattering")
plt.xlabel("Depth (cm)")
plt.ylabel("Absorption Probability Density")
plt.grid(True)
plt.show()
