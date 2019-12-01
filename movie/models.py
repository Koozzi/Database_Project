from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class realUser(AbstractUser):
    birth = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=45, blank=True, null=True, default='GOLD')
    phone = models.CharField(max_length=45, blank=True, null=True)
    user_rcount = models.IntegerField(blank=True, null=True, default=0)  # Field name made lowercase.
    user_bcount = models.IntegerField(blank=True, null=True, default=0)  # Field name made lowercase.


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class movieinfo(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=45, blank=True, null=True)
    movie_genre = models.CharField(max_length=45, blank=True, null=True)
    movie_open = models.DateField(blank=True, null=True)
    movie_director = models.CharField(max_length=45, blank=True, null=True)
    movie_actor1 = models.CharField(max_length=45, blank=True, null=True)
    movie_actor2 = models.CharField(max_length=45, blank=True, null=True)
    movie_runtime = models.IntegerField(blank=True, null=True)
    movie_age = models.CharField(max_length=45, blank=True, null=True)
    movie_booking_count = models.IntegerField(blank=True, null=True, default=0)
    movie_review_count = models.IntegerField(blank=True, null=True, default=0)
    movie_story = models.TextField(blank=True, null=True)
    movie_playing = models.IntegerField(blank=True, null=True)
    movie_score = models.FloatField(blank=True, null=True, default=0)
    movie_poster = models.ImageField(upload_to="poster")
    def __str__(self):
        return '%s - %s(%s)' % (self.movie_id, self.movie_name, self.movie_playing)

class pjh(models.Model):
    pjh_id = models.AutoField(primary_key=True)
    pjh_name = models.CharField(max_length=45, blank=True, null=True)
    pjh_location = models.CharField(max_length=45, blank=True, null=True)
    pjh_phone = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return '%s'%(self.pjh_name)


class timetable(models.Model):
    id  = models.AutoField(primary_key=True)
    movie_name = models.ForeignKey(movieinfo, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    theater_id = models.IntegerField(blank=True, null=True)
    start_time = models.CharField(max_length=45, blank=True, null=True)
    pjh_id = models.ForeignKey(pjh, on_delete=models.CASCADE)
    def __str__(self):
        return '%s  /  %s  /  %s  /  %s상영  /  %s'%(self.movie_name, self.date, self.pjh_id, self.theater_id, self.start_time)


class booking(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(realUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(movieinfo, on_delete=models.CASCADE)
    pjh = models.ForeignKey(pjh, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    theater = models.IntegerField(blank=True, null=True)
    time = models.CharField(max_length=45, blank=True, null=True)
    seat = models.CharField(max_length=45, blank=True, null=True)
    refund = models.IntegerField(blank=True, null=True, default = 0) # 예매를 하면 0 상태로 저장이 됨. 누군가가 환불을 하면 1 로 바뀜

    def __str__(self):
        return '%s  /  %s  /  %s  /  %s  /  %s  /  %s / %s '%(self.username, self.movie, self.pjh, self.date, self.theater, self.time, self.seat)
# class movieactor(models.Model):
#     movie_name = models.ForeignKey(movieinfo, on_delete=models.CASCADE)
#     movie_actor = models.CharField(max_length=45, blank=True, null=True)
#
#     def __str__(self):
#         return '%s - %s' % (self.movie_name, self.movie_actor)

class review(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(realUser, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(movieinfo, on_delete=models.CASCADE)
    review_grade = models.IntegerField(blank=True, null=True)
    review_text = models.TextField(blank=True, null=True)
    review_time = models.TimeField(blank=True, null=True)
    def __str__(self):
        return '%s %s' % (self.username, self.movie_id)

class seat(models.Model):
    seat_num = models.CharField(max_length=45, blank=True, null=True)
    seat_row = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return '%s' %(self.seat_num)