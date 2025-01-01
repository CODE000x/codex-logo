import cairosvg

def convert_svg_to_png(input_file, output_file, width=None, height=None):
    """
    Converts an SVG file to a PNG file with specified dimensions.
    
    :param input_file: Path to the input SVG file.
    :param output_file: Path to save the output PNG file.
    :param width: Desired width of the output PNG (optional).
    :param height: Desired height of the output PNG (optional).
    """
    try:
        cairosvg.svg2png(
            url=input_file,
            write_to=output_file,
            output_width=width,
            output_height=height
        )
        print(f"Successfully converted {input_file} to {output_file} with dimensions {width}x{height}.")
    except Exception as e:
        print(f"Error converting SVG to PNG: {e}")

# Example usage
input_svg = "cx.svg"
output_png = "cx.png"
desired_width = 800  # Replace with desired width
desired_height = 800  # Replace with desired height

convert_svg_to_png(input_svg, output_png, width=desired_width, height=desired_height)
