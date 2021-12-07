from rest_framework import generics, response
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.serializers import *


class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentSerializer


class InstructorCreateView(generics.CreateAPIView):
    serializer_class = InstructorSerializer


class GroupCreateView(generics.CreateAPIView):
    serializer_class = GroupSerializer


class ScheduleCreateView(generics.CreateAPIView):
    serializer_class = ScheduleSerializer


class ScheduleStudentView(APIView):
    def get(self, request):
        student = request.GET.get("student")
        schedule = Schedule.objects.filter(student=student)
        serializer = ScheduleDetailSerializer(schedule, many=True)
        return Response(serializer.data)


class ScheduleInstructorView(APIView):
    def get(self, request):
        instructor = request.GET.get("instructor")
        schedule = Schedule.objects.filter(instructor=instructor)
        serializer = ScheduleDetailSerializer(schedule, many=True)
        return Response(serializer.data)


class ScheduleEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class StudentListView(generics.ListAPIView):
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()


class InstructorListView(generics.ListAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class GroupListView(generics.ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class ScheduleListView(generics.ListAPIView):
    serializer_class = ScheduleDetailSerializer
    queryset = Schedule.objects.all()


class StatusListView(generics.ListAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class RequestView(APIView):
    def get(self, request):
        request = Request.objects.all()
        serializer = RequestSerializer(request, many=True)
        return Response(serializer.data)

    def post(self, request):
        request = RequestSerializer(data=request.data)
        if request.is_valid():
            request.save()
            return Response(status=201)
        else:
            return Response(status=400)


class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RequestDetailSerializer
    queryset = Request.objects.all()


class RequestEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()


class StudentEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()
