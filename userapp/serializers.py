from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

/



# in pthon manage.py shell

# >>> from userapp.serializers import StudentSerializer 
# >>> student_data={"name":"vishal","age":22}
# >>> serializer=StudentSerializer(student_data)
# >>> print(serializer.data
# >>> print(serializer.data)  
# output:: 'vishal', 'age': 22}
