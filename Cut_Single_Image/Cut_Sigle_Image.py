from PIL import Image

def resizeImage(image,imageType:str):
    if(imageType == 'main'):
            return image.resize((240, 240))
    else :  return image.resize((96, 74))

def cut_Image(file_url: str, file_name: str, Imageindex: int,imageType:str):
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
            cropped_img = resizeImage(cropped_img,imageType)

        # 儲存子圖片
            file_name = file_name.split('.')[0]
            cropped_img.save(f"{file_name}_{Imageindex}_{i}_{j}.png")
    return


# 單獨切
#圖片檔案位置
file_url="C:\\Users\\hyt\\Desktop\\Make_Line_Sticker_Tool\\lineImage\\FriendlyHusky.png"
# 圖片檔名
file_name="Image.png"
# 要裁切圖片的類型 main:貼圖的封面 tab:line 聊天室的小圖
image_type="main"
cut_Image(file_url,file_name,0,image_type)
print('ok')