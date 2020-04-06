from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<slug:slug>', views.view, name='view'),
    path('tools', views.tools, name='tool'),
    path('inspirations', views.inspirations, name='inspirations'),
    path('search', views.search, name='search'),
    path('tag/<slug:tag>', views.tag, name='tag'),
    path('page/<slug:slug>', views.page, name='page'),
    #path('articles/<slug:title>/', views.article, name='article-detail'),
    #path('articles/<slug:title>/<int:section>/', views.section, name='article-section'),
    #path('weblog/', include('blog.urls')),
    
]