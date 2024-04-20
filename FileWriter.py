class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, data):
        try:
            with open(self.file_name, 'a+') as file:
                file.write(data)
        except Exception as e:
            print(f"Error writing to file: {e}")