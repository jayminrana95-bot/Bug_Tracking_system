from django.contrib import admin
from .models import assignedtable, usertable,projectTable,moduletable,tasktable,bugtrackingtable,task_time_tracking_table,commentTable,assignedtable,assigned_bugtable
# Register your models here.
admin.site.register(usertable),
admin.site.register(projectTable),
admin.site.register(moduletable),
admin.site.register(tasktable),
admin.site.register(bugtrackingtable),
admin.site.register(task_time_tracking_table),
admin.site.register(commentTable),
admin.site.register(assignedtable),
admin.site.register(assigned_bugtable),

