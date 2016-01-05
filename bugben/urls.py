from django.conf.urls import url
from django.contrib import admin
from resume import views
from resume.views import ResumeDetailView

urlpatterns = [
    url(r'^$', ResumeDetailView.as_view()),
    url(r'^format/(?P<format>.*)/$', ResumeDetailView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^riker/', views.riker),

]
