import gdown

# Replace with your actual Google Drive file ID https://drive.google.com/file/d/1tDdLTys9V6rWPF94wz5OPDssY7VkIpYQ/view?usp=sharing
file_id = "1tDdLTys9V6rWPF94wz5OPDssY7VkIpYQ"
url = f"https://drive.google.com/uc?id={file_id}&export=download"

# Output file name
output = "model.pkl"

print("Downloading model file...")
gdown.download(url, output, quiet=False)
print("Download complete!")
