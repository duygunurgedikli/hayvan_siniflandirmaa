import os

translate = {
    "cane": "dog", "gatto": "cat", "elefante": "elephant",
    "cavallo": "horse", "farfalla": "butterfly", "gallina": "chicken",
    "mucca": "cow", "pecora": "sheep", "scoiattolo": "squirrel", "ragno": "spider"
}

path = "raw-img"

for folder in os.listdir(path):
    folder_path = os.path.join(path, folder)
    if os.path.isdir(folder_path) and folder in translate:
        new_folder_name = translate[folder]
        new_folder_path = os.path.join(path, new_folder_name)
        os.rename(folder_path, new_folder_path)
        print(f"{folder} klasörü → {new_folder_name} olarak değiştirildi.")
