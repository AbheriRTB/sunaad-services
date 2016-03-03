from django.http import Http404

from program.serializers import ProgramSerializer
from program.models import Program

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

class ProgramList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        programs = Program.objects.all().order_by('event_date')
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer_class = ProgramSerializer
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        program = self.get_object(pk)
        program.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProgramDetail(APIView):
    """
    Retrieve, update or delete a program instance.
    """
    def get_object(self, pk):
        try:
            return Program.objects.get(pk=pk)
        except Program.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        program = self.get_object(pk)
        program = ProgramSerializer(program)
        return Response(program.data)

    def put(self, request, pk, format=None):
        program = self.get_object(pk)
        serializer = ProgramSerializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        program = self.get_object(pk)
        program.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def program(request):
    """ 
    List all programs, or create a new programs.
    """ 
    if request.method == 'GET':
        programs = Program.objects.all()
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


