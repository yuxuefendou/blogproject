from django.db import models
# Create your models here.

# from __future__ import unicode_literals

class ParseStation(models.Model):
    id=models.IntegerField(primary_key=True)
    station=models.CharField(max_length=32,db_index=True)
    alias = models.CharField(max_length=12)
    fullPingyi = models.CharField(max_length=32,db_index=True)
    firstfight = models.CharField(max_length=8,db_index=True)
    def __str__(self):
        return self.station


class KeyWord(models.Model):
    keyword = models.CharField(
        '关键词', max_length=250, primary_key=True, help_text='用户发出的关键词')
    content = models.TextField(
        '内容', null=True, blank=True, help_text='回复给用户的内容')

    pub_date = models.DateTimeField('发表时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('发布状态', default=True)

    def __unicode__(self):
        return self.keyword


    class Meta:
        verbose_name = '关键词'
        verbose_name_plural = verbose_name


class UserStatus(models.Model):
    username=models.CharField(
        '用户编码',max_length=128,primary_key=True,help_text='用户账号'
    )
    content = models.CharField(
        '功能选择项',max_length=128,null=True,help_text='功能选项'
    )



class Express(models.Model):
    name=models.CharField(
        '快递名称',max_length=128,help_text='快递'
    )
    alias=models.CharField(
        '别名',max_length=32,help_text='别名'
    )


class User(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    openid = models.CharField(
        '微信号',max_length=128
    )

    def __str__(self):
        return '微信号:'+self.openid

class UserInfo(models.Model):
    SUBSCIBE= ((1,'已关注'),
               (2,'未关注'),)
    SEX=(
        (1,'男'),
        (2,'女')
    )
    user = models.ForeignKey(User)
    country = models.CharField(
        '国家',max_length=36,blank=True
    )
    language =models.CharField(
        '语言',max_length=36,blank=True
    )
    province = models.CharField(
        '省',max_length=36,blank=True
    )
    city = models.CharField(
        '城市',max_length=128,blank=True
    )
    subscribe=models.IntegerField('是否关注',max_length=1,choices=SUBSCIBE)

    subscribe_time = models.IntegerField(
        '关注时间',blank=True
    )
    groupid=models.IntegerField(
        '分组id',blank=True
    )
    sex=models.IntegerField(
        '性别',max_length=1,choices=SEX
    )
    nickname=models.CharField(
        '别名',max_length=128,blank=True
    )
    remark =models.CharField(
        '公众号运营者对粉丝的备注',max_length=128,blank=True
    )
    headimgurl =models.CharField(
        '用户头像',max_length=128,blank=True
    )
    # tagid_list =models.CharField(
    #     '用户被打上的标签ID列表',max_length=128,blank=True
    # )
    def __str__(self):
        return '别名:'+self.nickname


class UserLocation(models.Model):
    """
    用户地位位置信息上传
    """
    user = models.ForeignKey(User)
    Latitude = models.CharField('纬度',max_length=12)
    Longitude = models.CharField('经度',max_length=12)
    createTime = models.DateTimeField('时间',auto_now_add=True)


class DialogueInformation(models.Model):
    """
    用户对话信息
    """
    pass







