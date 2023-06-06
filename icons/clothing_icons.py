from PIL import Image, ImageTk
    
    
def show_clothing_icon(clothing_icon_label, icon_path):
    icon_image = Image.open(icon_path)
    icon_image = icon_image.resize((70, 70), Image.ANTIALIAS)
    icon_photo = ImageTk.PhotoImage(icon_image)
    clothing_icon_label.configure(image=icon_photo)
    clothing_icon_label.image = icon_photo
    clothing_icon_label.place(x=400, y=0)
    
