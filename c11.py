import os
import shutil

source="Downloads/C102_assets-main/C102_assets-main/feather.jfif"
print("before copying file ")
print(os.listdir (source))
destination="Downloads/C102_assets-main/C102_assets-main/copy_feather.jfif"
dest=shutil.copy(source,destination)
print("after copying file ")
print(os.listdir (source))

