import sys
sys.path.append('../../')
from config.wsgi import *
from core.erp.models import Type, Employee

#Listar
query = Type.objects.all()
print(query)

#Insert
# t = Type()
# t.name = 'Prueba AAA'
# t.save()

#t = Type(name='Prueba 2').save()

# update
# try:
#     t = Type.objects.get(id=1)
#     t.name = 'Prueba editato'
#     t.save()
# except Exception as e:
#     print(e)

# delete
# t = Type.objects.get(pk=1)
# t.delete()

# Listar con filtros
# obj = Type.objects.filter(name__contains='prue')
# obj = Type.objects.filter(name__icontains='prue')
# obj = Type.objects.filter(name__startswith='P')
# obj = Type.objects.filter(name__endswith='2')
# obj = Type.objects.filter(name__in=['Prueba 2', 'prue']).query
# obj = Type.objects.filter(name__icontains='prue').exclude(id=2)
#
# for i in Type.objects.filter(name__icontains='prue')[:1]:
#     print(i.name)

obj = Employee.objects.filter(type_id=1)
print(obj)