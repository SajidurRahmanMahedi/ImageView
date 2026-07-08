windows
pyinstaller --noconfirm --onedir --windowed --icon "icon.ico" --name "ImageView" --version-file "version.txt" main.py

linux
pyinstaller --noconfirm --onefile --windowed --name "imageview" main.py
