from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class question(models.Model):
    question = models.TextField(max_length=500)

    def __str__(self):
        return self.question
class option(models.Model):
    option = models.TextField(max_length=500)

    def __str__(self):
        return self.option
class answer(models.Model):
    answer = models.TextField(max_length=500)

    def __str__(self):
        return self.answer

class chatFlow(MPTTModel):
    # step =models.BigIntegerField(default=0)
    questions = models.ForeignKey(question,on_delete=models.CASCADE,null=True,blank=True)
    option = models.ForeignKey(option,on_delete=models.CASCADE,null=True,blank=True)
    answer = models.ForeignKey(answer,on_delete=models.CASCADE,null=True,blank=True)
    is_answer = models.BooleanField(default=False)
    is_option = models.BooleanField(default=False)
    is_question = models.BooleanField(default=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        if self.is_question:
            return str("Question: "+ str(self.questions))
        elif self.is_option :
            return str("Option: "+str(self.option))
        elif self.is_answer :
            return str("Answer: "+ str(self.answer))



