from django.urls import path
from .views import Calls, EnterAccountNumber, GetLastWithdraw

urlpatterns = [
    path('calls/', Calls.as_view(), name='calls'),
    path('call/account_balance/', EnterAccountNumber.as_view(), name='account_balance'),
    path('call/last_withdraw/', GetLastWithdraw.as_view(), name='last_withdraw'),

    
]