
import os
import base64
from PIL import Image
from io import BytesIO

from rembg import remove
from django.shortcuts import render
os.environ['OPENBLAS_NUM_THREADS']='1'



def homePage(request):
    image_out = None
    if request.method == "POST":
        if "image" in request.FILES:
            image = request.FILES["image"]
        else:
            image = None
            form = None
            image_out = None
            context={  
                    "form":form,
                    "image" : image,
                    "image_out" : image_out,
                }
            return render(request,'base.html',context)
        
        image = Image.open(image)


        # if image.mode == 'RGBA':
        #     image = image.convert('RGB')

        """ remove bg here """
        image_out = remove(image)
        # image_out = image_out.save()
        
        
        # # Convert the image to a base64-encoded string
        buffered_out = BytesIO()
        image_out.save(buffered_out, format="PNG")
        image_out = base64.b64encode(buffered_out.getvalue()).decode()



        # Convert the image to a base64-encoded string
        buffered = BytesIO()
        try:
            image.save(buffered, format=image.format)
        except ValueError:
            image.save(buffered, format="PNG")
        image = base64.b64encode(buffered.getvalue()).decode()


    else:
        image = None
    form =None
    context={  
        "form":form,
        "image" : image,
        "image_out" : image_out,
    }
    return render(request,'base.html',context)