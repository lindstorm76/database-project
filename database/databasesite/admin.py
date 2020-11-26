from django.contrib import admin

from .models import Employee, Department, Warehouse, Item, Lott, Customer, Order

class EmployeeView(admin.ModelAdmin):
  list_display = ("employee_number", "first_name", "last_name", "dnumber")

class DepartmentView(admin.ModelAdmin):
  list_display = ("department_number", "department_name")

class WarehouseView(admin.ModelAdmin):
  list_display = ("warehouse_number", "name", "location")

class ItemView(admin.ModelAdmin):
  list_display = ("item_number", "name", "lott")

class LottView(admin.ModelAdmin):
  list_display = ("lott_number", "date", "warehouse_number")

class CustomerView(admin.ModelAdmin):
  list_display = ("customer_id", "name")

class OrderView(admin.ModelAdmin):
  list_display = ("order_id", "item", "employee", "amount")

admin.site.register(Employee, EmployeeView)
admin.site.register(Department, DepartmentView)
admin.site.register(Warehouse, WarehouseView)
admin.site.register(Item, ItemView)
admin.site.register(Lott, LottView)
admin.site.register(Customer, CustomerView)
admin.site.register(Order, OrderView)