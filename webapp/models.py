# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
#
from django.urls import reverse

class WhouseIn(models.Model):
    whouse_code = models.IntegerField(primary_key=True)
    whouse_name = models.CharField(max_length=20, blank=False, null=False)
    whouse_address = models.CharField(max_length=30, blank=False, null=False)
    whouse_location = models.CharField(max_length=20, blank=False, null=False)
    whouse_city = models.CharField(max_length=10, blank=False, null=False)
    whouse_phone = models.CharField(db_column='whouse_Phone', max_length=11, blank=False, null=False)  # Field name made lowercase.
    whouse_mobile = models.CharField(max_length=11, blank=False, null=False)
    whouse_head_name = models.CharField(max_length=15, blank=False, null=False)
    whouse_pincode = models.CharField(max_length=6, blank=False, null=False)

    class Meta:
        #managed = False
        db_table = 'whouse_in'

    def __str__(self):
        return str(self.whouse_code) + '-' + self.whouse_name

    def get_absolute_url(self):
        return reverse('webapp:whouse', kwargs={})

class MasterIn(models.Model):
    item_code = models.CharField(primary_key=True, max_length=10)
    item_name = models.CharField(db_column='Item_name', max_length=15, blank=False, null=False)  # Field name made lowercase.
    item_qty = models.DecimalField(db_column='Item_qty', max_digits=15, decimal_places=2, blank=False, null=False)  # Field name made lowercase.
    item_rate = models.DecimalField(db_column='Item_rate', max_digits=15, decimal_places=2, blank=False, null=False)  # Field name made lowercase.
    item_bal_qty = models.DecimalField(db_column='Item_bal_qty', max_digits=15, decimal_places=2, blank=False, null=False)  # Field name made lowercase.
    item_new_rate = models.DecimalField(db_column='Item_new_rate', max_digits=15, decimal_places=2, blank=False, null=False)  # Field name made lowercase.
    whouse_code = models.ForeignKey('WhouseIn', models.DO_NOTHING, db_column='Whouse_code')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'master_in'

    def __str__(self):
        return str(self.item_code)

    def __repr__(self):
        return str(self.item_code) + '-' + self.item_name

    def get_absolute_url(self):
        return reverse('webapp:home', kwargs={})


class ConsumIn(models.Model):
    sl_no = models.AutoField(primary_key=True)
    item_code = models.ForeignKey('MasterIn', models.DO_NOTHING, db_column='item_code', blank=False, null=False)
    date_consum = models.DateField(db_column='Date_consum', blank=False, null=False)  # Field name made lowercase.
    item_consum_qty = models.DecimalField(db_column='Item_consum_qty', max_digits=15, decimal_places=2, blank=False, null=False)  # Field name made lowercase.
    item_consum_rate = models.DecimalField(db_column='Item_consum_rate', max_digits=15, decimal_places=2, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'consum_in'

    def get_absolute_url(self):
        return reverse('webapp:consum', kwargs={})



class IssueIn(models.Model):
    sl_no = models.AutoField(primary_key=True)
    item_code = models.ForeignKey('MasterIn', models.DO_NOTHING, db_column='item_code', blank=False, null=False)
    date_issue = models.DateField(db_column='Date_issue', blank=False, null=False)  # Field name made lowercase.
    item_issue_qty = models.DecimalField(db_column='Item_issue_qty', max_digits=15, decimal_places=2, blank=False, null=False)  # Field name made lowercase.
    item_issue_rate = models.DecimalField(db_column='Item_issue_rate', max_digits=15, decimal_places=2, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'issue_in'

    def get_absolute_url(self):
        return reverse('webapp:issue', kwargs={})

class ItemIn(models.Model):
    item_code = models.ForeignKey('MasterIn', models.DO_NOTHING, db_column='item_code', primary_key=True)
    item_name = models.CharField(db_column='Item_name', max_length=15, blank=False, null=False)  # Field name made lowercase.
    item_reorder_qty = models.DecimalField(db_column='Item_reorder_qty', max_digits=15, decimal_places=2, blank=False, null=False)  # Field name made lowercase.
    item_reorder_rate = models.DecimalField(db_column='Item_reorder_rate', max_digits=15, decimal_places=2, blank=False, null=False)  # Field name made lowercase.
    item_reorder_level = models.DecimalField(db_column='Item_reorder_level', max_digits=15, decimal_places=2, blank=False, null=False)  # Field name made lowercase.
    item_vendor_name = models.CharField(db_column='Item_vendor_name', max_length=20, blank=False, null=False)  # Field name made lowercase.
    item_vendor_address = models.CharField(db_column='Item_vendor_address', max_length=30, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'item_in'

    def __str__(self):
        return str(self.item_code) + '-' + self.item_name

    def get_absolute_url(self):
        return reverse('webapp:item', kwargs={})
