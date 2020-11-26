class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name
    def read_file(self):
        k = open("writeup.txt", "r")
        print(k.read())
    def update_file(self):
        f = open(self.file_name, 'a', encoding='utf-8')
        f.write("\nFile updated")
        f.close()
