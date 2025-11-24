from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from myproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import random

from .models import Chocolate,Register
from .serializer import TodoSerializer,RegSerializer

# chocolate todo api
@api_view(['POST']) #method type
def create_chocolate(request):
    serializer= TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET']) #method type
# def get_chocolate(request):
#     chocolate=Chocolate.objects.all()
#     serializer=TodoSerializer(chocolate,many=True)
#     return Response(serializer.data)

@api_view(['PUT'])
def update_chocolate(request,pk):
   chocolate=Chocolate.objects.get(pk=pk)
   serializer=TodoSerializer(chocolate,data=request.data)
   if serializer.is_valid():
      serializer.save()
      return Response({'message': 'user updated', 'data': serializer.data},status=status.HTTP_201_CREATED)
   return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def delete_chocolate(request,pk):
   product=Chocolate.objects.get(pk=pk)
   product.delete()
   return Response(status=status.HTTP_204_NO_CONTENT)

# get data by filter

@api_view(['GET'])
def chocolate_list(request):
    chocolate_name = request.query_params.get('chocolate_name', None)  

    if chocolate_name:
        products = Chocolate.objects.filter(chocolate_name__icontains=chocolate_name)
    
    else:
        products = Chocolate.objects.all()
   
    serializer = TodoSerializer(products , many=True) 
    return Response({
    "products": serializer.data
          })


# login api

@api_view(['POST'])
def create_user(request):
    phonenumber=request.data.get('phone_number')
    name=request.data.get('name')
    if Register.objects.filter(phone_number=phonenumber).exists():
        return Response({'error':'Phone number already exists'},status=status.HTTP_400_BAD_REQUEST)
    elif Register.objects.filter(name=name).exists():
        return Response({'error':'name already exists'},status=status.HTTP_400_BAD_REQUEST)
    serializer=RegSerializer(data=request.data)   
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


#login after registrtion
#checks if the mobile is already registered
@api_view(['POST'])
def login_user(request):
    phonenumber=request.data.get('phone_number')
    try:
        user=Register.objects.get(phone_number=phonenumber)
        serializer=RegSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Register.DoesNotExist:
        return Response({'error':'Phone number does not exits'},status=status.HTTP_400_BAD_REQUEST)


#view all the users
@api_view(['GET'])
def get_user(request):
    register=Register.objects.all()
    serializer=RegSerializer(register,many=True)
    return Response(serializer.data)

# email api
@api_view(['POST'])
def mailSend(request):
    
    name=request.data.get('name')
    email=request.data.get('email')
    otp=''
    for i in range(6):
        digit=random.randint(0,9)
        otp+=str(digit)

    subject = "Welcome Friend"
    message = f"Hi {name}, Your OTP is {otp}"
    recipient_list = [email]

    send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=False)

    return Response({'message': 'OTP sent successfully', 'otp': otp}, 
                    status=status.HTTP_200_OK)





