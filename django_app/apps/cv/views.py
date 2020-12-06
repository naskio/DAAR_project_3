from .forms import ResumeForm
from django.shortcuts import render
from .models import Resume
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from .documents import ResumeDocument
from .serializers import SearchQuerySerializer, ResumeSerializer


def resume_view(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your CV has been uploaded successfully.')
            return redirect('/')
    else:
        form = ResumeForm()
    return render(request, 'index.html', {'form': form})


class SearchViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SearchQuerySerializer

    def list(self, request):
        serializer = self.serializer_class(data=request.query_params)  # or request.GET
        serializer.is_valid(raise_exception=True)
        terms = serializer.validated_data.get('q').split(',')
        if terms:
            queryset = None
            for term in terms:
                if queryset is not None:
                    queryset &= ResumeDocument.search().query("match", text=term).to_queryset()
                else:
                    queryset = ResumeDocument.search().query("match", text=term).to_queryset()
                    print(queryset)
        else:
            queryset = Resume.objects.all()
        serializer = ResumeSerializer(queryset, many=True)
        return Response(serializer.data)


class ResumeViewSet(mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ResumeSerializer
    queryset = Resume.objects

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (AllowAny,)
        return super(ResumeViewSet, self).get_permissions()
