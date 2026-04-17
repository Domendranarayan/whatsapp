from django.shortcuts import render
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse

def whatsapp_reply(request):
        incomming_msg = request.POST.get('Body', '').lower()
        resp  = MessagingResponse()
        msg = resp.message()

        if incomming_msg == "hi":
                msg.body("hello this your whatsapp bot")
        elif incomming_msg == "help":
                msg.body("Commands: \n hi \nhelp \n info")
        else:
                msg.body(f" You said: {incomming_msg}")
        
        return HttpResponse(str(resp), content_type='application/xml')
        
