"""
URL configuration for learning_program project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from skillhub import views

# for images upload as well
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page),
    path('courses', views.courses_page),
    path('about', views.about_page),
    path('contact', views.contact_page),
    path('sign_up', views.sign_up_page),
    path('login', views.login_page),
    path('user_dashboard', views.user_dashboard_page),
    path('edit_profile/<int:id>', views.edit_profile_page),
    path('logout', views.logout_page),
    path('admin_signup', views.admin_signup_page),
    path('admin_dashboard', views.admin_dashboard_page),
    path('admin_edit_profile/<int:id>', views.admin_editprofile_page),
    path('web_dev', views.web_dev_page),
    path('gdesign', views.graphic_design_page),
    path('mobile_app', views.mobile_app_page),
    path('data_science', views.data_science_page),
    path('business', views.business_marketing_page),
    path('programming_basics', views.programming_page),
    path('computer_basics', views.computer_page),
    path('ui_ux', views.ui_ux_page),
    path('instructors', views.instructors_page),
    path('html_fund', views.html_fundamentals_page),
    path('css_basics', views.css_basics_page),
    path('js_fund', views.js_fund_page),
    path('bootstrap', views.bootstrap_page),
    path('advanced_js', views.advanced_js_page),
    path('react', views.react_page),
    path('django', views.django_page),
    path('node', views.node_js_page),
    path('fullstack', views.fullstack_page),
    path('html_fundamental_module1', views.html_fund_mod1_page),
    path('html_fundamental_module2', views.html_fund_mod2_page),
    path('html_fundamental_module3', views.html_fund_mod3_page),
    path('html_fundamental_module4', views.html_fund_mod4_page),
    path('html_fundamental_module5', views.html_fund_mod5_page),
    path('html_fundamental_module6', views.html_fund_mod6_page),
    path('html_fundamental_module7',views.html_fund_mod7_page),
    path('html_fundamental_module8',views.html_fund_mod8_page),
    path('html_fundamental_module9',views.html_fund_mod9_page),
    path('html_fundamental_module10',views.html_fund_mod10_page),
    path('css_basics_module1',views.css_basics_mod1_page),
    path('css_basics_module2',views.css_basics_mod2_page),
    path('css_basics_module3',views.css_basics_mod3_page),
    path('css_basics_module4',views.css_basics_mod4_page),
    path('css_basics_module5',views.css_basics_mod5_page),
    path('css_basics_module6',views.css_basics_mod6_page),
    path('css_basics_module7',views.css_basics_mod7_page),
    path('js_fundamental_module1',views.js_fund_mod1_page),
    path('js_fundamental_module2',views.js_fund_mod2_page),
    path('js_fundamental_module3',views.js_fund_mod3_page),
    path('js_fundamental_module4',views.js_fund_mod4_page),
    path('js_fundamental_module5',views.js_fund_mod5_page),
    path('js_fundamental_module6',views.js_fund_mod6_page),
    path('bootstrap_module1',views.bootstrap_mod1_page),
    path('bootstrap_module2',views.bootstrap_mod2_page),
    path('bootstrap_module3', views.bootstrap_mod3_page),
    path('bootstrap_module4', views.bootstrap_mod4_page),
    path('bootstrap_module5', views.bootstrap_mod5_page),
    path('advancedjs_module1', views.advancedjs__mod1_page),
    path('advancedjs_module2', views.advancedjs__mod2_page),
    path('advancedjs_module3', views.advancedjs__mod3_page),
    path('advancedjs_module4', views.advancedjs__mod4_page),
    path('advancedjs_module5', views.advancedjs__mod5_page),
    path('advancedjs_module6', views.advancedjs__mod6_page),
    
    
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)