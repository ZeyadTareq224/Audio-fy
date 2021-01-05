from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('FAQ/', views.FAQ, name="FAQ"),
    path('history-audios/', views.history, name="history"),
    path('saved-pdfs/', views.saved_pdfs, name="saved-pdfs"),
    path('delete-pdf/<int:pk>', views.delete_pdf, name="delete-pdf"),
    path('convert/<int:pk>/', views.convert_pdf_to_audio, name="convert"),

]
