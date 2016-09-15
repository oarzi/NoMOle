def create_pic_name(picname, addition, dir):
    name = picname.split('.')
    return dir + name[0] + addition + ".jpg"
