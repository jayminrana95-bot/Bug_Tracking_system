from django.db import models

# Create your models here.

class usertable ( models.Model):
    role_choice=(
       
        ('Project Manager','Project Manager'),
        ('Developer','Developer'),
        ('Tester','Tester'),)
    user_id=models.CharField(max_length=100,unique=True)
    Name = models.CharField(max_length=100)
    role = models.CharField(max_length=100,choices=role_choice)
    email = models.EmailField( )
    password =models.CharField(max_length=100)
    created_at =models.DateTimeField()

    class Meta:
        db_table ="usertable"

    def __str__(self):
        return self.Name
    



class projectTable (models.Model):
    choices = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
]
    project_id =models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    Description = models.TextField()
    created_by =models.ForeignKey(usertable,on_delete=models.CASCADE,null=True,blank=True)
    start_date =models.DateField(null=True)
    end_date =models.DateField(null=True)
    status = models.CharField(max_length=100,choices=choices)


    class Meta:
        db_table ="projectTable"


    def __str__(self):
        return self.project_name
    



class moduletable (models.Model):
    module_id = models.CharField(max_length=100)
    project_id =models.ForeignKey(projectTable,on_delete=models.CASCADE)
    module_name = models.CharField(max_length=100)
    Description =models.TextField()
    created_at =models.DateTimeField()

    class Meta:
        db_table = "moduletable"

    def __str__(self):
        return self.module_name
    



class tasktable (models.Model):
    choices = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
]
    task_id = models.CharField(max_length=100)
    module_id =models.ForeignKey(moduletable,on_delete=models.CASCADE)
    
    task_description =models.TextField()
    start_date = models.DateTimeField()
    end_date =models.DateTimeField()
    status =models.CharField(max_length=100,choices=choices)

    class Meta:
        db_table ="tasktable"


    def __str__(self):
        return self.task_id
    



class bugtrackingtable (models.Model):
    level_choice=(('low', 'Low'), ('medium', 'Medium'), ('high', 'High'))
    status_choice=(('open', 'Open'), ('in_progress', 'In Progress'), ('closed', 'Closed'))
    task_id=models.ForeignKey(tasktable,on_delete=models.CASCADE)
    reported_by =models.ForeignKey(usertable,on_delete=models.CASCADE,related_name='bug_reported_by')
    assigned_to=models.ForeignKey(usertable,on_delete=models.CASCADE,related_name='bug_assgined_to')
    Description =models.TextField()
    severity = models.CharField(max_length=100, choices=level_choice)
    status = models.CharField(max_length=100, choices=status_choice)
    reported_date =models.DateTimeField()
    fix_date=models.DateTimeField()


    class Meta:
        db_table ="bugtrackingtable"


    def __str__(self):
        return self.Description
    




class task_time_tracking_table (models.Model):
    recode_id =models.IntegerField()
    Developer_id =models.ForeignKey(usertable,on_delete=models.CASCADE,related_name='Devaloper_id')
    task_id =models.ForeignKey(usertable,on_delete=models.CASCADE,related_name='task_id')
    total_time =models.FloatField()
    updated_at =models.DateTimeField()


    class Meta:
        db_table="task_time_tracking_table"


    def __str__(self):
        return self.name
    




class commentTable (models.Model):
    comment_id = models.CharField(max_length=100,null=True,blank=True,unique=True)
    bug_id = models.ForeignKey(bugtrackingtable,on_delete=models.CASCADE,null=True,blank=True)
    user_id =models.ForeignKey(usertable,on_delete=models.CASCADE,null=True,blank=True)
    commentd = models.TextField(null=True,blank=True)
    commentd_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)


    class Meta:
        db_table="commentTable"

    def __str__(self):
        return str(self.comment_id)
    




class assignedtable (models.Model):
   
    task_id= models.ForeignKey(tasktable,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(usertable, on_delete=models.CASCADE,
        related_name='assigned_to' )
    assigned_by =models.ForeignKey(usertable, on_delete=models.CASCADE,
        related_name='assigned_by')
    Description=models.TextField()
    assigned_date=models.DateField()


    class Meta:
        db_table="assignedtable"


    def __str__(self):
        return self.Description
    





class assigned_bugtable(models.Model):
    def_choice=(('low','low'),('medium','medium'),('high','high'))
    sta_choice=(('pending', 'pending'), ('in_progress', 'In Progress'), ('closed', 'Closed'),('testing', 'testing'),('completed', 'completed'))
    task=models.ForeignKey(tasktable,on_delete=models.CASCADE,null=True,blank=True,related_name='task')
    bug=models.ForeignKey(bugtrackingtable,on_delete=models.CASCADE,null=True,blank=True,related_name='bug')
    Description = models.TextField()
    assigned_to =models.ForeignKey(usertable,on_delete=models.CASCADE,related_name='bug_assigned_to')
    assigned_by=models.ForeignKey(usertable,on_delete=models.CASCADE,null=True,blank=True,related_name='assigned_by_form_tester')
    reported_by =models.ForeignKey(usertable,on_delete=models.CASCADE,null=True,blank=True,related_name='bug_related_by')
    assigned_date =models.DateField(auto_now_add=True)
    severity = models.CharField(max_length=100, choices=def_choice)
    status = models.CharField(max_length=100, choices=sta_choice)
    fix_date =models.DateField()
    

    class Meta:
        db_table="assigned_bugtable"


    def __str__(self):
        return self.Description
    


