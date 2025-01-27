EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s²
WATER_DENSITY = 998.2  # kg/m³
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pa·s

def water_column_height(tower_height, tank_height):
    """Calculate and return the height of a water column."""
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    """Calculate and return the pressure gain from water height."""
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate and return the pressure loss from a pipe."""
    return (-friction_factor * pipe_length * WATER_DENSITY * (fluid_velocity ** 2)) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculate and return the pressure loss due to fittings."""
    return (-0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculate and return the Reynolds number."""
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculate and return the pressure loss from pipe reduction."""
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return (-k * WATER_DENSITY * (fluid_velocity ** 2)) / 2000

def kpa_to_psi(kpa):
    """Convert kilopascals to pounds per square inch."""
    return kpa * 0.145038

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = 0.28687  # PVC Schedule 80 inner diameter in meters
    friction = 0.013  # PVC Schedule 80 friction factor
    velocity = 1.65  # Supply velocity in m/s

    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, 0.048692)  # HDPE SDR11 inner diameter
    pressure += loss

    diameter = 0.048692
    friction = 0.018
    velocity = 1.75

    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    psi_pressure = kpa_to_psi(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {psi_pressure:.1f} psi")

if __name__ == "__main__":
    main()