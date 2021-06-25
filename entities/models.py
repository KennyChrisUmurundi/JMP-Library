from django.db import models
# from django_tenants.models import TenantMixin, DomainMixin
# from library.models import Library




# class Entity(TenantMixin):

#     name = models.CharField(max_length=100)
#     on_trial = models.BooleanField(default=False)
#     created_on = models.DateField(auto_now_add=True)
#     # library = models.ForeignKey(Library,on_delete=models.CASCADE)

#     # default true, schema will be automatically created and synced when it is saved
#     auto_create_schema = True

# class Domain(DomainMixin):
#     pass