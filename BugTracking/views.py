from pyexpat.errors import messages
from urllib import request
from webbrowser import get

from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required

from .models import commentTable, usertable ,assigned_bugtable,assignedtable, projectTable,moduletable, tasktable,bugtrackingtable
from .forms import assigned_bug_update_form, assigned_fix_bug_update_form, assigned_update_form, comment_update_form, project_created,module_created,task_created,user_role,assigned,Bug_Tracking,assigned_bug,assignedtester,comment_Table,user_update_form,project_update_form,module_update_form,task_update_form,bug_update_form
from django.contrib.auth import logout
# Create your views here.


@login_required(login_url='login')
def ProjectManagerView(request):
    return render (request,"BugTracking/Project_Manager.html")

@login_required(login_url='login')
def Developer_dashbord(request):
    return render (request,"BugTracking/Developer_dashbord.html")

@login_required(login_url='login')
def Tester_dashbord(request):
    return render (request,"BugTracking/Tester_dashbord.html")



def project__created(request):
    if request.method == "POST":
        form = project_created(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("module__created")
        else:
            return render(request,'BugTracking/project__created.html',{'form':form})
    else:
       form=project_created()
       return render(request,'BugTracking/project__created.html',{'form':form})

   
  

def module__created(request):
    if request.method == "POST":
        form = module_created(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("task__created")
        else:
            return render(request,'BugTracking/module__created.html',{'form':form})
    else:
        form=module_created()
        return render(request,'BugTracking/module__created.html',{'form':form})



def task__created(request):
    if request.method == "POST":
        form = task_created(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("assigned_page")
        else:
            return render(request,'BugTracking/task__created.html',{'form':form})
    else:
        form=task_created()
        return render(request,'BugTracking/task__created.html',{'form':form})



def user__role(request):
    if request.method == "POST":
        form = user_role(request.POST)

        if form.is_valid():

            # 🔥 check existing record
            obj = usertable.objects.filter(user_id=request.user.id).first()

            if obj:
                # 👉 अगर पहले से है → update करो
                form = user_role(request.POST, instance=obj)
                obj = form.save(commit=False)
            else:
                # 👉 अगर नहीं है → create करो
                obj = form.save(commit=False)
                obj.user_id = request.user.id

            obj.save()

            # 🔁 redirect logic
            if obj.role == "Project Manager":
                return redirect("project__created")
            elif obj.role == "Developer":
                return redirect("Developer_dashbord")
            elif obj.role == "Tester":
                return redirect("Tester_dashbord")
            elif obj.role == "admin":
                return redirect("admin")

        return render(request, 'BugTracking/user__role.html', {"form": form})

    else:
        form = user_role()
        return render(request, 'BugTracking/user__role.html', {"form": form})

def assigned_page(request):
    if request.method == "POST":
        form = assigned(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("Developer_dashbord")
        else:
            return render(request,'BugTracking/assigned_page.html',{'form':form})
    else:
        form=assigned()
        return render(request,'BugTracking/assigned_page.html',{'form':form})
    


def Bug_Tracking_Page(request):
    if request.method == "POST":
        form = Bug_Tracking(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("assigned_bug_page")
        else:
            return render(request,'BugTracking/Bug_Tracking_Page.html',{'form':form})
    else:
        form=Bug_Tracking()
        return render(request,'BugTracking/Bug_Tracking_Page.html',{'form':form})



def assigned_bug_page(request):
    if request.method == "POST":
        form = assigned_bug(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("Developer_dashbord")
        else:
            return render(request,'BugTracking/assigned_bug_page.html',{'form':form})
    else:
        form=assigned_bug()
        return render(request,'BugTracking/assigned_bug_page.html',{'form':form})




def assigned_by_tester(request):
    if request.method == "POST":
        form = assignedtester(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)

            # 1. Use lowercase 'email' (Fixes your first FieldError)
            user_obj = usertable.objects.filter(email=request.user.email).first()

            if not user_obj:
                # 2. Django uses messages.error(request, "message") 
                # This is the correct way to show errors
                from django.contrib import messages
                messages.error(request, "User not found in usertable!")
                return redirect("Tester_dashbord")

            obj.assigned_by = user_obj
            # Ensure 'reported_by' is the correct field name in your model
            obj.bug_reported_by = user_obj 

            obj.save()
            return redirect("Tester_dashbord")

        else:
            # 3. If form is invalid, just pass the form. 
            # Django handles form errors automatically in the template.
            return render(request, 'BugTracking/assigned_by_tester.html', {'form': form})

    else:
        form = assignedtester()
        return render(request, 'BugTracking/assigned_by_tester.html', {'form': form})

def comment_page(request):
    if request.method == "POST":
        form = comment_Table(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("Developer_dashbord")
        else:
            return render(request,'BugTracking/comment_page.html',{'form':form})
    else:
        form=comment_Table()
        return render(request,'BugTracking/comment_page.html',{'form':form})

#this is a list section
def comment_list(request):
    assignedlist2=commentTable.objects.all().order_by("id")

    print(assignedlist2)
    return render (request,"BugTracking/comment_list.html",{"comment_list":assignedlist2})

def User_list(request):
    User_list=usertable.objects.all().order_by("id")

    print(User_list)
    return render (request,"BugTracking/User_list.html",{"User_list":User_list})

def project_list(request):
    project_list= projectTable.objects.all().order_by("id")

    print(project_list)
    return render (request,"BugTracking/project_list.html",{"project_list":project_list})

def Moduel_list(request):
    Moduel_list=moduletable.objects.all().order_by("id")

    print( Moduel_list)
    return render (request,"BugTracking/Moduel_list.html",{"Moduel_list": Moduel_list})

def Task_list(request):
    Task_list=tasktable.objects.all().order_by("id")

    print(Task_list)
    return render (request,"BugTracking/Task_list.html",{"Task_list":Task_list})

def assigned_list(request):
    assgined_list=assignedtable.objects.all().order_by("id")

    print(assgined_list)
    return render (request,"BugTracking/assigned_list.html",{"assigned_list":assgined_list})

def Bug_creat_list(request):
    Bug_creat_list=bugtrackingtable.objects.all().order_by("id")

    print(Bug_creat_list)
    return render (request,"BugTracking/Bug_creat_list.html",{"Bug_creat_list":Bug_creat_list})

def assigned_bug1_list(request):
    assigned_Bug1_list= assigned_bugtable.objects.all().order_by("id")

    print(assigned_Bug1_list)
    return render (request,"BugTracking/assigned_bug1_list.html",{"assigned_bug1_list":assigned_Bug1_list})


def Assigned_by_tester_list(request):
    Assigned_by_tester_list=assigned_bugtable.objects.all().order_by("id")

    print(Assigned_by_tester_list)
    return render (request,"BugTracking/Assigned_by_tester_list.html",{"Assigned_by_tester_list":Assigned_by_tester_list})
# this is  a delete section
def delete_user(request, user_id):
    if request.method == "POST":
        user = get_object_or_404(usertable, user_id=user_id)
        user.delete()
    return redirect('User_list')

def delete_project(request, project_id):
    if request.method == "POST":
        project = get_object_or_404(projectTable,project_id=project_id)
        project.delete()
    return redirect('project_list')

def delete_module(request, module_id):
    if request.method == "POST":
       module = get_object_or_404(moduletable,module_id=module_id)
       module.delete()
    return redirect('Moduel_list')

def delete_task(request, task_id):
    if request.method == "POST":
       task = get_object_or_404(tasktable,task_id=task_id)
       task.delete()
    return redirect('Task_list')

def delete_bug(request, id):
    if request.method == "POST":
        bug = get_object_or_404(bugtrackingtable , id=id)
        bug.delete()
    return redirect('Bug_creat_list')

def delete_assigned_bugtester(request, id):
    if request.method == "POST":
        assigned_bug = get_object_or_404(assigned_bugtable, id=id)
        assigned_bug.delete()
    return redirect('Assigned_by_tester_list')

def delete_comment(request, comment_id):
    if request.method == "POST":
        comment = get_object_or_404(commentTable, comment_id=comment_id)
        comment.delete()
    return redirect('comment_list')

def delete_assigned(request,id):
    if request.method == "POST":
        assigned_table = get_object_or_404(assignedtable ,id=id)
        assigned_table.delete()
    return redirect('assigned_list')

def delete_assigned_bug(request,id):
    if request.method == "POST":
        assigned_bug = get_object_or_404(assigned_bugtable,id=id)
        assigned_bug.delete()
    return redirect('assigned_bug1_list')


# this is a logout 
def user_logout(request):
    logout(request)
    return redirect("login")


# this is a update form code section

def update_user(request,user_id):
    user=get_object_or_404(usertable, user_id=user_id)

    if request.method=="POST":
        form=user_update_form(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect("User_list")
    else:
        form =user_update_form(instance=user)

    return render(request,'BugTracking/Update_user.html',{'form':form})
        

def update_project(request,project_id):
    project=get_object_or_404(projectTable, project_id=project_id)

    if request.method=="POST":
        form=project_update_form(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
         form =project_update_form(instance=project)

    return render(request,'BugTracking/Update_project.html',{'form':form})


def update_module(request,module_id):
    module=get_object_or_404(moduletable, module_id=module_id)

    if request.method=="POST":
        form=module_update_form(request.POST,instance=module)
        if form.is_valid():
            form.save()
            return redirect("Moduel_list")
    else:
        form =module_update_form(instance=module)

    return render(request,'BugTracking/Update_module.html',{'form':form})


def update_task(request,task_id):
    task=get_object_or_404(tasktable, task_id=task_id)

    if request.method=="POST":
        form=task_update_form(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("Task_list")
    else:
         form =task_update_form(instance=task)

    return render(request,'BugTracking/Update_task.html',{'form':form})
        

def update_assigned(request,id):
    obj=get_object_or_404(assignedtable, id=id)

    if request.method=="POST":
        form=assigned_update_form(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("assigned_list")
    else:
        form =assigned_update_form(instance=obj)

    return render(request,'BugTracking/Update_assigned.html',{'form':form})


def update_created_bug(request,id):
    created=get_object_or_404(bugtrackingtable,id =id)

    if request.method=="POST":
        form=bug_update_form(request.POST,instance=created)
        if form.is_valid():
            form.save()
            return redirect("Bug_creat_list")
    else:
        form =bug_update_form(instance=created)

    return render(request,'BugTracking/Update_created_bug.html',{'form':form})


def update_assigned_bug(request,id):
    obj1=get_object_or_404(assigned_bugtable,id=id)

    if request.method=="POST":
        form=assigned_bug_update_form(request.POST,instance=obj1)
        if form.is_valid():
            form.save()
            return redirect("assigned_bug1_list")
    else:
        form =assigned_bug_update_form(instance=obj1)

    return render(request,'BugTracking/Update_assigned_bug.html',{'form':form})


def update_assigned_to_tester(request,id):
   obj2 =get_object_or_404(assigned_bugtable,id=id)

   if request.method=="POST":
        form=assigned_fix_bug_update_form(request.POST,instance=obj2)
        if form.is_valid():
            form.save()
            return redirect("Assigned_by_tester_list")
        
   else:
        form =assigned_fix_bug_update_form(instance=obj2)

   return render(request,'BugTracking/Update_assigned_to_tester.html',{'form':form})


def update_comment(request,comment_id):
    comment=get_object_or_404(commentTable,comment_id=comment_id)

    if request.method=="POST":
        form=comment_update_form(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            return redirect("comment_list")
    else:
        form =comment_update_form(instance=comment)

    return render(request,'BugTracking/Update_comment.html',{'form':form})