from django.db import models
from  django.contrib.auth.models import User
from products.models import Product

from django.utils import timezone

class Comment(models.Model):

    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creted_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return str(self.product) + str(self.user)



