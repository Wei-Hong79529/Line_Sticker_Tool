from rembg import remove
from PIL import Image
import os

def removeBg(input_file_path:str,output_file_path:str):
    input = Image.open(input_file_path)
    output = remove(input)
    output.save(output_file_path)
    print("結束")
    return

def removeMultipleImage(folder_path:str):
    # 讀取資料夾內的所有檔案名稱
    file_names = os.listdir(folder_path)
    # 設定副檔名
    file_extension=".png"
    for file_name in file_names:
        if file_name.endswith(file_extension):
            file_url = folder_path+"\\"+file_name
            removeBg(file_url,file_url)
    print("所有圖片去背完成")
    return

# 圖片資料來源路徑(多)
folder_path = "C:\\Users\\hyt\\Desktop\\Make_Line_Sticker_Tool\\Cut_Single_Image"
# 單張圖片路徑
image_path=""
# 預設多張去背
multipleImage=True

if(multipleImage):
    removeMultipleImage(folder_path)
else:
    removeBg(image_path,image_path)
