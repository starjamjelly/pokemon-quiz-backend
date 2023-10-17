from django.db import models

class TblType(models.Model):
    """
    ポケモンのタイプの情報を格納するテーブル
    """
    class Meta:
        db_table = 'tbl_type'
        app_label = 'models_controller'
        ordering = ['type_id']
    
    type_id      = models.SmallIntegerField(primary_key=True)
    type_name    = models.CharField(max_length=5)
    color_code   = models.CharField(max_length=6)
    created_user = models.CharField(max_length=50)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_user = models.CharField(max_length=50)
    updated_at   = models.DateTimeField(auto_now=True)