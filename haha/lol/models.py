from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pfp = models.URLField(default="https://pm1.narvii.com/6755/8bf4fe6f5365d373ffe14121d94ffb75f9281e9fv2_hq.jpg")
class Listing(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctions")
    desc = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
    min_bid = models.PositiveIntegerField()
    bids = models.ManyToManyField('Bid', symmetrical=False)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateField(blank=True)
    image = models.URLField(blank=True)
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    for_listing = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name="all_bids")
    amount = models.PositiveIntegerField()


