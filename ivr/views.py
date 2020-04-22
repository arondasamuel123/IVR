from rest_framework import generics
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import UserBankDetails


# Create your views here.
class Calls(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        isActive = request.POST.get("isActive")
        if isActive == '1':
            content = """<?xml version="1.0" encoding="utf-8"?> <Response> <GetDigits timeout="10" finishOnKey="#" 
            callbackUrl="https://c31a6d18.ngrok.io/call/select_service/"> <Say>Welcome to Furaha Bank. Your bank of choice. Please press one followed by hash for English. Please press two followed by hash for Kiswahili</Say> </GetDigits> <Say>We did not get any response. Good bye</Say> </Response> """
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
            data = {'session_id':session_id,'caller_number':phone_number,'dtmfDigits':digits, 'direction':direction}
            serializers = SessionSerializer(data=data)
            if serializers.is_valid():
                serializers.save()
            if digits == '1':
      
                content = """ <?xml version="1.0" encoding="utf-8"?> <Response> <GetDigits timeout="10" finishOnKey="#" 
            callbackUrl=""> <Say>Please select your service followed by hash.
                                 Press 1 to check your account balance
                                 Press 2 to check your last deposit
                                 Press 3 to check your last withdraw
                                 Press 4 to speak to an agent </Say> </Response> """
        
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
            if digits == '1':
                content = """<?xml version="1.0" encoding="utf-8"?><Response><GetDigits timeout="10" finishOnKey="#" 
                callbackUrl=""><Say>Please enter your account number followed by hash to receive account 
                balance</Say></GetDigits><Say>We did not get any response. Good bye</Say></Response>"""
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

            elif digits == '2':
                content = """<?xml version="1.0" encoding="utf-8"?><Response><GetDigits timeout="10" finishOnKey="#" 
                callbackUrl="https://c31a6d18.ngrok.io/call/last_deposit/"><Say>Please enter your account number followed by hash to receive your last deposit amount</Say></GetDigits><Say>We did not get any response. Good bye</Say></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

            elif digits == '3':
                content = """<?xml version="1.0" encoding="utf-8"?><Response><GetDigits timeout="10" finishOnKey="#" 
                callbackUrl=""><Say>Please enter your account number followed by hash to receive your last withdrawal 
                amount</Say></GetDigits><Say>We did not get any response. Good bye</Say></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

            elif digits == '4':
                content = """<?xml version="1.0" encoding="utf-8"?><Response><Say>You will shortly be redirected to 
                customer care agent</Say></Response> """
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
            deposit = UserBankDetails.objects.filter(account_number=digits).first()
            if deposit is not None:
                fname = str(deposit.user_id.first_name)
                lname = str(deposit.user_id.last_name)
                deposit_amount = str(deposit.deposit)
                content = """<?xml version="1.0" encoding="utf-8"?><Response><Say> """ + fname + """ """ + lname + """ your last deposit is """ + deposit_amount + """ shillings </Say></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

            else:
                length = len(count)
                if length < 4:
                    content = """<?xml version="1.0" encoding="utf-8"?><Response><GetDigits timeout="10" 
                    finishOnKey="#" callbackUrl="https://c31a6d18.ngrok.io/call/last_deposit/"><Say>The account does not exist. Please enter the correct account number followed by hash</Say></GetDigits><Say>We did not get any response. Good bye</Say></Response> """
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
    def post(self,request,count=[],*args,**kwargs):
        isActive=request.POST.get("isActive")
        if isActive=='1':
            digits=request.POST.get("dtmfDigits")
            if digits=='1':
                deposit
