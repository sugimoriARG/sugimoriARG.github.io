import pytesseract
import os
import sys
import re

if len(sys.argv) == 2:
    imgs_dir=sys.argv[1]
    if not (os.path.exists(imgs_dir)):
        print("Se debe pasar un path valido de imagenes como parametro.")
    else:
        pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

        result_file="reglamento.txt"
        
        img_dicts_list=[]
        with open(result_file, 'a+') as file_object: 
            dir_list = os.listdir(imgs_dir)
            dir_list.sort()

            img_file_dict = {}
            for img_file_name in dir_list:
                img_file_id = int(re.findall(r'\d+',img_file_name.split(" ")[0])[-1])
                img_file_dict = {"img_file_id":img_file_id,"img_file_name":img_file_name}
                img_dicts_list.append(img_file_dict)
                
            for img_dict in sorted(img_dicts_list,key = lambda i: i["img_file_id"]):
                img_path=img_dict["img_file_name"]
                filepath = os.path.join(imgs_dir, img_path)
                print("Procesando texto de imagen {} ".format(img_path))
                img_text=pytesseract.image_to_string(filepath)
                file_object.write(img_text)
else:
    print("Se debe pasar un path valido de imagenes como parametro.")
