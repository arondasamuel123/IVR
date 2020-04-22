from django.urls import path
from .views import Calls, ServiceSelection, EnterAccountNumber, ObtainUserDeposit, getLastWithdraw

urlpatterns = [
    path('calls/', Calls.as_view(), name='calls'),
    path('call/select_service/', ServiceSelection.as_view(), name='language_response'),
    path('call/account_number/', EnterAccountNumber.as_view(), name='enter_account_number'),
    path('call/last_deposit/', ObtainUserDeposit.as_view(), name='last_deposit'),
     path('call/last_withdraw/', GetLastWithdraw.as_view(), name='last_withdraw'),

]
