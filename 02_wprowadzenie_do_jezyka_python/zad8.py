from file_manager import FileManager
text = FileManager("writeup.txt")
text.read_file()
print("and after update ... ")
text.update_file()
text.read_file()
#cannot import module __main is not a package
#"szedł sobie Maciek przez wieś Kupił jaj pięć Płacił bezgotówkowo Cześć"