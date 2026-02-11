from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} ({self.employee_id})"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('employee', 'date')
        ordering = ['-date']

    def save(self, *args, **kwargs):
        if self.date.weekday() in [5, 6]:
            raise ValueError("Cannot mark attendance on Saturday or Sunday.")
        super().save(*args, **kwargs)
