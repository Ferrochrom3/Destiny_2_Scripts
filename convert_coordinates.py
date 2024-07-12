def convert_coordinates(x, y, old_res, new_res):
    old_width, old_height = old_res
    new_width, new_height = new_res

    # Calculate scaling factors
    width_scale = new_width / old_width
    height_scale = new_height / old_height

    # Convert coordinates
    new_x = int(x * width_scale)
    new_y = int(y * height_scale)

    return new_x, new_y


old_resolution = (1920, 1080)
new_resolution = (2560, 1440)
x, y = 825, 466  # Coordinates in the old resolution

new_x, new_y = convert_coordinates(x, y, old_resolution, new_resolution)
print(f"Converted coordinates: ({new_x}, {new_y})")
