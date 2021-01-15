from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from table.models import timetable
from table.models import students
from table.models import subject_link


def common_member(a, b): 
    a_set = set(a)
    b_set = set(b)
    return list(a_set & b_set)
    

        
def converttomin(hrs,min):
    return (hrs*60)+min
@csrf_exempt
def base(request):
    context = {}
    context['link']="#"
    context['lecture']=""
    return render(request, 'timetable/base.html',context)

@csrf_exempt
def tt(request):
    context = {}
    if request.POST:
        if request.POST['roll_no'] != '':
            roll_no= request.POST['roll_no']
            hours=request.POST['hours']
            minute=request.POST['minute']
            day=request.POST['day']
            ct= converttomin(int(hours),int(minute))
            subjects = timetable.objects.values_list('Subject', flat=True).filter(Day=day).filter(start_time_min__lte=int(ct)).filter(end_time_min__gte=int(ct))
            all_subj = timetable.objects.values_list('Subject', flat=True).filter(Day=day)
            student_subjects= students.objects.values_list('Subject',flat=True).filter(roll_no = int(roll_no))
            td_sub = common_member(list(all_subj),list(student_subjects))
            subject = common_member(list(subjects),list(student_subjects))
            print(list(subjects))
            print(list(student_subjects))
            context['td_sub']= td_sub
            try:
                context['lecture']=subject[0]
            except:
                context['lecture']="Hurray No lecture"
            try:
                context['link']=(subject_link.objects.filter(Subject=subject[0]))[0].link
            except:
                context['link']="#"
            
            json_object = json.dumps(context, indent = 4)
            return HttpResponse(json_object, content_type='application/json')
    

def studentfill(request):
    if request.POST:
        print(request.POST)
        sub = []
        if request.POST['roll_no']!='':
            roll_no= request.POST['roll_no']
            sub.append(request.POST['IOT'])
            sub.append(request.POST['IOTL'])
            sub.append(request.POST['OB'])
            sub.append(request.POST['PE_2'])
            sub.append(request.POST['PE_2L'])
            sub.append(request.POST['OE'])
            sub.append(request.POST['PE_3'])
            sub.append(request.POST['PE_3L'])
            sub.append(request.POST['ES'])
            sub.append(request.POST['ESL'])
            try:
                rno = students.objects.filter(roll_no = roll_no)
                if len(rno):
                    i = 0;
                    for s in rno:
                        s.Subject = sub[i]
                        s.save()
                        i=i+1
                else:
                    for s in sub:
                        b= students(roll_no =roll_no,Subject = s)
                        b.save()
            except:
                pass
            return redirect('/')    
                
    return render(request, 'timetable/studentform.html')              



def linkfill(request):
    if request.POST:
        print(request.POST)
        if request.POST['KEY'] == 'Qwerty123@':
            subject= request.POST['subject']
            link  = request.POST['link']
            try:
                s=subject_link.objects.filter(Subject = subject)
                if len(s):
                    s[0].link= link
                    s[0].save()
                else:
                    s = subject_link(Subject = subject,link = link)
                    s.save()
            except:
                pass
    return render(request,'timetable/linkfill.html')

