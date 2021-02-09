from django.db import models
from authapp.models import User

from mainapp.models import Product

# class BasketQuerySet(models.QuerySet):
#     def delete(self):
#         for object in self:
#             object.product.quantity += object.quantity
#             object.product.save()
#         # Для того чтобы дальше опять по стандарту delete()  работал опять его "переопределяем"
#         super().delete()

class Basket(models.Model):

    # objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'
# Эти методы взяли с обработчика и вставили модель в его методы, чтобы сократить
# логику в  обработчике и содержать их в модели

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super().delete()

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - self.pk.quantity
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super().save(*args, **kwargs)


