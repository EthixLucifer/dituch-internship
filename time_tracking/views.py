# from django.utils.timezone import now
# from rest_framework import viewsets, status as drf_status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import Entry, Project, Activity, Location, Status as StatusModel
# from .serializers import EntrySerializer, ProjectSerializer, ActivitySerializer, LocationSerializer, StatusSerializer

# class EntryViewSet(viewsets.ModelViewSet):
#     queryset = Entry.objects.all()
#     serializer_class = EntrySerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         """ Clock In: Start a new work entry """
#         user = request.user
#         project = Project.objects.get(id=request.data.get('project'))
#         activity = Activity.objects.get(id=request.data.get('activity'))
#         location = Location.objects.get(id=request.data.get('location'))
#         status = StatusModel.objects.get(id=request.data.get('status'))
#         status_model = StatusModel.objects.get(id=request.data.get('status'))


#         # Check if there's already an active entry
#         active_entry = Entry.objects.filter(user=user, end_time__isnull=True).first()
#         if active_entry:
#             active_entry.end_time = now()
#             active_entry.save()

#         # Create new entry
#         entry = Entry.objects.create(
#             user=user, project=project, activity=activity,
#             location=location, status=status, start_time=now()
#         )
#         # return Response(EntrySerializer(entry).data, status=status.HTTP_201_CREATED)
#         return Response(EntrySerializer(entry).data, status=drf_status.HTTP_201_CREATED)

# def update(self, request, *args, **kwargs):
#     """ Update an entry, including setting the end_time if provided """
#     entry = self.get_object()
#     end_time = request.data.get("end_time")

#     if end_time:
#         entry.end_time = end_time
#     else:
#         entry.end_time = now()

#     entry.save()
#     return Response(EntrySerializer(entry).data)

# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]

# class ActivityViewSet(viewsets.ModelViewSet):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer
#     permission_classes = [IsAuthenticated]

# class LocationViewSet(viewsets.ModelViewSet):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer
#     permission_classes = [IsAuthenticated]

# class StatusViewSet(viewsets.ModelViewSet):
#     queryset = StatusModel.objects.all()
#     serializer_class = StatusSerializer
#     permission_classes = [IsAuthenticated]


from django.utils.timezone import now
from rest_framework import viewsets, status as drf_status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Entry, Project, Activity, Location, Status as StatusModel
from .serializers import EntrySerializer, ProjectSerializer, ActivitySerializer, LocationSerializer, StatusSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """ Clock In: Start a new work entry """
        user = request.user
        project = Project.objects.get(id=request.data.get('project'))
        activity = Activity.objects.get(id=request.data.get('activity'))
        location = Location.objects.get(id=request.data.get('location'))
        status = StatusModel.objects.get(id=request.data.get('status'))

        # Check if there's already an active entry
        active_entry = Entry.objects.filter(user=user, end_time__isnull=True).first()
        if active_entry:
            active_entry.end_time = now()
            active_entry.save()

        # Create new entry
        entry = Entry.objects.create(
            user=user, project=project, activity=activity,
            location=location, status=status, start_time=now()
        )
        return Response(EntrySerializer(entry).data, status=drf_status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """ Update an entry, including setting the end_time if provided """
        entry = self.get_object()
        end_time = request.data.get("end_time")

        if end_time:
            entry.end_time = end_time
        else:
            entry.end_time = now()

        entry.save()
        return Response(EntrySerializer(entry).data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

class StatusViewSet(viewsets.ModelViewSet):
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]