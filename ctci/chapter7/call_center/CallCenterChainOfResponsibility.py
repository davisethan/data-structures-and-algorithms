from abc import ABC
from Employee import Employee

class CallCenterChainOfResponsibility(ABC):
    def __init__(self, employees = [], parent = None):
        self._employees = employees
        self._parent = parent

    def get_employees(self):
        return self._employees

    def join_call_center_employees(self, call_center):
        self._employees += call_center.get_employees()

    def dispatch_call(self):
        for employee in self._employees:
            if employee.is_busy():
                continue
            return employee.get_id()
        if self._parent:
            return self._parent.dispatch_call()

class Director(CallCenterChainOfResponsibility):
    pass

class Manager(CallCenterChainOfResponsibility):
    pass

class Respondent(CallCenterChainOfResponsibility):
    pass
