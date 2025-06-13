from radiation_transport import Simulation
import matplotlib.pyplot as plt

sim = Simulation()

sim.run_simulation()

print(f"Escaped photons: {sim.escaped_count} ({sim.escaped_fraction:.2%})")
print(f"Absorbed photons: {sim.absorbed_count} ({sim.absorbed_fraction:.2%})")

# Plot absorption depth histogram
plt.hist(sim.absorbed_positions, bins=50, density=True, alpha=0.7, color='steelblue')
plt.title("1D Radiation Transport with Scattering")
plt.xlabel("Depth (cm)")
plt.ylabel("Absorption Probability Density")
plt.grid(True)
plt.show()