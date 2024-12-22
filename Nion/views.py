from django.http import HttpResponse


START_HTML = f"\
        <!Doctype html>\
        <html lang='en'/>\
            <head>\
                <meta charset='utf-8'/>\
                <meta name='viewport' content='width=device-width, initial-scale=1'/>\
                <title>N ION</title>\
                <script>\
                        const nionnavbar = document.getElementById('nion-navbar');\
                        nionnavbar.style.position = 'fixed';
                        nionnavbar.style.width = '-webkit-fill-available';
                        nionnavbar.style.height = '9vh';
                        nionnavbar.style.display = 'flex';
                        nionnavbar.style.alignItems = 'center';
                        nionnavbar.style.justifyContent = 'space-around';
                </script>\
            </head>"

STOP_HTML = f"\
        </body>\
        </html>"

homehtml = START_HTML+"<nav id='nion-navbar'>\
            <div id='nion-div-logo'>\
                <svg xmlns='https://www.w3.org/2000/scg/'>\
                    <path d='M26 26 L26 87 L50 50 Z' fill='#001928'></path>\
                </svg>\
            </div>\
        </nav>"+STOP_HTML


def home(request):
    return HttpResponse(homehtml)
def account(request):
    return HttpResponse(homehtml)
def username(request):
    return HttpResponse(homehtml)
def settings(request):
    return HttpResponse(homehtml)