from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from Repository.models import Questions ,Submissions
from Repository.serializers import QuestionSerializer , SubmissionSerializer

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):
        qs = Questions.objects.all() # collection of questions

        serializer_instance = QuestionSerializer(qs,many = True)
        # many = True -> tells the serialzer that the input contains multiple objects.

        return Response(serializer_instance.data)
        # returns the serialized data as a response

    def post(self,request):
        form_data = request.data
        serializer_instance = QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Questions.objects.create(**actual_data)
            return Response(data= serializer_instance.data)
        else:
            return Response(data= serializer_instance.errors)

class QuestionRetrieveUpdateDelete(APIView):
    def get(self,request,pk):                               # pk is the primary key of the question to retrieve
        qs= Questions.objects.get(id = pk)                  # get the qn object with the given pk
        serializer_instance = QuestionSerializer(qs)        # serialize the qs
        return Response(data = serializer_instance.data)    # retruns the serialized data as response

    def put(self,request,pk):
        form_data = request.data                                        # gets the data
        serializer_instance = QuestionSerializer(data = form_data)      # passes the data within the serializer
        if serializer_instance.is_valid():                              # checks if the data is valid
            actual_data = serializer_instance.validated_data            # the validated data is passed to a variable actual_data 
            Questions.objects.filter(id=pk).update(**actual_data)       # filters out the qn that needs to be updated and updates
            return Response(data = serializer_instance.data)            # returns the data as a response
        else:
            return Response(data=serializer_instance.errors)            # if the data is not valid it returns error as response

    def delete(self,request,pk):
        Questions.objects.filter(id=pk).delete()                    # filters out the qn that needs to be deleted
        return Response(data = {"message" : "question deleted"})    # returns the data as a response
    


class SubmissionsListCreateView(APIView):
    def get(self,request):
        qs = Submissions.objects.all()
        serializer_instance = SubmissionSerializer(qs,many = True)
        return Response(data = serializer_instance.data)