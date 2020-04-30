from rest_framework import generics
from django.http import HttpResponse
from .models import UserBankDetails
from .serializers import SessionSerializer


# Create your views here.
class Calls(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        isActive = request.POST.get("isActive")
        if isActive == '1':
            content = """<?xml version="1.0" encoding="utf-8"?> <Response> <GetDigits timeout="10" finishOnKey="#" 
            callbackUrl="https://262563e5.ngrok.io/call/select_service/"> <Say>Welcome to Furaha Bank. Your bank of choice. Please press one followed by hash for English. Please press two followed by hash for Kiswahili</Say> </GetDigits> <Say>We did not get any response. Good bye</Say> </Response> """
            response = HttpResponse(content, content_type="application/xml; charset=utf-8")
            response['Content-Length'] = len(content)

            return response

        return HttpResponse("Ok")


class ServiceSelection(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        isActive = request.POST.get("isActive")
        if isActive == '1':
            digits = request.POST.get("dtmfDigits")
            session_id = request.POST.get("sessionId")
            phone_number = request.POST.get("callerNumber")
            direction = request.POST.get("direction")
            data = {'session_id': session_id, 'caller_number': phone_number, 'dtmfDigits': digits, 'direction': direction}
            serializers = SessionSerializer(data=data)
            if serializers.is_valid():
                serializers.save()
            if digits == '1':
                content = """<?xml version="1.0" encoding="utf-8"?><Response><GetDigits timeout="10" finishOnKey="#" 
                callbackUrl="https://262563e5.ngrok.io/call/account_number/"><Say>For Account balance please press one followed by hash. For last deposit please press two followed by hash. For last withdrawal please press three followed by hash. To speak to a customer agent please press four followed by hash</Say></GetDigits> <Say>We did not get any response. Good bye</Say></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

            elif digits == '2':
                content = """<?xml version="1.0" encoding="utf-8"?><Response><Say>Thank you for selecting Kiswahili</Say></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

        return HttpResponse("Ok")


class EnterAccountNumber(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        isActive = request.POST.get("isActive")
        if isActive == '1':
            digits = request.POST.get("dtmfDigits")
            session_id = request.POST.get("sessionId")
            phone_number = request.POST.get("callerNumber")
            direction = request.POST.get("direction")
            data = {'session_id': session_id, 'caller_number': phone_number, 'dtmfDigits': digits, 'direction': direction}
            serializers = SessionSerializer(data=data)
            if serializers.is_valid():
                serializers.save()

            if digits == '1':
                content = """<?xml version="1.0" encoding="utf-8"?><Response><GetDigits timeout="10" finishOnKey="#" 
                callbackUrl="https://262563e5.ngrok.io/call/account_balance/"><Say>Please enter your account number followed by hash to receive account balance</Say></GetDigits><Say>We did not get any response. Good bye</Say></Response>"""
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

            elif digits == '2':
                content = """<?xml version="1.0" encoding="utf-8"?><Response><GetDigits timeout="10" finishOnKey="#" 
                callbackUrl="https://262563e5.ngrok.io/call/last_deposit/"><Say>Please enter your account number followed by hash to receive your last deposit amount</Say></GetDigits><Say>We did not get any response. Good bye</Say></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

            elif digits == '3':
                content = """<?xml version="1.0" encoding="utf-8"?><Response><GetDigits timeout="10" finishOnKey="#" 
                callbackUrl="https://262563e5.ngrok.io/last_withdrawal/"><Say>Please enter your account number followed by hash to receive your last withdrawal amount</Say></GetDigits><Say>We did not get any response. Good bye</Say></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

            elif digits == '4':
                content = """<?xml version="1.0" encoding="utf-8"?><Response><Say>You will shortly be redirected to a customer care agent</Say><Dial phoneNumbers="+254727315437"/></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

        return HttpResponse("Ok")


class ObtainUserDeposit(generics.CreateAPIView):

    def post(self, request, count=[], *args, **kwargs):
        isActive = request.POST.get("isActive")
        count.append(1)
        if isActive == '1':
            digits = request.POST.get("dtmfDigits")
            session_id = request.POST.get("sessionId")
            phone_number = request.POST.get("callerNumber")
            direction = request.POST.get("direction")
            data = {'session_id': session_id, 'caller_number': phone_number, 'dtmfDigits': digits, 'direction': direction}
            serializers = SessionSerializer(data=data)
            if serializers.is_valid():
                serializers.save()

            deposit = UserBankDetails.objects.filter(account_number=digits).last()
            if deposit is not None:
                fname = str(deposit.user_id.first_name)
                lname = str(deposit.user_id.last_name)
                deposit_amount = str(deposit.deposit)
                content = """<?xml version="1.0" encoding="utf-8"?><Response><Say> """ + fname + """ """ + lname + """ your last deposit is """ + deposit_amount + """ shillings. Goodbye. </Say></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

            else:
                length = len(count)
                if length < 4:
                    content = """<?xml version="1.0" encoding="utf-8"?><Response><GetDigits timeout="10" 
                    finishOnKey="#" callbackUrl="https://262563e5.ngrok.io/call/last_deposit/"><Say>The account does not exist. Please enter the correct account number followed by hash</Say></GetDigits><Say>We did not get any response. Good bye</Say></Response> """
                    response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                    response['Content-Length'] = len(content)

                    return response

                else:
                    content = """<?xml version="1.0" encoding="utf-8"?><Response><Say>Number of attempts exceeded. Goodbye</Say></Response>"""
                    response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                    response['Content-Length'] = len(content)

                    return response

        return HttpResponse("Ok")


class GetLastWithdraw(generics.CreateAPIView):
    def post(self, request, count=[], *args, **kwargs):
        isActive = request.POST.get("isActive")
        count.append(1)

        if isActive == '1':
            digits = request.POST.get("dtmfDigits")
            session_id = request.POST.get("sessionId")
            phone_number = request.POST.get("callerNumber")
            direction = request.POST.get("direction")
            data = {'session_id': session_id, 'caller_number': phone_number, 'dtmfDigits': digits, 'direction': direction}
            serializers = SessionSerializer(data=data)
            if serializers.is_valid():
                serializers.save()

            withdrawal = UserBankDetails.objects.filter(account_number=digits).last()
            if withdrawal is not None:
                fname = str(withdrawal.user_id.first_name)
                lname = str(withdrawal.user_id.last_name)
                withdrawal_amount = str(withdrawal.withdrawal)
                content = """<?xml version="1.0" encoding="utf-8"?><Response><Say> """ + fname + """ """ + lname + """ your last withdraw is """ + withdrawal_amount + """ shillings. Goodbye. </Say></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

            else:
                length = len(count)
                if length < 4:
                    content = """<?xml version="1.0" encoding="utf-8"?><Response><GetDigits timeout="10" 
                    finishOnKey="#" callbackUrl="https://262563e5.ngrok.io/call/last_withdrawal/"><Say>The account does not exist. Please enter the correct account number followed by hash</Say></GetDigits><Say>We did not get any response. Good bye</Say></Response> """
                    response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                    response['Content-Length'] = len(content)
                    return response

                else:
                    content = """<?xml version="1.0" encoding="utf-8"?><Response><Say>Number of attempts exceeded. Goodbye</Say></Response>"""
                    response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                    response['Content-Length'] = len(content)
                    return response

        return HttpResponse("Ok")


class GetAccountBalance(generics.CreateAPIView):
    def post(self, request, count=[], *args, **kwargs):
        isActive = request.POST.get("isActive")
        count.append(1)
        if isActive == '1':
            digits = request.POST.get("dtmfDigits")
            session_id = request.POST.get("sessionId")
            phone_number = request.POST.get("callerNumber")
            direction = request.POST.get("direction")
            data = {'session_id': session_id, 'caller_number': phone_number, 'dtmfDigits': digits, 'direction': direction}
            serializers = SessionSerializer(data=data)
            if serializers.is_valid():
                serializers.save()

            account_balance = UserBankDetails.objects.filter(account_number=digits).last()
            if account_balance is not None:
                fname = str(account_balance.user_id.first_name)
                lname = str(account_balance.user_id.last_name)
                amount_balance = str(account_balance.account_balance)
                content = """<?xml version="1.0" encoding="utf-8"?><Response> <Say>""" + fname + """ """ + lname + """ your account balance is """ + amount_balance + """ shillings. Goodbye. </Say></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

            else:
                length = len(count)
                if length < 4:
                    content = """<?xml version="1.0" encoding="utf-8"?><Response><GetDigits timeout="10" 
                    finishOnKey="#" callbackUrl=""http://fddb8f91.ngrok.io/call/account_balance/"><Say>The account does not exist. Please enter the correct account number followed by hash</Say></GetDigits><Say>We did not get any response. Good bye</Say></Response> """
                    response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                    response['Content-Length'] = len(content)
                    return response
                else:
                    content = """<?xml version="1.0" encoding="utf-8"?><Response><Say>Number of attempts exceeded. Goodbye</Say></Response>"""
                    response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                    response['Content-Length'] = len(content)
                    return response

        return HttpResponse("Ok")