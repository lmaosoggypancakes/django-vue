from django.http import HttpResponse, JsonResponse
from .models import Listing, Bid, User
from .serializers import ListingSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import json
ALLOWED = "http://127.0.0.1:8080"
def check_username(name):
    print(name)
    for i in User.objects.all():
        if name == i.username:
            return False
    return True
check = lambda request: request.META["HTTP_ORIGIN"] == ALLOWED
@csrf_exempt
def register(request):
    if check(request):
        data = json.loads(request.body)
        try:
            a = User.objects.create(username=data["username"], password=data["password"], email=data["email"], first_name=data["first"], last_name=data["last"], pfp=data["pfp"])
            return JsonResponse(
                {
                    'user': UserSerializer(a).serialize()
                }
            )
        except:
            return JsonResponse({
                'message': "Something went wrong!"
            })
def get_all(request):
    print(request.META["HTTP_ORIGIN"])
    if check(request):
        listings = Listing.objects.all()
        the = ListingSerializer(listings)
        return JsonResponse(the.serialize(), safe=False)
    else:
        return JsonResponse({
            "message": "not authorized."
        })
@csrf_exempt
def login_view(request):
    print(check(request))
    if check(request):
        try:
            data = json.loads(request.body)
            username = data["username"]
            password = data["password"]
            try: 
                user = User.objects.get(username=username, password=password)
            except:
                user = None
            print(user)
        except:
            return JsonResponse({
                'valid': 'false',
                "message": "invalid credentials."
            })
        if user is not None:
            the_user = User.objects.get(username=username, password=password)
            # serialize the user
            the = UserSerializer(the_user) 
            return JsonResponse({
                'valid': 'true',
                "message": "You have been logged in.",
                "user": the.serialize()
            }, safe=False)
        return JsonResponse({
            'valid': 'false',
            "message": "invalid credentials."
        })
def logout_view(request):
    if check(request):
        logout(request)
        return JsonResponse({
            "message": "You have been logged out."
        })
def grab_post(request, id):
    post = ListingSerializer(Listing.objects.get(id=id))
    return JsonResponse(post.serialize())
@csrf_exempt
def check_view(request):
    print(json.loads(request.body))
    return JsonResponse(
        {
           'is_ok': check_username(json.loads(request.body)["name"])
        },
        safe=False
    )