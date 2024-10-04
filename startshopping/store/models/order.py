from django.db import models

STATUS_CHOICE = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

class OrderDetail(models.Model):
    user = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    qty = models.PositiveIntegerField(default=1)
    price = models.IntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending', choices=STATUS_CHOICE)