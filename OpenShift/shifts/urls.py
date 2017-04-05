#blank file created by me
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	#parking_train
	url(r'parking_train/', views.parking_train, name = 'parking_train'),
	url(r'hotel_location/', views.hotel_location, name = 'hotel_location'),
	url(r'parking/', views.parking, name = 'parking'),
	url(r'train/', views.train, name = 'train'),


	#post confirm
	#post confirm shift per per Ascent TV Tut
    url(r'^shift/post_url/([0-9]+)', views.post_confirm, name = 'post_confirm'),

	#each shift as  url
	url(r'shift/([0-9]+)', views.each_shift, name = 'each_shift'),
]
