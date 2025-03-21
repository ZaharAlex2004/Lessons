from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Ad, Comment, User, Category
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone


class AdModelTest(TestCase):
    def test_auto_deactivate_ad(self):
        # Create a user
        user = get_user_model().objects.create_user(username="testuser", email="test@example.com", password="password123")

        # Create a category (required because the Ad model has a ForeignKey to Category)
        category = Category.objects.create(name="Test Category", description="A test category")

        # Now create an Ad and associate it with the user
        ad = Ad.objects.create(
            title="Old Ad",
            description="Old description",
            price=100,
            user=user,  # Make sure to associate the ad with the user
            category=category  # Add the required category
        )

        # Test logic...
        self.assertEqual(ad.is_active, True)


class CommentModelTest(TestCase):

    def test_count_comments(self):
        user = User.objects.create(username="user1", email="user1@example.com")
        category = Category.objects.create(name="Category1")
        ad = Ad.objects.create(title="Ad 1", description="Description", price=100, user=user, category=category)
        comment1 = Comment.objects.create(content="Comment 1", ad=ad, user=user)
        comment2 = Comment.objects.create(content="Comment 2", ad=ad, user=user)

        self.assertEqual(Comment.count_comments(ad), 2)
