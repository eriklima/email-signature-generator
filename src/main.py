import os
import time
from PIL import Image, ImageDraw, ImageFont

fonte_padrao = os.path.join(os.path.dirname(__file__), '../fontes/louis_george_cafe/Louis George Cafe.ttf')
fonte_negrito = os.path.join(os.path.dirname(__file__), '../fontes/louis_george_cafe/Louis George Cafe Bold.ttf')

def main():
    image_base_path = os.path.join(os.path.dirname(__file__), "../images/base_image_01.jpg")
    imagem_base = Image.open(image_base_path)
    
    assinatura = ImageDraw.Draw(imagem_base)

    # print(imagem_base.size)

    fonte = ImageFont.truetype(fonte_padrao, 45)
    assinatura.text((30, 30), "Erik Lima", fill=(0, 0, 0), font=fonte)

    fonte = ImageFont.truetype(fonte_negrito, 20)
    assinatura.text((30, 80), "TECH LEAD", fill=(0, 0, 0), font=fonte)

    fonte = ImageFont.truetype(fonte_negrito, 15)
    assinatura.text((450, 30), "+55 99 9999-9999", fill=(0, 0, 0), font=fonte)

    fonte = ImageFont.truetype(fonte_negrito, 15)
    assinatura.text((450, 50), "erik.lima@topmaster.com.br", fill=(0, 0, 0), font=fonte)

    fonte = ImageFont.truetype(fonte_negrito, 15)
    assinatura.text((450, 70), "www.topmaster.com.br", fill=(0, 0, 0), font=fonte)

    imagem_qrcode_path = os.path.join(os.path.dirname(__file__), '../images/qrcode.png')
    imagem_qrcode = Image.open(imagem_qrcode_path)
    imagem_qrcode = imagem_qrcode.resize((175, 175))

    imagem_base.paste(imagem_qrcode, (250, 30))
    

    # image.show()

    imagem_base.save(os.path.join(os.path.dirname(__file__), "../assinaturas/assinatura.png"))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"{(time.time() - start_time)} segundos ")

