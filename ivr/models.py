from django.db import models


# Create your models here.
class Session(models.Model):
    session_id = models.CharField(max_length=50)
    caller_number = models.CharField(max_length=20)
    dtmfDigits = models.CharField(max_length=10)
    direction = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caller_number


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class UserBankDetails(models.Model):
    account_number = models.CharField(max_length=30)
    deposit = models.CharField(max_length=30)
    withdrawal = models.CharField(max_length=30)
    account_balance = models.CharField(max_length=30)

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_number
