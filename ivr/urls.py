from django.urls import path
from .views import Calls, ServiceSelection, EnterAccountNumber, ObtainUserDeposit,GetAccountBalance

urlpatterns = [
    path('calls/', Calls.as_view(), name='calls'),
    path('call/select_service/', ServiceSelection.as_view(), name='language_response'),
    path('call/account_number/', EnterAccountNumber.as_view(), name='enter_account_number'),
    path('call/last_deposit/', ObtainUserDeposit.as_view(), name='last_deposit'),
    path('call/account_balance/', GetAccountBalance.as_view(), name='account_balance'),

]
