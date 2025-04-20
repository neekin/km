from django.db import models

class Order(models.Model):
    strCode = models.CharField(max_length=100, verbose_name="票面字符串码") # Renamed strCode to str_code following Python conventions
    serialNumber = models.IntegerField(verbose_name="序列号") # Renamed serialNumber to serial_number
    orders = models.JSONField(verbose_name="订单详情") # Renamed orders to orders_data to avoid conflict with model name, using JSONField
    verTicketCode = models.CharField(max_length=100, verbose_name="验证票码") # Renamed verTicketCode to ver_ticket_code
    playMethod = models.CharField(max_length=50, verbose_name="玩法") # Renamed playMethod to play_method
    drawTime = models.CharField(max_length=50, verbose_name="开奖日期", null=True, blank=True) # Renamed drawTime to draw_time, assuming date only
    lastPeriodData = models.CharField(max_length=255, verbose_name="上期数据", null=True, blank=True) # Renamed lastPeriodData to last_period_data
    storeAddress = models.CharField(max_length=255, verbose_name="门店地址", null=True, blank=True) # Renamed storeAddress to store_address
    machineCode = models.CharField(max_length=50, verbose_name="机器码", null=True, blank=True) # Renamed machineCode to machine_code
    # draw_period = models.CharField(max_length=100, verbose_name="开奖期号", null=True, blank=True) # Renamed drawPeriod to draw_period
    # draw_number = models.CharField(max_length=100, verbose_name="开奖号码", null=True, blank=True) # Renamed drawNumber to draw_number
    salePeriod = models.CharField(max_length=20, verbose_name="销售期号", null=True, blank=True) # Renamed salePeriod to sale_period
    copywriting = models.TextField(verbose_name="文案", null=True, blank=True)
    activity = models.BooleanField(default=False, verbose_name="活动")
    saleTime = models.CharField(max_length=255,verbose_name="销售时间", null=True, blank=True) # Renamed saleTime to sale_time
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格", null=True, blank=True)
    # contribute = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="贡献值", null=True, blank=True)
    machineId = models.CharField(max_length=255, verbose_name="机器ID") # Renamed machineId to machine_id, assuming it should be unique
    create_time = models.DateTimeField(auto_now_add=True) # 创建时间

    def __str__(self):
        return f"订单 {self.serialNumber} - {self.strCode}"

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"