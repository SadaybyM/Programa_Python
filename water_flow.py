def water_column_height(tower_height, tank_height):
    """Calculate and return the height of a water column."""
    return tower_height + (3 * tank_height) / 4


def pressure_gain_from_water_height(height):
    """Calculate and return the pressure gain from water height."""
    density = 998.2  # kg/m³
    gravity = 9.80665  # m/s²
    return (density * gravity * height) / 1000


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate and return the pressure loss from a pipe."""
    density = 998.2  # kg/m³
    return (-friction_factor * pipe_length * density * (fluid_velocity ** 2)) / (2000 * pipe_diameter)
