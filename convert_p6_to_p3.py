def convert_p6_to_p3(input_path, output_path):
    with open(input_path, 'rb') as f:
        if f.readline().strip() != b'P6':
            raise ValueError("Not a valid P6 file.")
        while True:
            line = f.readline()
            if not line.startswith(b'#'):
                break
        width, height = map(int, line.strip().split())
        maxval = int(f.readline().strip())
        pixel_data = f.read()

    with open(output_path, 'w') as out:
        out.write(f"P3\n{width} {height}\n{maxval}\n")
        for i in range(0, len(pixel_data), 3):
            out.write(f"{pixel_data[i]} {pixel_data[i+1]} {pixel_data[i+2]}\n")

