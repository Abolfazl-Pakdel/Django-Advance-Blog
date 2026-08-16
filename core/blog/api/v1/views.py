from django.core.serializers import serialize
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.response import Response

# --------------------------------------
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    GenericAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import *


class PostList(ListCreateAPIView):
    """getting a list of posts and creating new posts"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostViewSet(viewsets.ModelViewSet):
    """getting a list of posts and creating new posts"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination
    # @action(methods=['get'], detail=False)
    # def get_ok(self, request):
    #     return Response({'detail':'ok'})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


"""    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def create(self, request):
        pass
    def update(self, request, pk=None):
        pass
    def partial_update(self, request, pk=None):
        pass
    def destroy(self, request, pk=None):
        pass"""
"""class PostList(APIView):
    '''getting a list of posts and creating new posts'''
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self, request):
        '''returving a list of posts'''
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self, request):
        '''crating a post with provided data'''
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)
"""
"""
class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
"""
"""
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postList(request):
#     if request.method == 'GET':
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(request.data)

# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postDetail(request, id):
#     post = get_object_or_404(Post, pk=id, status=True)
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail":"item removed successfully"}, status=status.HTTP_204_NO_CONTENT)

"""
