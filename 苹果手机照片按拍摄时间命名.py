import os  
from PIL import Image  
import piexif  
import shutil 


def get_exif_date(image_path):  
    try:  
        img = Image.open(image_path)  
        exif_data = img.getexif()  
        date_str = exif_data.get(0x9003)  # exif tag for date/time taken  
        img.close()
        return date_str  
    except (AttributeError, FileNotFoundError):  
        img.close()
        return None
    
    
def rename_images(directory):  
    count = 0  
    for filename in os.listdir(directory):  
        if filename.endswith(".jpg") or filename.endswith(".JPG"):  
            img_path = os.path.join(directory, filename)  
            date_str =get_exif_date(img_path)
                
            if date_str:
                # Extract the date portion from the file name  
                date_parts = date_str.split(' ')[0].split(':')  
                year = date_parts[0]  
                month = date_parts[1]  
                day = date_parts[2]  
            
                time_parts=date_str.split(' ')[1].split(':')
                hh=time_parts[0]
                mm=time_parts[1]
                ss=time_parts[2]
                # Extract the index from the file name (after the '_')  
                index = int(filename.split('_')[-1].split('.')[0])  
                new_filename = f"IMG_{year}_{month}_{day}_{hh}_{mm}_{ss}_{index}.JPG"  
            else:
                new_filename = filename 
            
                
            new_path = os.path.join(directory+"/pic_new/", new_filename)  
            shutil.copy2(img_path, new_path)
            print(f"Renamed {filename} to {new_filename}")  
            count += 1  
    print(f"Renamed {count} files.")  
  
# 使用时请替换为实际的文件夹路径  
directory = "E:/2015年 照片/PIC/"  
rename_images(directory)