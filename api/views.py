from rest_framework.decorators import api_view
import base64
from django.core.files.base import ContentFile
from api import models
from rest_framework.response import Response

@api_view(["POST"])
def img_saver(request):

    data = request.data.get("image");
    img64 = data.split(";base64,")[1]
    deocded_file = base64.b64decode(img64)
    img_file = ContentFile(deocded_file, name="digit.png")
    obj = models.Digit.objects.create(image=img_file)
    return Response({"response": obj.classification})

