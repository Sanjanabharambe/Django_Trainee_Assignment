from django.db import transaction
from myapp.models import MainModel, SignalModel

with transaction.atomic():
    MainModel.objects.create(name="RollbackMe")
    print("MainModel created. Now forcing rollback.")
    transaction.set_rollback(True)


print("MainModel count:", MainModel.objects.count())
print("SignalModel count:", SignalModel.objects.count())
