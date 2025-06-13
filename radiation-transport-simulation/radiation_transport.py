import numpy as np
import matplotlib.pyplot as plt
import time

class Simulation:
    def __init__(self, num_photons = 100_000, slab_thickness = 10.0, attenuation_coeff = 0.1, use_scatter = False, p_scatter = 0.7, p_scatter_reverses_direction = 0.5, seed = 1):
        """
        Class that defines a Monte Carlo simulation of 1D photon radiation transport.

        slab thickness [cm]
        
        linear attenuation coefficient (mu) [1/cm]
        """
        self.num_photons = num_photons
        self.slab_thickness = slab_thickness
        self.attenuation_coeff = attenuation_coeff
        self.use_scatter = use_scatter
        self.p_scatter = p_scatter
        self.p_scatter_reverses_direction = p_scatter_reverses_direction
        self.seed = seed

        self.absorbed_positions = []
        self.absorbed_count = 0
        self.absorbed_fraction = 0.0
        
        self.escaped_count = 0
        self.escaped_fraction = 0
        
        self.time_needed = 0.0

    def run_simulation(self, print_debug = False):
        np.random.seed(self.seed)

        absorbed_positions = []
        escaped_count = 0

        if (print_debug):
            print("Simulation parameters:")
            print(f"num_photons={self.num_photons}")
            print(f"slab_thickness={self.slab_thickness}")
            print(f"attenuation_coeff={self.attenuation_coeff}")
            print(f"use_scatter={self.use_scatter}")
            print(f"p_scatter={self.p_scatter}")
            print(f"p_scatter_reverses_direction={self.p_scatter_reverses_direction}")
            print(f"seed={self.seed}")

        start_time = time.perf_counter()

        for _ in range(self.num_photons):
            x = 0.0  # Photon starts at surface
            direction = 1  # +1 = forward, -1 = backward

            while True:
                # Sample a step from exponential distribution
                step = np.random.exponential(1 / self.attenuation_coeff)
                x += direction * step

                # Check if photon escapes
                if x < 0 or x > self.slab_thickness:
                    escaped_count += 1
                    break

                # Decide interaction outcome: scatter or absorb
                if self.use_scatter and np.random.rand() < self.p_scatter:
                    # Scatter: reverse direction randomly
                    direction = 1 if np.random.rand() < self.p_scatter_reverses_direction else -1
                else:
                    # Absorbed at current location
                    absorbed_positions.append(x)
                    break

        end_time = time.perf_counter()

        self.absorbed_positions = absorbed_positions
        self.escaped_count = escaped_count
        self.time_needed = round(end_time - start_time, 2)

        if (print_debug):
            print(f"Time needed: {self.time_needed} s")

        self.absorbed_count = len(self.absorbed_positions)
        self.escaped_count = self.num_photons - self.absorbed_count
        
        self.absorbed_fraction = self.absorbed_count / self.num_photons
        self.escaped_fraction = escaped_count / self.num_photons