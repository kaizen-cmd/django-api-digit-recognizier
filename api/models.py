from django.db import models
from PIL import Image
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
from django.conf import settings
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Create your models here.

class Digit(models.Model):

    image = models.ImageField(upload_to="digits")
    classification = models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        img = Image.open(self.image)
        img_array = image.img_to_array(img)
        new_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        dim = (28, 28)
        resized = cv2.resize(new_img, dim, interpolation=cv2.INTER_AREA)
        ready = np.expand_dims(resized, axis=2)
        ready = np.expand_dims(ready, axis=0)
        try:
            file_model = settings.BASE_DIR / "CNN_model.h5"
            graph = tf.compat.v1.get_default_graph()

            with graph.as_default():
                model = load_model(file_model)
                pred = np.argmax(model.predict(ready))
                self.classification = str(pred)
        except:
            self.classification = "Failed to classify"

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)

