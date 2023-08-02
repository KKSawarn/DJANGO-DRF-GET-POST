from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shirt.models import Category, Shirt

from shirt.serializers import CategoryDetailSerializer, CategorySerializerParam, CreateCategorySerializer, CreateShirtSerializer, ShirtDetailSerializer, ShirtSerializerParam

# Create your views here.
class CreateShirtView(APIView):
    """
    this class has implementation of post method and get method.
    post method is used to create information about shirt whear as get method is used to fetch all details of shirt.
    """
    @staticmethod
    def post(request):
        try:
            params = CreateShirtSerializer(data=request.data,partial=True)
            if params.is_valid(raise_exception=True):
                Shirt.objects.create(
                    item_id=params.validated_data.get("item_id"),
                    brand_name=params.validated_data.get("brand_name"),
                    fabric=params.validated_data.get("fabric"),
                    sku=params.validated_data.get("sku"),
                    is_imported=params.validated_data.get("is_imported"),
                    category_id=Category.objects.get(category_id = params.validated_data.get("category__id")).category_id
                )
                return Response({"Message ":"Created Successfully."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"Error":"Faild to create.}"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error":f"Faild to create. Error: {e} "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    @staticmethod
    def get(request):
        try:
            params = ShirtSerializerParam(data=request.GET,partial=True)
            if params.is_valid(raise_exception=True):
                return Response(
                    ShirtDetailSerializer(
                        Shirt.objects.filter(**params.validated_data),many=True
                    ).data
                )
            else:
                return Response({"Error":"Faild to fetch.}"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error":f"Faild to fetch. Error: {e} "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreateCategoryView(APIView):
    """
    this class has implementation of post method and get method.
    post method is used to create information about categofy whear as get method is used to fetch all details of category.
    """
    @staticmethod
    def post(request):
        try:
            params = CreateCategorySerializer(data=request.data,partial=True)
            obj=0
            if params.is_valid(raise_exception=True):
                Category.objects.create(
                    **params.validated_data
                )
                return Response({"Message":"Category created"},status=status.HTTP_201_CREATED)

            else:
                return Response({"Error":f"Faild to create.{obj}"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"Error":f"Faild to create. Error: {e} "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def get(request):
        try:
            return Response(
                CreateCategorySerializer(
                    Category.objects.filter(),many=True,
                ).data,status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({"Error":f"Faild to fetch. Error: {e} "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
