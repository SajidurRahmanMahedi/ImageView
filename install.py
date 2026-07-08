"""
.desktop
/usr/share/applications/myapp.desktop

application
/usr/bin/myapp

icon.png
/usr/share/icons/hicolor/256x256/apps/myapp.png
"""

# installation script for linux

import os
import shutil
import subprocess

base_dir = os.getcwd()
app_path = os.path.join(base_dir, "dist", "imageview")
icon_path = os.path.join(base_dir, "imageview.png")

app_dist = os.path.join("/", "usr", "bin")
icon_dist = os.path.join("/", "usr", "share", "icons", "hicolor", "256x256", "apps")

app_name = os.path.basename(app_path)
ico = os.path.basename(icon_path)

app_chk = os.path.join(app_dist, app_name)
if not os.path.exists(app_chk):
    try:
        shutil.copy(app_path, app_dist)
        subprocess.run(["chmod", "+x", f"{app_chk}"])
    except Exception as e:
        print(str(e))

ico_chk = os.path.join(icon_dist, ico)
if not os.path.exists(ico_chk):
    try:
        shutil.copy(icon_path, icon_dist)
    except Exception as e:
        print(str(e))

desktop_entry = fr"""[Desktop Entry]
Type=Application
Name={app_name}
Exec={app_chk} %f
Icon={ico_chk}
Terminal=false
MimeType=image/*;
Categories=Graphics;Photography;
"""

entry_path = os.path.join("/", "usr", "share", "applications", f"{app_name}.desktop")

try:
    with open(entry_path, "w") as source:
        source.write(desktop_entry)
        
    subprocess.run(["update-desktop-database", os.path.join("/", "usr", "share", "applications")])

except Exception as e:
    print(str(e))
