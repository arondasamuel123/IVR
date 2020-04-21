from rest_framework import generics
from django.http import HttpResponse
from .serializers import SessionSerializer


# Create your views here.
class Calls(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        isActive = request.POST.get("isActive")
        if isActive == '1':
            content = """<?xml version="1.0" encoding="utf-8"?> <Response> <GetDigits timeout="10" finishOnKey="#" 
            callbackUrl=""> <Say>Welcome to Furaha Bank. Your bank of choice. Please press one followed by hash for 
            English. Please press two followed by hash for Kiswahili</Say> </GetDigits> <Say>We did not get any 
            response. Good bye</Say> </Response> """
            response = HttpResponse(content, content_type="application/xml; charset=utf-8")
            response['Content-Length'] = len(content)

            return response

        return HttpResponse("Ok")


class CallResponseForLanguage(generics.CreateAPIView):
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
                content = """<?xml version="1.0" encoding="utf-8"?<Response><Say>Thank you for selecting 
                Kiswahili</Say></Response> """
                response = HttpResponse(content, content_type="application/xml; charset=utf-8")
                response['Content-Length'] = len(content)

                return response

        return HttpResponse("Ok")
