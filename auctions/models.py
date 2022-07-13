from django.db.models import Max
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class User(AbstractUser):
    pass

class Categories(models.Model):
    
    name_categories = models.CharField(max_length=80)
    def __str__(self) -> str:return f"{self.name_categories}"
class Listings(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=64,blank=False)
    description = models.TextField(blank=False)
    starting_bid = models.FloatField()
    url_image = models.URLField(blank=True,default="https://upload.wikimedia.org/wikipedia/commons/2/2f/No-photo-m.png")
    date = models.DateTimeField(default=datetime.datetime.now())
    active = models.BooleanField(blank = False, default = True)
    categorie = models.ForeignKey(Categories,on_delete= models.CASCADE,related_name="cat")
    name_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    watchList = models.ManyToManyField(User, blank=True, related_name="watchlisting")
    
    def __str__(self) -> str:return f"{self.title} from {self.name_user}"
    @property
    def count_bid(self):
        return self.user_bids.all().count()
    @property
    def max_bid(self):
        if self.count_bid > 0:return round(self.user_bids.aggregate(Max('amount'))['amount__max'],2)
        return self.starting_bid
    @property
    def winner(self):
        if self.count_bid > 0: return  self.user_bids.get(amount= self.max_bid).user
    def watch_list(self,user):
        return user.watchlisting.filter(pk=self.id).exists()
        

class Bids(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    item = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="user_bids",blank=False,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids",null=True)
    def __str__(self) -> str:return f"{self.amount}"
        
class Comments(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now(),null=True)
    comment = models.CharField(max_length=1000,null=True) 
    item = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="comment",null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userc",null=True)

    


    

