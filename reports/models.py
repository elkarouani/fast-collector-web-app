from django.db import models

class Employee(models.Model):
    matricule = models.IntegerField()
    first_name = models.CharField(max_length=50, default="Not defined")
    last_name = models.CharField(max_length=50, default="Not defined")
    is_collector = models.BooleanField(default=False)
    still_working = models.BooleanField(default=True)
    is_new = models.BooleanField(default=True)
    salary = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self): return "[{}]: {} {}".format(self.matricule, self.last_name, self.first_name)

class Report(models.Model):
    work_date = models.DateField(auto_now=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self): return "[{}]: {}".format(self.employee.matricule, self.work_date)
