from PIL import Image
import os

def transBackGround(ImageUrl,targetPath,file_name:str,imageIndex):
    file_name=file_name.split('.')[0]
    img = Image.open(ImageUrl)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
    img.putdata(newData)

    # img=img.resize((96, 74)) 用來縮小圖片尺吋
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    img.save(f"{targetPath}\\{file_name}_{imageIndex}.png")
    return


# 圖片資料來源路徑
folder_path = "C:\\Users\\hyt\\Desktop\\cutImage\\Husky_emoj"
# 轉化背景後圖片路徑
target_folder_path="C:\\Users\\hyt\\Desktop\\cutImage\\Husky_emoj\\transBackgroundFolder"
# 讀取資料夾內的所有檔案名稱
file_names = os.listdir(folder_path)
# 輸出所有檔案名稱
imageIndex = 0
# 設定副檔名
file_extension=".png"
for file_name in file_names:
    if file_name.endswith(file_extension):
        file_url = folder_path+"\\"+file_name
        transBackGround(file_url,target_folder_path, file_name, imageIndex)
        imageIndex += 1
print("所有圖片去背完成")
