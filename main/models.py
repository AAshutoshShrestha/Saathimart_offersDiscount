from django.db import models

STATUS = (
			('Running', 'Running'),
			('Stopped', 'Stopped'),
			('UnComming', 'UnComming'),
			)


class category(models.Model):
    name = models.CharField(max_length=50,null=True)
    icon = models.ImageField(upload_to ='',default='logo.png')
        
    def __str__(self):
        return self.name

class offers_by_category(models.Model):
    category = models.ForeignKey(category, on_delete= models.SET_NULL, null=True) 
    discount = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField( null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.discount



class offers_by_product(models.Model):
    category = models.ForeignKey(category, on_delete= models.SET_NULL, null=True) 
    product_name = models.CharField(max_length=200, null=True)
    MRP = models.CharField(max_length=200, null=True)
    discount_rate = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField( null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product_name
