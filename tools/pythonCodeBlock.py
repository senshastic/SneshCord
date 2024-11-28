
cool_color_1 = "#ff6f61"  # Coral
cool_color_2 = "#4682b4"  # Muted Blue

keyframes_coral_steelblue = []
for percent in range(201):  # (0.5% steps)
    angle = percent * 1.8  

    gradient = (
        f"background: conic-gradient(from calc(var(--start-angle) + {angle}deg) at 50% 50%, "
        f"{cool_color_1} 0deg, "
        f"{cool_color_2} 90deg, "
        f"{cool_color_1} 180deg, "
        f"{cool_color_2} 270deg, "
        f"{cool_color_1} 360deg);"
    )
    keyframes_coral_steelblue.append(f"    {percent / 2}% {{ {gradient} }}")

# CSS structure
css_code_coral_steelblue = "@keyframes smoothSnakeSpin {\n" + "\n".join(keyframes_coral_steelblue) + "\n}"

# Save to file
file_path_coral_steelblue = "/mnt/data/smooth_snake_spin_keyframes_coral_steelblue.css"
with open(file_path_coral_steelblue, "w") as css_file_coral_steelblue:
    css_file_coral_steelblue.write(css_code_coral_steelblue)

file_path_coral_steelblue



# 30% gold (top/bottom) and 70% blue (sides)
keyframes_30_gold_70_blue = []

# Define the percentage duration 
gold_duration = 30 
blue_duration = 70  

# Calculate individual region durations
top_gold_end = gold_duration / 2 
right_blue_end = top_gold_end + blue_duration / 2  # (next 35%)
bottom_gold_end = right_blue_end + gold_duration / 2  # (next 15%)
left_blue_end = bottom_gold_end + blue_duration / 2  # (final 35%)

for percent in range(201):  # (0.5% steps)
    angle = percent * 1.8  # Each step adds 1.8 degrees
    position = percent / 2  
    # Assign colors
    if position < top_gold_end:  # Top 
        current_color = "gold"
    elif top_gold_end <= position < right_blue_end:  # Right 
        current_color = "blue"
    elif right_blue_end <= position < bottom_gold_end:  # Bottom 
        current_color = "gold"
    else:  # Left 
        current_color = "blue"

    gradient = (
        f"background: conic-gradient(from calc(var(--start-angle) + {angle}deg) at 50% 50%, "
        f"var(--radial-gradient-{current_color}));"
    )
    keyframes_30_gold_70_blue.append(f"    {position}% {{ {gradient} }}")

# CSS structure
css_code_30_gold_70_blue = "@keyframes smoothSnakeSpin {\n" + "\n".join(keyframes_30_gold_70_blue) + "\n}"

# Save to file
file_path_30_gold_70_blue = "/mnt/data/smooth_snake_spin_keyframes_30_gold_70_blue.css"
with open(file_path_30_gold_70_blue, "w") as css_file_30_gold_70_blue:
    css_file_30_gold_70_blue.write(css_code_30_gold_70_blue)

file_path_30_gold_70_blue
