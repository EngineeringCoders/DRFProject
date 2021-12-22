from models import Employee
from serializers import EmployeeSerializer
emp = Employee(eno=100,ename='Python',esal=9998,eaddr='Bangalore')
eserialize = EmployeeSerializer(emp)
eserialize.data
