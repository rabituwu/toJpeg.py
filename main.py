from PIL import Image
import os
import sys

def convert_to_jpg(input_path, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for root, dirs, files in os.walk(input_path):
        for file in files:
            input_file = os.path.join(root, file)
            output_file = os.path.join(output_directory, f"{os.path.splitext(file)[0]}.jpg")

            try:
                image = Image.open(input_file)
                image.save(output_file, "JPEG")
                print(f"Converted: {input_file} -> {output_file}")
            except Exception as e:
                print(f"Conversion failed for {input_file}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python batch_convert_to_jpg.py input_directory output_directory")
    else:
        input_path = sys.argv[1]
        output_directory = sys.argv[2]

        if not os.path.exists(input_path):
            print(f"Input directory '{input_path}' does not exist.")
        else:
            convert_to_jpg(input_path, output_directory)
