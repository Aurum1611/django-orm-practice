from core.models import UserProfile
from django.db.models import Q, F

UserProfile.objects.filter(
    Q(name__startswith='Jo') | Q(name__endswith='Jo')
)

UserProfile.objects.order_by('-dob')
# <QuerySet [<UserProfile: Sajna Mehndi>, <UserProfile: Jasmine Parker>, <UserProfile: Josh Hernandez>, <UserProfile: Dwayne Salazar>, <UserProfile: Steve Ditko>]>

UserProfile.objects.filter(address__contains='H.No')
# <QuerySet [<UserProfile: Josh Hernandez>, <UserProfile: Jasmine Parker>, <UserProfile: Dwayne Salazar>, <UserProfile: Sajna Mehndi>]>

UserProfile.objects.filter(name__contains='j')
# <QuerySet [<UserProfile: Josh Hernandez>, <UserProfile: Jasmine Parker>, <UserProfile: Sajna Mehndi>]>

UserProfile.objects.filter(
    Q(age__gte=21) & Q(age__lt=45)
).order_by('dob')
# <QuerySet [<UserProfile: Dwayne Salazar>, <UserProfile: Josh Hernandez>, <UserProfile: Jasmine Parker>]>
