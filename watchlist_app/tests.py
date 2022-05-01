from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from watchlist_app.api import serializers
from .models import StreamingPlatform, WatchList

class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.User.objects.create_user(username="example", password="Example@1")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.stream = StreamPlatform.objects.create(name="netflix", about="dd", website="https://www.netflix.com")

    def test_streamplatform_create(self):
        data = {
            "name":"netflix",
            "about":"sssss",
            "website":"https://netflix.com"
        }
        response = self.client.post(reverse('streaming_create'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streaming_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class WatchListTestCase(APITestCase):

    def setUp(self):
        self.User.objects.create_user(username="example", password="Example@1")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.stream = StreamPlatform.objects.create(name="netflix", about="dd", website="https://www.netflix.com")
        self.watchlist = WatchList.objects.create(platform=self.stream, title="dd", storyline=True)

    def test_watchlist_creat(self):
        data = {
            "platform":self.stream,
            "title":"example movie",
            "storyline":"SSSSSSS",
            "active":True
        }
        response = self.client.post(reverse('watch_list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('watch_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_ind(self):
        response = self.client.get(reverse('watch_list_detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(WatchList.objects.get().title, 'example movie')


class ReviewTestCase(APITestCase):

    def setUp(self):
        self.User.objects.create_user(username="example", password="Example@1")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = StreamPlatform.objects.create(name="netflix", about="dd", website="https://www.netflix.com")
        self.watchlist = WatchList.objects.create(platform=self.stream, title="dd", storyline="lkjh", active=True)
        self.watchlist2 = WatchList.objects.create(platform=self.stream, title="dd", storyline="lkjh", active=True)
        self.review = Review.objects.create(review_user=self.user, rating=5, watchlist=self.watchlist2,description="kjh", active=True)

    def test_review_create(self):
        data = {
            'review_user':self.user,
            'rating':5,
            'description':"Great Movie",
            "watchlist":self.watchlist,
            "active":True
        }
        response = self.client.post(reverse('review_create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)
        self.assertEqual(Review.objects.get().rating, 5)

    def test_review_create_unauth(self):
        data = {
            'review_user': self.user,
            'rating': 5,
            'description': "Great Movie",
            "watchlist": self.watchlist,
            "active": True
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review_create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            'review_user': self.user,
            'rating': 4,
            'description': "Great Movie",
            "watchlist": self.watchlist,
            "active": True
        }
        response = self.client.post(reverse('review_detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_review_list(self):
        response = self.client.post(reverse('review', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_ind(self):
        response = self.client.post(reverse('review_detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_user(self):
        response = self.client.get('/reviews/?username' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


