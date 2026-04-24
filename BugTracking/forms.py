from django import forms 
from .models import bugtrackingtable, projectTable,moduletable,tasktable,usertable,assignedtable,assigned_bugtable,commentTable


class project_created (forms.ModelForm):
    
    class Meta:
        model = projectTable
        fields = [
            'project_id', 'project_name','created_by','Description','start_date','end_date','status',
        ]
       
        widgets = {
            'project_id': forms.TextInput(attrs={'class': 'input'}),
            'project_name': forms.TextInput(attrs={'class': 'input'}),
            'created_by': forms.Select(attrs={'class': 'input'}),
            'Description': forms.Textarea(attrs={'class': 'input', 'rows': 3}),
            'start_date': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
            'status': forms.Select(choices=  [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
]),
        }

    def clean(self):
     cleaned_data = super().clean()
     start = cleaned_data.get('start_date')
     end = cleaned_data.get('end_date')

     if start and end:
        if end < start:
            self.add_error('end_date', 'End date must be after start date')

     return cleaned_data
     

class module_created (forms.ModelForm):
    
    class Meta:
        model = moduletable
        fields = [
            'module_id', 'project_id', 'module_name', 'Description','created_at'
        ]
        
        widgets = {
            'module_id': forms.TextInput(attrs={'class': 'input'}),
            'project_id': forms.Select(attrs={'class': 'input'}),
            'module_name': forms.TextInput(attrs={'class': 'input'}),
            'Description': forms.Textarea(attrs={'class': 'input', 'rows': 3}),
            'created_at': forms.DateTimeInput(attrs={'class': 'input', 'type': 'datetime-local'}),
        }

class task_created (forms.ModelForm):
    
    class Meta:
        model = tasktable
        fields = [
            'task_id', 'module_id','task_description', 'start_date', 'end_date', 'status'
        ]
        
        widgets = {
            'task_id': forms.TextInput(attrs={'class': 'input'}),
            'module_id': forms.Select(attrs={'class': 'input'}),
            'task_description': forms.Textarea(attrs={'class': 'input', 'rows': 3}),
            'start_date': forms.DateTimeInput(attrs={'class': 'input', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'input', 'type': 'datetime-local'}),
            'status': forms.Select(choices = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
]),
        }

    
    def clean(self):
     cleaned_data = super().clean()
     start = cleaned_data.get('start_date')
     end = cleaned_data.get('end_date')

     if start and end:
        if end < start:
            self.add_error('end_date', 'End date must be after start date')

     return cleaned_data
     


class user_role (forms.ModelForm):
    class Meta:
        model = usertable
        fields = [
            'user_id','Name','role','email','password','created_at'
        ]

        widgets = {
           # 'user_id': forms.TextInput(attrs={'class': 'input'}),
            #'Name': forms.TextInput(attrs={'class': 'input'}),
          #  'role': forms.Select(attrs={'class': 'input'}),
           # 'email': forms.EmailInput(attrs={'class': 'input'}),
            'password': forms.PasswordInput(attrs={'class': 'input','placeholder':'enter password'}),
            'created_at': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
        }


class assigned(forms.ModelForm):
    class Meta:
        model=assignedtable
        fields= ['task_id','assigned_to','assigned_by','Description','assigned_date']


        widgets = {
            'task_id': forms.Select(attrs={'class': 'input'}),
            'assigned_to': forms.Select(attrs={'class': 'input'}),
            'assigned_by': forms.Select(attrs={'class': 'input'}),
            'Description': forms.Textarea(attrs={'class': 'input', 'rows': 3}),
            'assigned_date': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
        }


class Bug_Tracking(forms.ModelForm):
    class Meta:
        model=bugtrackingtable
        fields= ['task_id','reported_by','assigned_to','Description','severity','status','reported_date','fix_date']
        
        widgets = {
            'task_id': forms.Select(attrs={'class': 'input'}),
            'reported_by': forms.Select(attrs={'class': 'input'}),
            'assigned_to': forms.Select(attrs={'class': 'input'}),
            'Description': forms.Textarea(attrs={'class': 'input', 'rows': 3}),
            'severity': forms.Select(attrs={'class': 'input'}),
            'status': forms.Select(attrs={'class': 'input'}),
            'reported_date': forms.DateTimeInput(attrs={'class': 'input', 'type': 'datetime-local'}),
            'fix_date': forms.DateTimeInput(attrs={'class': 'input', 'type': 'datetime-local'}),
        }

    def clean(self):
     cleaned_data = super().clean()
     reported = cleaned_data.get('reported_date')
     fix = cleaned_data.get('fix_date')

     if reported and fix:
        if fix < reported:
            self.add_error('fix_date', 'Fix date must be after reported date')

     return cleaned_data


