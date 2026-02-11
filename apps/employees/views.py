from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer

from rest_framework.permissions import IsAdminUser

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, methods=['get'])
    def attendance(self, request, pk=None):
        employee = self.get_object()
        records = employee.attendance_records.all()
        serializer = AttendanceSerializer(records, many=True)
        return Response(serializer.data)


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related('employee').all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()
        employee_id = self.request.query_params.get('employee_id')
        date = self.request.query_params.get('date')

        if employee_id:
            queryset = queryset.filter(employee__employee_id=employee_id)

        if date:
            queryset = queryset.filter(date=date)

        return queryset
