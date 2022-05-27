from core.models import UserProfile, City, State, College, ElectiveSubject
from django.db.models import Q, F
from django.db.models.aggregates import Sum, Max, Min, Count, Avg

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

UserProfile.objects.get(id=1)
# <UserProfile: Josh Hernandez>

UserProfile.objects.exclude(id__gt=3)
# <QuerySet [<UserProfile: Josh Hernandez>, <UserProfile: Jasmine Parker>, <UserProfile: Dwayne Salazar>]>

UserProfile.objects.aggregate(Sum('age'))
# {'age__sum': 156}

UserProfile.objects.aggregate(Avg('age'))
# {'age__avg': 31.2}

UserProfile.objects.aggregate(Max('age'))
# {'age__max': 48}

UserProfile.objects.aggregate(Min('age'))
# {'age__min': 20}

cities = UserProfile.objects.values('city').annotate(Avg('age'))
# <QuerySet [{'city': 1, 'age__avg': 32.5}, {'city': 2, 'age__avg': 48.0}, {'city': 6, 'age__avg': 23.0}, {'city': 7, 'age__avg': 20.0}]>

for obj in cities:
    City.objects.get(id=obj['city'])

# <City: Hyderabad>
# <City: Lucknow>
# <City: Thane>
# <City: Margao>

UserProfile.objects.annotate(
    age_dbl=F('age')*2).values('id', 'name', 'age', 'age_dbl')
# <QuerySet [{'id': 1, 'name': 'Josh Hernandez', 'age': 24, 'age_dbl': 48}, {'id': 2, 'name': 'Jasmine Parker', 'age': 23, 'age_dbl': 46}, {'id': 3, 'name': 'Dwayne Salazar', 'age': 41, 'age_dbl': 82}, {'id': 4, 'name': 'Sajna Mehndi', 'age': 20, 'age_dbl': 40}, {'id': 5, 'name': 'Steve Ditko', 'age': 48, 'age_dbl': 96}]>

UserProfile.objects.filter(age__gt=30).aggregate(Count('id'))
# {'id__count': 2}

UserProfile.objects.filter(age__lt=30).aggregate(Count('id'))
# {'id__count': 3}

user = UserProfile.objects.get(id=3)
# <UserProfile: Dwayne Salazar>
user.name = 'Dwayne Pietro Salazar'
user.save()
# <UserProfile: Dwayne Pietro Salazar>

UserProfile.objects.update(age=F('age')+1)
# 5

College.objects.values('name', 'city')
# <QuerySet [{'name': 'Goa University', 'city': 3}, {'name': 'Mumbai University', 'city': 4}]>

UserProfile.objects.filter(Q(age__gt=25) & ~ Q(college=4))
# <QuerySet [<UserProfile: Dwayne Pietro Salazar>, <UserProfile: Steve Ditko>]>

College.objects.extra(select={'CollegeName': 'name', 'PhoneNum': 'phone_num'}).values(
    'CollegeName', 'PhoneNum')
# <QuerySet [{'CollegeName': 'Goa University', 'PhoneNum': '8457938458'}, {'CollegeName': 'Mumbai University', 'PhoneNum': '8543213256'}]>

# Queries for Many-to-Many field
user = UserProfile.objects.get(id=3)
# <UserProfile: Dwayne Pietro Salazar>
user.elective.all()
# <QuerySet [<ElectiveSubject: Computer Science>, <ElectiveSubject: Human Machine Interaction>, <ElectiveSubject: Distributed Operating Systems>, <ElectiveSubject: Web Technologies>, <ElectiveSubject: Motion Picture Direction>, <ElectiveSubject: Emotional Health>, <ElectiveSubject: Evolutionary Algorithms>, <ElectiveSubject: Data Structures and Algorithms>]>

elective = ElectiveSubject.objects.get(name='Human Machine Interaction')
# <ElectiveSubject: Human Machine Interaction>
UserProfile.objects.filter(elective=elective.id)           
# <QuerySet [<UserProfile: Steve Ditko>, <UserProfile: Dwayne Pietro Salazar>, <UserProfile: Jasmine Parker>, <UserProfile: Josh Hernandez>]>

electives = ElectiveSubject.objects.filter(Q(name='Computer Science') | Q(id__gt=5) & ~ Q(id__gte=10))                                                                                            
# <QuerySet [<ElectiveSubject: Computer Science>, <ElectiveSubject: Object Oriented Programming>, <ElectiveSubject: Animal Husbandry>, <ElectiveSubject: Motion Picture Direction>, <ElectiveSubject: Modern Fashion Design>]>
eids = [e.id for e in electives]
# [1, 6, 7, 8, 9]
UserProfile.objects.filter(elective__in=eids).aggregate(Count('name'))
# {'name__count': 9}
UserProfile.objects.filter(elective__in=eids)                         
# <QuerySet [<UserProfile: Steve Ditko>, <UserProfile: Dwayne Pietro Salazar>, <UserProfile: Jasmine Parker>, <UserProfile: Sajna Mehndi>, <UserProfile: Jasmine Parker>, <UserProfile: Sajna Mehndi>, <UserProfile: Dwayne Pietro Salazar>, <UserProfile: Jasmine Parker>, <UserProfile: Josh Hernandez>]>

objs = UserProfile.objects.values('elective').annotate(Count('id'))
# <QuerySet [{'elective': 1, 'id__count': 2}, {'elective': 3, 'id__count': 4}, {'elective': 4, 'id__count': 5}, {'elective': 5, 'id__count': 4}, {'elective': 6, 'id__count': 1}, {'elective': 7, 'id__count': 2}, {'elective': 8, 'id__count': 3}, {'elective': 9, 'id__count': 1}, {'elective': 10, 'id__count': 3}, {'elective': 11, 'id__count': 1}, {'elective': 12, 'id__count': 2}, {'elective': 13, 'id__count': 2}, {'elective': 14, 'id__count': 2}]>
max_el = 0
for e in objs:
    if e['id__count'] > max_el:
        max_el = e['elective']
# max_el
# 4
