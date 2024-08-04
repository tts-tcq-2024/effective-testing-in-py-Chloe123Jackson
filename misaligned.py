import io
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)

def fake_print_colour_map():
    memory_buffer = io.StringIO()
    print_color_map(memory_buffer)
    return memory_buffer.getvalue()


result = print_color_map()
print_output=fake_print_colour_map()
assert (print_output=2)
assert(result == 25)
print("All is well (maybe!)\n")
