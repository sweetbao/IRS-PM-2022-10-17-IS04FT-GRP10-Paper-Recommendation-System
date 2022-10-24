from django.contrib.auth.models import User
from rest_framework.authtoken.views import APIView, AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from .models import UserViewRecord, UserPrefer
from .serializers import PreferSerializer, ViewRecordSerializer


class Register(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        if User.objects.filter(username=username).exists():
            resp = {"status": False, "data": "用户名已被注册"}
        else:
            user = User.objects.create_user(username=username, password=password)
            token, created = Token.objects.get_or_create(user=user)
            resp = {
                "status": True,
                "token": token.key,
                "user_id": user.pk,
                "user_name": user.username,
            }
        return Response(resp)


class Login(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "status": True,
                "token": token.key,
                "user_id": user.pk,
                "user_name": user.username,
            }
        )


class UserPreferViewSet(viewsets.ModelViewSet):

    queryset = UserPrefer.objects.all().order_by("-retrievetime")
    serializer_class = PreferSerializer

    def get_queryset(self):
        UserID = self.request.query_params.get("userid", None)
        if UserID:
            qs = UserPrefer.objects.filter()
            qs = qs.filter(UserID=UserPrefer.UserID)
            return qs

        return super().get_queryset()

    def delete(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset.delete()  # CAREFUL! This could easily delete all the items in this queryset.
        # You might want some additional checking
        return Response(self.get_queryset())


class UserRecordViewSet(viewsets.ModelViewSet):

    queryset = UserViewRecord.objects.all().order_by("-retrievetime")
    serializer_class = ViewRecordSerializer

    def get_queryset(self):
        UID = self.request.query_params.get("userid", None)
        if UID:
            qs = UserViewRecord.objects.filter()
            qs = qs.filter(UID=UserViewRecord.UserID)

            return qs

        return super().get_queryset()
