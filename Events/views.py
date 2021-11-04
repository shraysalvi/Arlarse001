from django.shortcuts import render
from .form import FormEmailSubscriber, FormApplyCandidates
import datetime as dt
from .models import EmailSubscriberForm, ApplyCandidates

all_details = {'full_name', 'gender', 'email', 'dob', 'state', 'college_name', 'degree_level', 'degree_program',
               'graduation_date', 'video'}


# Create your views here.
def event_page(request):
    if request.method == "POST":
        subscriber_form = FormEmailSubscriber(request.POST)
        application_form = FormApplyCandidates(request.POST)
        if "subscribe_form" in request.POST:
            if subscriber_form.is_valid():
                mails = subscriber_form.cleaned_data['subscriber_mail']
                x = EmailSubscriberForm(subscriber_mail=mails)
                x.save()
                result = "Subscribed, See You Again!"
                return render(request, "Events/html/event_page.html", {'result': result})
            else:
                result = "Enter Mail Carefully!"
                return render(request, "Events/html/event_page.html", {'result': result, 'reponse_color': 'red'})
        if 'applyform' in request.POST:
            if application_form.is_valid():
                details = application_form.cleaned_data
                valid_age = (dt.date.today() - details['dob']) > dt.timedelta(days=5840)
                graduation_valid_age = dt.timedelta(days=5840) < (
                        details['graduation_date'] - details['dob']) < dt.timedelta(days=10950)
                correct_details = set()
                for _ in details:
                    correct_details.add(_)
                wrong_details = all_details - correct_details
                if valid_age is False:
                    wrong_details.add('dob')
                if graduation_valid_age is False:
                    wrong_details.add('graduation_date')
                if len(wrong_details) == 0:
                    save_applycandidate = ApplyCandidates(full_name=details['full_name'], gender=details['gender'],
                                                          email=details['email'], dob=details['dob'],
                                                          state=details['state'],
                                                          college_name=details['college_name'],
                                                          degree_level=details['degree_level'],
                                                          degree_program=details['degree_program'],
                                                          graduation_date=details['graduation_date'],
                                                          video=details['video'])
                    save_applycandidate.save()
                    result = "Applied Successful! We will contact You soon"
                    return render(request, "Events/html/event_page.html", {'result_applycandidate': result})
                else:
                    border = dict()
                    border = border.fromkeys(wrong_details, 'border-color: red;')
                    result = "Enter Your Details Carefully!"
                    return render(request, "Events/html/event_page.html",
                                  {'result_applycandidate': result, 'details': details, 'border': border,
                                   'reponse_color': 'red'})
            else:
                result = "Enter Your Details Carefully!"
                return render(request, "Events/html/event_page.html",
                              {'result_applycandidate': result, 'reponse_color': 'red'})
    else:
        return render(request, "Events/html/event_page.html")
