from django.shortcuts import render
from django.urls import reverse_lazy
from account.decorators import login_required
from .models import Attendance
from django.views import generic
from .forms import AttendanceForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from django.db import models
from django.db.models import Count

#404 error handling
def custom_404_view(request, exception):
    return render(request, 'app/404.html')

@login_required
def index(request):
    attendance_form = AttendanceForm()
    all_attendance=Attendance.objects.all()
    return render(request,'app/index.html',{'all_attendance':all_attendance,'attendance_form':attendance_form})


@method_decorator(login_required, name='dispatch')
class AttendanceListView(generic.ListView):
    model = Attendance
    template_name = 'app/tables.html'
    context_object_name = 'all_attendance'


@method_decorator(login_required, name='dispatch')
class AttendanceCreateView(generic.CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'app/attendance_from.html'
    success_url = reverse_lazy('app:attendance_create')  
   
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.warning(self.request, f"Error in {error}")
        return super().form_invalid(form)


@login_required
def chart(request):
    return render(request,'app/charts.html')



class AttendanceReport(APIView):
    def get(self, request):
        report_type = request.query_params.get('type', 'weekly')
        today = timezone.now().date()

        if report_type == 'weekly':
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')

            if not start_date or not end_date:
                start_date = today - timezone.timedelta(days=today.weekday())
                end_date = today

            attendances = Attendance.objects.filter(date__gte=start_date, date__lte=end_date)
        
        else:  
            month = request.query_params.get('month')

            if not month:
                month = today.month
            
            start_date = today.replace(day=1, month=int(month))
            end_date = (start_date + timezone.timedelta(days=31)).replace(day=1) - timezone.timedelta(days=1)

            attendances = Attendance.objects.filter(date__gte=start_date, date__lte=end_date)

        data = attendances.values('date').annotate(present_count=Count('id', filter=models.Q(is_present=True)))

        return Response(data)





