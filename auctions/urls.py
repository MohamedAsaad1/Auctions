from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create",views.create,name="create"),
    path("listing/<int:list_id>",views.listing,name="listing"),
    path("add_bid/<int:list_id>",views.add_bid,name="addbid"),
    path("add_comment/<int:list_id>",views.add_comment,name="addcomment"),
    path("watchlist",views.watch_list,name="watchlist"),
    path("watchchange/<int:list_id>",views.watchchange,name="watchchange"),
    path("watchlist_list/<int:list_id>",views.watchlist_list,name="watchlist_list"),
    path("categories", views.categories, name="categories"),
    path("category/<int:cat_id>",views.category, name="category"),
    path("close/<int:list_id>",views.close, name="close"),
    path("notify",views.notify,name="notify"),
    

]