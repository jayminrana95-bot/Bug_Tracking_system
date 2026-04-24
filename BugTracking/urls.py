from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='core/password_reset.html'
    ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='core/password_reset_done.html'
    ), name='password_reset_done'),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='core/password_reset_confirm.html'
    ), name='password_reset_confirm'),
      path('reset_done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='core/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('Developer_dashbord/',views.Developer_dashbord,name='Developer_dashbord'),
    path('Project_Manager/',views.ProjectManagerView,name= 'Project_Manager'),
    path("Tester_dashbord/",views.Tester_dashbord,name='Tester_dashbord'),
    #path("Admin_deashbord/",views.Admin_deashbord,name='Admin_deashbord'),
    path("project__created/",views.project__created,name='project__created'),
    path("module__created/",views.module__created,name='module__created'),
    path("task__created/",views.task__created,name='task__created'),
    path("user__role/",views.user__role,name='user__role'),
    path("assigned_page/",views.assigned_page,name='assigned_page'),
    path("Bug_Tracking_Page/",views.Bug_Tracking_Page,name='Bug_Tracking_Page'),
    path("assigned_bug_page/",views.assigned_bug_page,name='assigned_bug_page'),
    path("assigned_by_tester/",views.assigned_by_tester,name='assigned_by_tester'),
    path("comment_page/",views.comment_page,name='comment_page'),
    path("comment_list/",views.comment_list,name='comment_list'),
    path("User_list/",views.User_list,name='User_list'),
    path("project_list/",views.project_list,name='project_list'),
    path("Moduel_list/",views.Moduel_list,name='Moduel_list'),
    path("Task_list/",views.Task_list,name='Task_list'),
    path("Bug_creat_list/",views.Bug_creat_list,name='Bug_creat_list'),
    path("Assigned_by_tester_list/",views.Assigned_by_tester_list,name='Assigned_by_tester_list'),
    path('delete_user/<str:user_id>/', views.delete_user, name='delete_user'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('assigned_list/', views.assigned_list, name='assigned_list'),
    path('assigned_bug1_list/', views.assigned_bug1_list, name='assigned_bug1_list'),
    path('delete_assigned_bug/<int:id>/', views.delete_assigned_bug, name='delete_assigned_bug'),
    path('delete_project/<str:project_id>/', views.delete_project, name='delete_project'),
    path('delete_module/<str:module_id>/', views.delete_module, name='delete_module'),
    path('delete_task/<str:task_id>/', views.delete_task, name='delete_task'),
    path('delete-bug/<int:id>/', views.delete_bug, name='delete_bug'),
    path('delete_assigned_bugtester/<int:id>/', views.delete_assigned_bugtester, name='delete_assigned_bugtester'),
    path('delete_comment/<str:comment_id>/', views.delete_comment, name='delete_comment'),
    path('delete_assigned/<int:id>/', views.delete_assigned, name='delete_assigned'),
    #this is a update path
    path('Update_user/<str:user_id>/', views.update_user, name='Update_user'),
    path('Update_project/<str:project_id>/', views.update_project, name='Update_project'),
    path('Update_module/<str:module_id>/', views.update_module, name='Update_module'),
    path('Update_task/<str:task_id>/', views.update_task, name='Update_task'),
    path('Update_assigned/<int:id>/', views.update_assigned, name='Update_assigned'),
    path('Update_created_bug/<int:id>/', views.update_created_bug, name='Update_created_bug'),
    path('Update_assigned_bug/<int:id>/', views.update_assigned_bug, name='Update_assigned_bug'),
    path('Update_assigned_to_tester/<int:id>/', views.update_assigned_to_tester, name='Update_assigned_to_tester'),
    path('Update_comment/<str:comment_id>/',views.update_comment, name='Update_comment'),
   
]


