from django.http import HttpResponse

def home(request):
    return HttpResponse("\
        <!Doctype html>\
        <html lang='en'/>\
            <head>\
                <meta charset='utf-8'/>\
                <meta name='viewport' content='width=device-width, initial-scale=1'/>\
                <title>N ION</title>\
                <style>\
                    * {\
                        margin: 0;\
                        padding: 0;\
                        box-sizing: border-box;\
                    }\
                    html, body {\
                        background-color: #92112687;\
                    }\
                </style>\
            </head>\
            <body>\
                <nav id='nion-navbar'>\
                    <div id='nion-div-logo'>\
                        <svg xmlns='https://www.w3.org/2000/scg/'>\
                            <path d='M26 26 L26 87 L50 50 Z' fill='#001928'></path>\
                        </svg>\
                    </div>\
                </nav>\
            </body>\
        </html>")
def account(request):
    return HttpResponse("<title>N ION- account</title>")
def username(request):
    return HttpResponse("<title>N ION - username</title>")
def settings(request):
    return HttpResponse("<title>N ION - settings</title>")
