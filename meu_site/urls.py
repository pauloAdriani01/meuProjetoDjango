"""
URL configuration for meu_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#Aqui estão os caminhos de URL que o Django irá usar para encaminhar o usuário a página selecionada

from django.contrib import admin
from django.urls import include, path 
#importa as funções include e path do módulo django.urls
#Servindo para definir rotas de URL e incluir outras configurações de URL

#*URL -> Localizador Uniforme de Recursos

urlpatterns = [
    #Rota raiz do site, que inclui as URLs definidas no aplicativo 'usuarios'
    path('', include('usuarios.urls')), 
    path('admin/', admin.site.urls),
    
]