class assigned_bug(forms.ModelForm):
    class Meta:
        model=assigned_bugtable
        fields =[
           'assigned_to','reported_by','severity','status','fix_date','Description'
             
 ]

        widgets = {
            'assigned_to': forms.Select(attrs={'class': 'input'}),
            'reported_by': forms.Select(attrs={'class': 'input'}),
            'severity': forms.Select(attrs={'class': 'input'}),
            'status': forms.Select(attrs={'class': 'input'}),
            'fix_date': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
            'Description': forms.Textarea(attrs={'class': 'input', 'rows': 3}),
        }


class assignedtester(forms.ModelForm):
    class Meta:
        model =assigned_bugtable
        fields=[
            'assigned_to','assigned_by','Description','task','bug','status','fix_date'
        ]
        
        widgets = {
            'assigned_to': forms.Select(attrs={'class': 'input'}),
            'assigned_by': forms.Select(attrs={'class': 'input'}),
            'Description': forms.Textarea(attrs={'class': 'input', 'rows': 3}),
            'task': forms.Select(attrs={'class': 'input'}),
            'bug': forms.Select(attrs={'class': 'input'}),
            'status': forms.Select(attrs={'class': 'input'}),
            'fix_date': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
        }

    def clean(self):

     cleaned_data=super().clean()
     task=cleaned_data.get('task')
     bug=cleaned_data.get('bug')
     if not task and not bug:
        raise forms.ValidationError("cna you please select the either task or bug ")
     if task and bug:
        raise forms.ValidationError("enter only one field not both field")
     
     return cleaned_data
     
     

class  comment_Table(forms.ModelForm):
    class Meta:
        model= commentTable
        fields=[
            'comment_id','bug_id','user_id','commentd'
        ]


        widgets = {
            'comment_id': forms.TextInput(attrs={'class': 'input'}),
            'bug_id': forms.Select(attrs={'class': 'input'}),
            'user_id': forms.Select(attrs={'class': 'input'}),
            'commentd': forms.Textarea(attrs={
                'class': 'input',
                'rows': 4,
                'placeholder': 'Write your comment...'
            }),
        }



class user_update_form(forms.ModelForm):
    class Meta:
        model = usertable
        fields = ['Name', 'role', 'email', 'password']



class project_update_form(forms.ModelForm):
    class Meta:
        model = projectTable
        fields = ['project_name', 'Description', 'start_date', 'end_date','status']



class module_update_form(forms.ModelForm):
    class Meta:
        model = moduletable
        fields = ['project_id','module_name', 'Description','created_at']


class task_update_form(forms.ModelForm):
    class Meta:
        model = tasktable
        fields = ['module_id', 'task_description','start_date','end_date','status']


class assigned_update_form(forms.ModelForm):
    class Meta:
        model = assignedtable
        fields = ['task_id','assigned_to','assigned_by','Description','assigned_date']


class bug_update_form(forms.ModelForm):
    class Meta:
        model = bugtrackingtable
        fields = ['task_id','reported_by','severity','status','fix_date','Description','reported_date']


class assigned_bug_update_form(forms.ModelForm):
    class Meta:
        model = assigned_bugtable
        fields = ['assigned_to','reported_by','severity','status','fix_date','Description']


class assigned_bug_update_form(forms.ModelForm):
    class Meta:
        model = assigned_bugtable
        fields = ['assigned_to','reported_by','severity','status','fix_date','Description']


class assigned_fix_bug_update_form(forms.ModelForm):
    class Meta:
        model = assigned_bugtable
        fields = ['assigned_to','assigned_by','task','bug','status','fix_date','Description']


class comment_update_form(forms.ModelForm):
    class Meta:
        model = commentTable
        fields = ['bug_id','user_id','commentd']