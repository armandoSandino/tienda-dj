# APIView es equivalente al FormView de Django
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#THIRD_PARTY_APPS
from firebase_admin import auth

from django.shortcuts import render
# Generic views
from django.views.generic import TemplateView
# Serializers
from .serializers import LoginSocialSerializer
# models
from .models import User

class LoginUser(TemplateView):

    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        return context


class GoogleLoginView(APIView):

    serializer_class = LoginSocialSerializer

    def post(self, request ):
        # Obtener los datos del formulario
        # serializado = LoginSocialSerializer(data=request.data)
        serializado = self.serializer_class(data=request.data)
        serializado.is_valid(raise_exception=True)
        #
        id_token = serializado.data.get('el_token')

        # Decodificar el token
        token_decodificado = auth.verify_id_token(id_token)
        #
        email = token_decodificado['email']
        name = token_decodificado['name']
        avatar = token_decodificado['picture']
        verified =token_decodificado['email_verified']
        
        # verificar si el usuario ya fue creado en la db
        el_usuario,  crear = User.objects.get_or_create(
            email=email,
            defaults= {
                'full_name': name,
                'email': email,
                'is_active': True
            }
        )
        # SI el usuario se creo vamos a generar su token
        if crear:
            token = Token.objects.create(user=el_usuario)
        else:
            token = Token.objects.get(user=el_usuario)


        userGet = {
            'ID': el_usuario.pk,
            'email': el_usuario.email,
            'full_name': el_usuario.full_name,
            'genero': el_usuario.genero,
            'date_birth': el_usuario.date_birth,
            'city': el_usuario.city
        }

        return Response({
            'response': True,
            'token': token.key,
            'usuario': userGet
        })
