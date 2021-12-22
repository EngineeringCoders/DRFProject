from rest_framework import serializers
class EmployeeSerializer(serializers.Serializer):
    eno= serializers.IntegerField()
    ename = serializers.CharField(max_length=100)
    esal = serializers.FloatField()
    eaddr = serializers.CharField(max_length=200)
