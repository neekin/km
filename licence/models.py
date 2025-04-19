from django.db import models

# Create your models here.
class Licence(models.Model):
    # id = models.AutoField(primary_key=True)
    # licence_content = models.TextField(verbose_name="证书内容",blank=True, null=True) # 证书内容 
    machine_code = models.CharField(max_length=100, blank=True, null=True,verbose_name="机器码") # 机器码
    type = models.IntegerField(default=1,verbose_name='客户端类型',choices=((1, '3D彩'), (2, '六合彩'))) # 证书类型 
    remark = models.TextField(verbose_name="备注") # 证书备注
    enabled = models.IntegerField(default=0, verbose_name='是否启用', choices=((1, '启用'), (0, '停用')))
    status = models.IntegerField(default=0, verbose_name='机器状态', choices=((1, '在线'), (0, '离线'))) # 证书状态
    # expire_time = models.IntegerField(default=365,verbose_name="可用时间天数") #剩余时间天数
    create_time = models.DateTimeField(auto_now_add=True) # 证书创建时间
    update_time = models.DateTimeField(auto_now=True) # 证书更新时间 

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['machine_code', 'type'], name='unique_machine_type')
        ]
    def __str__(self):
        return self.machine_code
    class Meta:
        verbose_name = "打印机"
        verbose_name_plural = "打印机"