from django.db import models
class autocomplete(models.Model):
    map_no=models.CharField(max_length=200)
    class Meta:
        db_table="ppr_report"
