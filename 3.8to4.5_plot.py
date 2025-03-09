import matplotlib.pyplot as plt

# Data
lattice_values = [3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.3]
energy_values = [
    -92.9303440359, 
    -93.06875675, 
    -93.17240516, 
    -93.24751110, 
    -93.29928290, 
    -93.33209611, 
    -93.34964046, 
    -93.3549433418, 
    -93.35061747, 
    -93.33935676, 
    -93.30515657
]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(lattice_values, energy_values, marker='o', linestyle='-', color='b', label='Lattice Energy')

# Add labels and title
plt.title('Lattice Energy vs. Lattice Value', fontsize=14)
plt.xlabel('Lattice Value', fontsize=12)
plt.ylabel('Energy (Ry)', fontsize=12)
plt.xticks(lattice_values)
plt.grid(True)

# Add a horizontal line for the specified energy value
energy_reference = -93.35494334
plt.axhline(y=energy_reference, color='r', linestyle='--', label='Energy Reference Line (-93.35494334 Ry)')

# Adding legend
plt.legend()

# Save the plot to the current directory
plt.tight_layout()
plt.savefig('lattice_energy_plot_with_reference.png')  # Saves the plot as a PNG file
