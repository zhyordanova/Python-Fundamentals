text = input().split("\\")[-1]

file_name = text.split(".")[0]
file_extension = text.split(".")[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
