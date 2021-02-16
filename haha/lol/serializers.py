from django.db.models.query import QuerySet
class UserSerializer:
    def __init__(self, obj):
        self.user = obj
    def serialize(self):
        res = {
            "username": self.user.username,
            "email": self.user.email,
            "id": self.user.id,
            "password": self.user.password,
            "image": self.user.pfp
        }
        return res
class ListingSerializer():
    def __init__(self, obj):
        if (isinstance(obj, QuerySet)) == True:
            self.objects = obj
            self.is_queryset = True
        else: 
            self.objects = [obj]
            self.is_queryset = False
    def add(self, other):
        if self.is_queryset == False:            
            if self.objects[0].__class__ == other.__class__:
                self.objects.append(other) 
    def serialize(self):
        res = []
        static_attrs = [
            "title",
            "desc",
            "min_bid",
            "image"
        ]
        for i in self.objects:
            a = {}
            for j in static_attrs:
                a[j] = getattr(i, j)
            host = UserSerializer(i.host)
            a["host"] = host.serialize()
            a["bids"] = []
            a["end"] = i.end.strftime("%m/%d/%Y, %H:%M:%S")
            for j in i.bids.all():
                a["bids"].append({
                    "bid": j.amount,
                    "bidder": UserSerializer(j.user).serialize()
                })
            res.append(a)
        return res

