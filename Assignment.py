def read_and_write_file():
    """
    Reads a file, processes its content, and writes a modified version to a new file.
    Handles errors if the file doesn't exist or can't be read.
    """
    try:
        # Prompt the user for the input filename
        input_filename = input("Enter the name of the input file: ")

        # Attempt to open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Process the content: Convert to uppercase and count words
        uppercase_content = content.upper()
        word_count = len(content.split())

        # Prompt the user for the output filename
        output_filename = input("Enter the name of the output file (e.g., output.txt): ")

        # Write the processed content and word count to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(uppercase_content)
            outfile.write(f"\n\nWord Count: {word_count}")

        print(f"Successfully processed the file. Results saved to {output_filename}.")

    except FileNotFoundError:
        print("Error: The file you specified does not exist. Please check the filename and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    read_and_write_file()
