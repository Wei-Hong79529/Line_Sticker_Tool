from PIL import Image
import os


def cut_Image(file_url: str, file_name: str, Imageindex: int):
    # 開啟原始圖片
    img = Image.open(file_url)

    # 獲取原始圖片大小
    width, height = img.size

    # 計算每張子圖片的大小
    new_width = width // 2
    new_height = height // 2

# 裁剪並儲存每張子圖片
    for i in range(2):
        for j in range(2):
            # 計算子圖片的左上角和右下角座標
            left = j * new_width
            top = i * new_height
            right = (j + 1) * new_width
            bottom = (i + 1) * new_height

            # 裁剪子圖片
            cropped_img = img.crop((left, top, right, bottom))
            # 貼圖本身
            cropped_img = cropped_img.resize((370, 320))

        # 儲存子圖片
            file_name = file_name.split('.')[0]
            cropped_img.save(f"{file_name}_{Imageindex}_{i}_{j}.png")
    return


# 資料夾路徑
folder_path = "C:\\Users\\hyt\\Desktop\\cutImage\\lineImage"
# 讀取資料夾內的所有檔案名稱
file_names = os.listdir(folder_path)
# 輸出所有檔案名稱
imageIndex = 0
for file_name in file_names:
    if file_name.endswith(".png"):
        file_url = folder_path+"\\"+file_name
        cut_Image(file_url, file_name, imageIndex)
        imageIndex += 1
        
print("所有圖片已裁切完成")
