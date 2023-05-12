from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    step =models.BigIntegerField(default=0)
    questions = models.CharField(max_length=200,null=True,blank=True)
    option = models.CharField(max_length=100,null=True,blank=True)
    answer = models.CharField(max_length=200,null=True,blank=True)
    is_answer = models.BooleanField(default=False)
    is_option = models.BooleanField(default=False)
    is_question = models.BooleanField(default=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['step']

    def __str__(self):
        if self.is_question:
            return str("Q: "+self.questions)
        elif self.is_option :
            return str("O: "+self.option)
        elif self.is_answer :
            return str("N: "+self.answer)



