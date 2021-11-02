from django.shortcuts import render
from .form import EmailSubscriberForm, ApplyCandidates
import datetime as dt


def StoreSubscribeMails(emails):
    with open(r"Events\MailBoxes\SubscribeMails.csv", "a") as maildetail:
        maildetail.write(str(emails) + ",\n")


def StoreApllyCandidates(details):
    print(details)
    values = details.values()
    final_details = ''
    for _ in values:
        final_details += str(_) + ','
    with open(r"Events\MailBoxes\AppliedCandidates.csv", "a") as applydetails:
        applydetails.write(final_details + ",\n")


all_details = {'full_name', 'gender', 'email', 'dob', 'state', 'college_name', 'degree_level', 'degree_program',
               'graduation_date', 'video'}


# Create your views here.
def event_page(request):
    if request.method == "POST":
        subscriber_form = EmailSubscriberForm(request.POST)
        application_form = ApplyCandidates(request.POST)
        if subscriber_form.is_valid():
            mails = subscriber_form.cleaned_data['subscriber_mail']
            StoreSubscribeMails(mails)
            result = "Subscribed, See You Again!"
            return render(request, "Events/html/EventPage.html", {'result': result})
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
                StoreApllyCandidates(details)
                result = "AEnter Detail Carefully"
                return render(request, "Events/html/EventPage.html", {'result': result})
            border = dict()
            border = border.fromkeys(wrong_details, 'border-color: red;')
            result = ""
            return render(request, "Events/html/EventPage.html",
                          {'result': result, 'details': details, 'border': border})

        if not (subscriber_form.is_valid() or application_form.is_valid()):
            result = "Enter Detail Carefully!"
            return render(request, "Events/html/EventPage.html", {'result': result})
    else:
        return render(request, "Events/html/EventPage.html")
