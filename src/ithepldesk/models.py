from django.db import models

# Create your models here.

class Ticket(models.Model):
    pass
    # tck_id
    # title 
    # description
    # issue_date
    # open_date
    # close_date
    # issue_priority
    # assign_to
    # file_attachment
    # issue_by = models.CharField(max_length=150, null=True, blank=True)
    # createdate = models.DateTimeField(auto_now_add=True, editable=False)
    # status

class Solution(models.Model):
    pass
    # sol_id
    # title 
    # description
    # sol_date
    # file_attachement


class StartTask(models.Model):
    pass
    # task_id
    # start_task
    # end_task
    # task_level
    # task_remark



