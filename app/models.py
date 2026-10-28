# This is an auto-generated Django model module.
# python manage.py inspectdb --database=app_db > models.py
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'account_type'


class ActionType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'action_type'


class AppUser(models.Model):
    id = models.UUIDField(primary_key=True)
    display_name = models.CharField(max_length=200)
    username = models.CharField(unique=True, max_length=100)
    password_hash = models.CharField(max_length=255)
    profile_picture_hash = models.CharField(max_length=64, blank=True, null=True)
    account_type = models.ForeignKey(AccountType, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'app_user'


class IconType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'icon_type'


class Report(models.Model):
    id = models.UUIDField(primary_key=True)
    gps_coords = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(AppUser, models.DO_NOTHING)
    category = models.ForeignKey('ReportCategory', models.DO_NOTHING)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    picture_hash = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'report'


class ReportAction(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(AppUser, models.DO_NOTHING)
    action_type = models.ForeignKey(ActionType, models.DO_NOTHING)
    actioned_at = models.DateTimeField()
    report = models.ForeignKey(Report, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'report_action'


class ReportCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'report_category'


class ReportComment(models.Model):
    id = models.UUIDField(primary_key=True)
    comment_user = models.ForeignKey(AppUser, models.DO_NOTHING)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    changed_by = models.ForeignKey(AppUser, models.DO_NOTHING, db_column='changed_by', related_name='reportcomment_changed_by_set', blank=True, null=True)
    created_at = models.DateTimeField()
    reply_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    content = models.TextField()

    class Meta:
        managed = True
        db_table = 'report_comment'


class ReportStatusHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    new_status = models.ForeignKey('ReportStatusType', models.DO_NOTHING)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    changed_by = models.ForeignKey(AppUser, models.DO_NOTHING, db_column='changed_by')
    changed_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'report_status_history'


class ReportStatusType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'report_status_type'


class UserMarker(models.Model):
    id = models.UUIDField(primary_key=True)
    gps = models.TextField()
    name = models.CharField(max_length=200)
    colour = models.CharField(max_length=50, blank=True, null=True)
    icon_type = models.ForeignKey(IconType, models.DO_NOTHING, blank=True, null=True)
    owned_by = models.ForeignKey(AppUser, models.DO_NOTHING, db_column='owned_by')

    class Meta:
        managed = True
        db_table = 'user_marker'
