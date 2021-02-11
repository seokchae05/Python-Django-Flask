from django.db import models

# Create your models here.


class Fcusers(models.Model):
    username = models.CharField(max_length=64,
                                verbase_name="사용자명")
    password = models.CharField(max_length=64,
                                verbase_name="비밀번호")
    registered_data = models.DataTimField(
        auto_now_add=True, verbase_name="등록시간")

    class Meta:
        db_table = "fastcampus_fcusers"
