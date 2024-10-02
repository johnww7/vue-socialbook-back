from urllib import response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, auth
from rest_framework import status, permissions
from .models import Profile, Post, LikePost, FollowersCount
from .serializers import ProfileSerializer, PostSerializer, LikePostSerializer, FollowersCountSerializer,UserSerializer

#@method_decorator(csrf_protect,name='dispatch')
class api_upload(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        new_post = PostSerializer(data = request.data)
        print('post data: ', new_post)
        if new_post.is_valid():
            new_post.save()
            return Response(new_post.data, status=status.HTTP_201_CREATED)

        return Response(new_post.errors, status=status.HTTP_400_BAD_REQUEST) 


#@method_decorator(csrf_protect,name='dispatch')
class api_like_post(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, post_id, username):
        try:
            #post = Post.objects.get(id=post_id)
            return LikePost.objects.filter(post_id=post_id, username=username)
        except Post.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        username = request.user.username
        #post_id = request.GET.get('post_id')
        post_id = request.data.post_id
        post = Post.objects.get(id=post_id)
        like_post = self.get_object(post_id, username)
        like_post_serializer = LikePostSerializer(like_post)
        if like_post_serializer.is_valid():
            like_post_serializer.save()
            post_serializer = PostSerializer(post)
            post_serializer.save()
            post_data = {'like_post': like_post_serializer.data, 'post': post_serializer.data}
            return Response(post_data, status=status.HTTP_201_CREATED)

        return Response(like_post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, format=None):
        username = request.username
        post_id = request.data.post_id
        like_post = self.get_object(post_id, username)
        post = Post.objects.get(id=post_id)
        like_serializer = LikePostSerializer(like_post)
        post_serializer = PostSerializer(post)
        post_data = {'like_post': like_serializer, 'post': post_serializer}
        return Response(post_data)

#@method_decorator(csrf_protect,name='dispatch')
class api_profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        #user_object = User.objects.get(username=request.data)
        print('Whats user: ', request.user)
        print('All users: ', User.objects.all())
        #user_object = User.objects.get()
        user_object = request.user
        user_profile = Profile.objects.filter(user=request.user).get()
        print('User profile: ', user_profile)
        user_posts = Post.objects.all()
        #user_posts = Post.objects.filter(user=request.user)
        print('User posts: ', user_posts)
        follower_count = FollowersCount.objects.all()
        #print('Follower count: ', follower_count)

        user_profile_serializer = ProfileSerializer(user_profile)
        user_posts_serializer = PostSerializer(user_posts, many=True)
        follower_count_serializer = FollowersCountSerializer(follower_count, many=True)

        return Response({
            
            "user_profile": user_profile_serializer.data,
            "user_post": user_posts_serializer.data,
            "follower_count": follower_count_serializer.data
        })

class api_profile_user(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        #user_object = User.objects.get(username=request.data)
        print('Whats user: ', pk)
        print('All users: ', User.objects.all())
        #user_object = User.objects.get()
        #user_object = request.data.user
        user_object = pk
        #user_profile = Profile.objects.filter(user=pk).get()
        user_profile = Profile.objects.all()
        print('User profile: ', user_profile)
        user_posts = Post.objects.all()
        #user_posts = Post.objects.filter(user=request.user)
        print('User posts: ', user_posts)
        follower_count = FollowersCount.objects.all()
        #print('Follower count: ', follower_count)

        user_profile_serializer = ProfileSerializer(user_profile)
        user_posts_serializer = PostSerializer(user_posts, many=True)
        follower_count_serializer = FollowersCountSerializer(follower_count, many=True)

        return Response({
            
            "user_profile": user_profile_serializer.data,
            "user_post": user_posts_serializer.data,
            "follower_count": follower_count_serializer.data
        })

class api_user_suggestion(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        all_users = User.objects.all()
        print('whats User users: ', User.objects.all())
        print('whats profiles: ', Profile.objects.all())
        user_following = FollowersCount.objects.all()
        feed_lists = Post.objects.all()
        profile_lists = Profile.objects.all()

        user_following_serializer = FollowersCountSerializer(user_following, many=True)
        feed_list_serializer = PostSerializer(feed_lists, many=True)
        profile_list_serializer = ProfileSerializer(profile_lists, many=True)
        user_serializer = UserSerializer(all_users, many=True)
        print("suggestion profile serializer: ", profile_list_serializer.data)

        return Response({
            "followers": user_following_serializer.data,
            "posts": feed_list_serializer.data,
            "profiles": profile_list_serializer.data,  
            'users': user_serializer.data,          
        })
        

        

#@method_decorator(csrf_protect,name='dispatch')
class api_follow(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        follower = request.data.follower
        user = request.data.user

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            follower_count = FollowersCount.objects.get(follower=follower, user=user)
            follower_count.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            new_follower = FollowersCountSerializer(data=request.data)
            if new_follower.is_valid():
                new_follower.save()
                return Response(new_follower.data)
            return Response(new_follower.errors, status=status.HTTP_400_BAD_REQUEST)    

#@method_decorator(csrf_protect,name='dispatch')        
class api_settings(APIView):
    permission_classes = [IsAuthenticated]
    print("I am in settings view")
    def get_object(self, username):
        try:
            #post = Post.objects.get(id=post_id)
            return Profile.objects.get(user=username)
        except Post.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        user_profile = self.get_object(request.data.user)

        if request.data.image == None:
            image = user_profile.profileimg
            bio = request.data.bio
            location = request.data.location
            profile_data = {
                "image": image,
                "bio": bio,
                "location": location
            }
            user_serializer = ProfileSerializer(data=profile_data)
            user_serializer.save()
            return Response(user_serializer.data)

        if request.data.image != None:
            image = request.data.profileimg
            bio = request.data.bio
            location = request.data.location
            profile_data = {
                "image": image,
                "bio": bio,
                "location": location
            }
            user_serializer = ProfileSerializer(data=profile_data)
            user_serializer.save()
            return Response(user_serializer.data)

    def get(self, request, format=None):
        print("whats request: ", request.data)
        #user_profile = self.get_object(request.data)
        user_profile = Profile.objects.all()
        user_serializer = ProfileSerializer(user_profile, many=True)
        return Response(user_serializer.data)

#@method_decorator(csrf_protect,name='dispatch')        
class api_createprofile(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        username = request.data.user
        email = request.data.email
        if(User.objects.filter(username=username, email=email) == None):
            user_model = User.objects.get(username=username)
            new_profile = ProfileSerializer(user=user_model, id_user=user_model.id)
            #new_profile= Profile.objects.create(user=user_model,id_user=user_model.id)
            if new_profile.is_valid():
                new_profile.save()
                return Response(new_profile.data, status=status.HTTP_201_CREATED)
        return Response(new_profile.errors, status=status.HTTP_400_BAD_REQUEST)

