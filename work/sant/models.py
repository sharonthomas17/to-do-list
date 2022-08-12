from django.db import models

class Ceo(models.Model):
    ceo_name=models.CharField(max_length=30)

    def __str__(self):
        return self.ceo_name   

class Cmo(models.Model):
    ceo=models.OneToOneField(Ceo,on_delete=models.CASCADE)
    cmo_name=models.CharField(max_length=30)

    def __str__(self):
        return self.cmo_name

class Pro_manager(models.Model):
    cmo_name=models.ForeignKey(Cmo,on_delete=models.CASCADE)
    pro_manager=models.CharField(max_length=30)

    def __str__(self):
        return self.pro_manager

class Developer(models.Model):
    product_manager=models.ForeignKey(Pro_manager,on_delete=models.CASCADE)
    cmo_name=models.ForeignKey(Cmo,on_delete=models.CASCADE)
    dev=models.CharField(max_length=30)    
    def __str__(self):
        return self.dev    


class Sales_manager(models.Model):
    ceo_name=models.ForeignKey(Ceo,on_delete=models.CASCADE)
    sales_manager=models.CharField(max_length=30)
    def __str__(self):
        return self.sales_manager

class Sales_head(models.Model):
    sales_manager=models.ForeignKey(Sales_manager,on_delete=models.CASCADE)
    sales_head=models.CharField(max_length=30)
    def __str__(self):
        return self.sales_head

class Sale_exe(models.Model):
    sales_head=models.ForeignKey(Sales_head,on_delete=models.CASCADE)
    sales_man=models.ForeignKey(Sales_manager,on_delete=models.CASCADE)
    sale_executive=models.CharField(max_length=30)

    def __str__(self):
        return self.sale_executive