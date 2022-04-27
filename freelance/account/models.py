from django.db import models
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.

FREELANCER = "freelancer"
CLIENT = "client"


class CustomUserManager(UserManager):
    def freelancers(self):
        return self.filter(user_type=FREELANCER)

    def clients(self):
        return self.filter(user_type=CLIENT)


class User(models.Model):
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )

    USER_TYPES = (
        (FREELANCER, _("Freelancer")),
        (CLIENT, _("Client")),
    )
    user_type = models.CharField(
        _("User Type"), choices=USER_TYPES, max_length=30
    )
    is_subscribe = models.BooleanField(
        _("Is subscribed"),
        default=True,
        help_text=_("Designate whether the user is subscribed for email notification."),
    )

    active_login = models.BooleanField(
        _("Is login"),
        default=False,
        help_text=_("Check whether the user is currently logged in or not."),
    )

    authentication_required = models.BooleanField(
        _("Is login"),
        default=False,
        help_text=_("Check whether the user need login authentication."),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    avatar = models.ImageField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    @property
    def is_freelancer(self) -> bool:
        if self.user_type == FREELANCER:
            return True
        return False

    @property
    def is_client(self) -> bool:
        if self.user_type == CLIENT:
            return True
        return False

    def __str__(self):
        return "User <{}>".format(self.email)
