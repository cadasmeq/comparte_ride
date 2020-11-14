"""Invitations tests."""

# Django
from django.test import TestCase

# Model
from cride.circles.models import Invitation
from cride.users.models import User
from cride.circles.models import Circle

class InvitationsManagerTestCase(TestCase):
    """Invitation manager test case."""

    def setUp(self):
        """Test case setup."""
        self.user = User.objects.create(
            first_name = "zedd",
            last_name = "noname",
            email = "zedd@lol.cl",
            username = "zedd",
            password = "inicio123."
        )
        self.circle = Circle.objects.create(
            name = "League of Legends",
            slug_name = "lol",
            about = "League of legends circle.",
            verified = True
        )

    def test_code_generation(self):
        """Random codes should be generated automatically."""
        invitation = Invitation.objects.create(
            issued_by=self.user,
            circle=self.circle
        )
        self.assertIsNotNone(invitation.code)

    def test_code_usage(self):
        """If a code is give, there's no need to create a new one."""
        code = 'holamundo'
        invitation = Invitation.objects.create(
            issued_by = self.user,
            circle = self.circle,
            code = code
        )
        self.assertEqual(invitation.code, code)

    def test_code_generation_if_duplicated(self):
        """If given code is not unique, a new one must be generated."""
        code = Invitation.objects.create(
            issued_by=self.user,
            circle=self.circle,
        ).code
        
        # Create Another Invitation with the past code
        invitation = Invitation.objects.create(
            issued_by=self.user,
            circle=self.circle,
            code = code
        )
        self.assertNotEqual(code, invitation.code)

    

