from django.shortcuts import render, redirect
from datetime import datetime
import pytz
total_time_package = datetime.now(pytz.timezone("Africa/Lagos"))
# import modal here
from skillhub.models import *
from django.contrib import messages # this is messaging users
from django.contrib.auth.hashers import make_password # hash password
from dateutil.parser import parse

from django.contrib.auth.decorators import login_required
# checking for authentication (Are you logged in?)
from django.db.models import Sum

# Below is for API's
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import SignupSerializer

# Create your views here.
def landing_page(request):
    return render(request, 'index.html')
@login_required(login_url ='/login')
def courses_page(request):
    return render(request, 'courses.html')
def about_page(request):
    return render(request, 'about.html')
def contact_page(request):
    return render(request, 'contact.html')
def sign_up_page(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        # phone = request.POST.get('phone')
        # dob = request.POST.get('dob')
        # ph = request.POST.get('ph')
        # gender = request.POST.get('gender')
        # location = request.POST.get('location')
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')
        get_subject = request.POST.get('subject')
        
        if User.objects.filter(username = get_username).exists() or User.objects.filter(email = email).exists():
            messages.info(request, "Email or Username already exists in our dashboard!! Login instead.")
            return redirect('/login')
        else:
            auth_user_submit = User.objects.create_user(password=get_password, is_superuser=0, username=get_username, first_name=full_name, email=email)
            auth_user_submit.save()
            
            if "fileToUpload" in request.FILES:
                get_passport = request.FILES['fileToUpload']
            else:
                get_passport = "abc.jpg"
                
            signup_submit = SignUp.objects.create(passport=get_passport, name=full_name, email=email, username=get_username, is_superuser= 0, subject=get_subject, user=auth_user_submit)
            signup_submit.save()
            
            messages.info(request, f"{full_name}, Thank you for registering with us. You will be redirected to login page.")
            return redirect('/login')   
    else:
       return render(request, 'signup.html')
  
def login_page(request):
    if request.method == "POST":
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')
        user = auth.authenticate(username=get_username, password=get_password)
        
        if user is None:
            messages.info(request, f"{get_username}, Username or password is incorrect, you can try signing up if you haven't.")
            return redirect("/login")
        else: 
            auth.login(request, user) 
            get_username = request.user
            get_superuser = get_username.is_superuser
            get_signup_row = SignUp.objects.get(username=get_username)
            get_status = get_signup_row.status
            
            if get_status == "block":
                messages.info(request, "Your account has been blocked please contact support@facebook.com")
                return render(request, 'login.html')
            else: 
                if get_superuser == 1:
                    return redirect("/admin_dashboard")
                else:
                    return redirect("/user_dashboard")
    else:
        return render(request, 'login.html')
    
def logout_page(request):
    auth.logout(request)
    return redirect ('/login')

@login_required(login_url='/login')
def user_dashboard_page(request):
    return render(request, 'user_dashboard.html')

@login_required(login_url='/login')
def edit_profile_page(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        old_image = request.POST.get('old_image')
        get_email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob1 = request.POST.get('dob')
        dob = parse(dob1)
        ph = request.POST.get('ph')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        get_username = request.POST.get('username')
        get_subject = request.POST.get('subject')
        
        if 'fileToUpload' in request.FILES:
            get_passport = request.FILES['fileToUpload']
        else:
            get_passport = old_image.replace('/media/', '')
            
        user__identity = User.objects.get(id=id)
        user__identity.username = get_username
        user__identity.first_name = name
        user__identity.email = get_email
        user__identity.save()
            
        signup_identity = SignUp.objects.get(user_id=id)
        signup_identity.name = name
        signup_identity.email = get_email
        signup_identity.phone = phone
        signup_identity.dob = dob
        signup_identity.ph = ph
        signup_identity.gender = gender
        signup_identity.location = location
        signup_identity.username = get_username
        signup_identity.passport = get_passport
        signup_identity.subject = get_subject
        signup_identity.save()
        messages.info(request, "Your profile has been updated")
        return redirect("/user_dashboard")
    
    else:
        return render(request, 'edit_profile.html')

@login_required(login_url ='/login')
def web_dev_page(request):
    return render(request, 'courses/webdev.html')

@login_required(login_url ='/login')
def graphic_design_page(request):
    return render(request, 'courses/gdesign.html')

@login_required(login_url ='/login')  
def mobile_app_page(request):
    return render(request, 'courses/mobile_app_dev.html')

@login_required(login_url ='/login')
def data_science_page(request):
    return render(request, 'courses/data_science.html')

@login_required(login_url ='/login')
def business_marketing_page(request):
    return render(request, 'courses/business.html')

@login_required(login_url ='/login')
def programming_page(request):
    return render(request, 'courses/programming.html')

@login_required(login_url ='/login')
def computer_page(request):
    return render(request, 'courses/computer.html')

@login_required(login_url ='/login')
def ui_ux_page(request):
    return render(request, 'courses/ui_ux.html')

@login_required(login_url ='/login')
def instructors_page(request):
    return render(request, 'instructors.html')

@login_required(login_url ='/login')
def html_fundamentals_page(request):
    return render(request, 'web_development/html_fund.html')

@login_required(login_url ='/login')
def css_basics_page(request):
    return render(request, 'web_development/css_basics.html')

@login_required(login_url ='/login')
def js_fund_page(request):
    return render(request, 'web_development/js_fund.html')

@login_required(login_url ='/login')
def bootstrap_page(request):
    return render(request, 'web_development/bootstrap.html')

@login_required(login_url ='/login')
def advanced_js_page(request):
    return render(request, 'web_development/advancedjs.html')

@login_required(login_url ='/login')
def react_page(request):
    return render(request, 'web_development/react_js.html')

@login_required(login_url ='/login')
def django_page(request):
    return render(request, 'web_development/django.html')

@login_required(login_url ='/login')
def node_js_page(request):
    return render(request, 'web_development/node_js.html')

@login_required(login_url ='/login')
def fullstack_page(request):
    return render(request, 'web_development/fullstack.html')

@login_required(login_url ='/login')
def html_fund_mod1_page(request):
    return render(request, 'web_development/web_dev_modules/html_mod1.html')

@login_required(login_url ='/login')
def html_fund_mod2_page(request):
    return render(request, 'web_development/web_dev_modules/html_mod2.html')

@login_required(login_url ='/login')
def html_fund_mod3_page(request):
    return render(request, 'web_development/web_dev_modules/html_mod3.html')

@login_required(login_url ='/login')
def html_fund_mod4_page(request):
    return render(request, 'web_development/web_dev_modules/html_mod4.html')

@login_required(login_url ='/login')
def html_fund_mod5_page(request):
    return render(request, 'web_development/web_dev_modules/html_mod5.html')

@login_required(login_url ='/login')
def html_fund_mod6_page(request):
    return render(request, 'web_development/web_dev_modules/html_mod6.html')

@login_required(login_url ='/login')
def html_fund_mod7_page(request):
    return render(request, 'web_development/web_dev_modules/html_mod7.html')

@login_required(login_url ='/login')
def html_fund_mod8_page(request):
    return render(request, 'web_development/web_dev_modules/html_mod8.html')

@login_required(login_url ='/login')
def html_fund_mod9_page(request):
    return render(request, 'web_development/web_dev_modules/html_mod9.html')

@login_required(login_url ='/login')
def html_fund_mod10_page(request):
    return render(request, 'web_development/web_dev_modules/html_mod10.html')

@login_required(login_url ='/login')
def css_basics_mod1_page(request):
    return render(request, 'web_development/web_dev_modules/css_mod1.html')

@login_required(login_url ='/login')
def css_basics_mod2_page(request):
    return render(request, 'web_development/web_dev_modules/css_mod2.html')

@login_required(login_url ='/login')
def css_basics_mod3_page(request):
    return render(request, 'web_development/web_dev_modules/css_mod3.html')

@login_required(login_url ='/login')
def css_basics_mod4_page(request):
    return render(request, 'web_development/web_dev_modules/css_mod4.html')

@login_required(login_url ='/login')
def css_basics_mod5_page(request):
    return render(request, 'web_development/web_dev_modules/css_mod5.html')

@login_required(login_url ='/login')
def css_basics_mod6_page(request):
    return render(request, 'web_development/web_dev_modules/css_mod6.html')

@login_required(login_url ='/login')
def css_basics_mod7_page(request):
    return render(request, 'web_development/web_dev_modules/css_mod7.html')

@login_required(login_url ='/login')
def js_fund_mod1_page(request):
    return render(request, 'web_development/web_dev_modules/js_mod1.html')

@login_required(login_url ='/login')
def js_fund_mod2_page(request):
    return render(request, 'web_development/web_dev_modules/js_mod2.html')

@login_required(login_url ='/login')
def js_fund_mod3_page(request):
    return render(request, 'web_development/web_dev_modules/js_mod3.html')

@login_required(login_url ='/login')
def js_fund_mod4_page(request):
    return render(request, 'web_development/web_dev_modules/js_mod4.html')

@login_required(login_url ='/login')
def js_fund_mod5_page(request):
    return render(request, 'web_development/web_dev_modules/js_mod5.html')

@login_required(login_url ='/login')
def js_fund_mod6_page(request):
    return render(request, 'web_development/web_dev_modules/js_mod6.html')

@login_required(login_url ='/login')
def bootstrap_mod1_page(request):
    return render(request, 'web_development/web_dev_modules/bootstrap_mod1.html')

@login_required(login_url ='/login')
def bootstrap_mod2_page(request):
    return render(request, 'web_development/web_dev_modules/bootstrap_mod2.html')

@login_required(login_url ='/login')
def bootstrap_mod3_page(request):
    return render(request, 'web_development/web_dev_modules/bootstrap_mod3.html')

@login_required(login_url ='/login')
def bootstrap_mod4_page(request):
    return render(request, 'web_development/web_dev_modules/bootstrap_mod4.html')

@login_required(login_url ='/login')
def bootstrap_mod5_page(request):
    return render(request, 'web_development/web_dev_modules/bootstrap_mod5.html')

@login_required(login_url ='/login')
def advancedjs__mod1_page(request):
    return render(request, 'web_development/web_dev_modules/advancedjs_mod1.html')

@login_required(login_url ='/login')
def advancedjs__mod2_page(request):
    return render(request, 'web_development/web_dev_modules/advancedjs_mod2.html')

@login_required(login_url ='/login')
def advancedjs__mod3_page(request):
    return render(request, 'web_development/web_dev_modules/advancedjs_mod3.html')

@login_required(login_url ='/login')
def advancedjs__mod4_page(request):
    return render(request, 'web_development/web_dev_modules/advancedjs_mod4.html')

@login_required(login_url ='/login')
def advancedjs__mod5_page(request):
    return render(request, 'web_development/web_dev_modules/advancedjs_mod5.html')

@login_required(login_url ='/login')
def advancedjs__mod6_page(request):
    return render(request, 'web_development/web_dev_modules/advancedjs_mod6.html')

# =========================================================== ADMIN ======================================================================
def admin_signup_page(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        ph = request.POST.get('ph')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')
        
        if User.objects.filter(username = get_username).exists() or User.objects.filter(email = email).exists():
            messages.info(request, "Email or Username already exists in our dashboard!! Login instead.")
            return redirect('/login')
        else:
            auth_user_submit = User.objects.create_user(password=get_password, is_superuser=1, username=get_username, first_name=full_name, email=email)
            auth_user_submit.save()
            
            if "fileToUpload" in request.FILES:
                get_passport = request.FILES['fileToUpload']
            else:
                get_passport = "abc.jpg"
                
            signup_submit = SignUp.objects.create(passport=get_passport, name=full_name, email=email, phone=phone, dob=dob, ph=ph, gender=gender, location=location, username=get_username, is_superuser= 1, user=auth_user_submit)
            signup_submit.save()
            
            messages.info(request, f"{full_name}, you have successfully registered as an admin.")
            return redirect('/login')   
    else:
       return render(request, 'admin_signup.html')
   
def logout_page(request):
    auth.logout(request)
    return redirect ('/login')
 
@login_required(login_url='/login')  
def admin_dashboard_page(request):
    return render(request, 'admin_dashboard.html')

@login_required(login_url='/login')
def admin_editprofile_page(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        old_image = request.POST.get('old_image')
        get_email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob1 = request.POST.get('dob')
        dob = parse(dob1)
        ph = request.POST.get('ph')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        get_username = request.POST.get('username')
        
        if 'fileToUpload' in request.FILES:
            get_passport = request.FILES['fileToUpload']
        else:
            get_passport = old_image.replace('/media/', '')
            
        user__identity = User.objects.get(id=id)
        user__identity.username = get_username
        user__identity.first_name = name
        user__identity.email = get_email
        user__identity.save()
            
        signup_identity = SignUp.objects.get(user_id=id)
        signup_identity.name = name
        signup_identity.email = get_email
        signup_identity.phone = phone
        signup_identity.dob = dob
        signup_identity.ph = ph
        signup_identity.gender = gender
        signup_identity.location = location
        signup_identity.username = get_username
        signup_identity.passport = get_passport
        signup_identity.save()
        messages.info(request, "Your profile has been updated")
        return redirect("/admin_dashboard")
    
    else:
        return render(request, 'admin_edit_profile.html')
