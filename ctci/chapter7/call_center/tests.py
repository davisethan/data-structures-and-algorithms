import unittest
from CallCenterChainOfResponsibility import Respondent, Manager, Director
from Employee import Employee

class TestCallCenterChainOfResponsibility(unittest.TestCase):
    def test_call_center_chain_of_responsibility(self):
        # (case name, call center with unbusy employee, unbusy employee id)
        cases = [
            ("respondent unbusy", Respondent([Employee(303, busy = False)]), 303),
            ("respondent unbusy", Manager([Employee(203, busy = False)]), 203),
            ("respondent unbusy", Director([Employee(103, busy = False)]), 103),
        ]
        for case in cases:
            with self.subTest(case[0]):
                call_center_chain_of_responsibility_helper = CallCenterChainOfResponsibilityHelper()
                call_center_chain_of_responsibility_helper._merge_employees(case[1])
                respondent = call_center_chain_of_responsibility_helper.get_respondent()

                actual_call_response = respondent.dispatch_call()

                self.assertEqual(case[2], actual_call_response)

class CallCenterChainOfResponsibilityHelper:
    def __init__(self):
        self._director = Director([Employee(101), Employee(102)])
        self._manager = Manager([Employee(201), Employee(202)], self._director)
        self._respondent = Respondent([Employee(301), Employee(302)], self._manager)

    def get_respondent(self):
        return self._respondent

    def _merge_employees(self, call_center):
        if isinstance(call_center, Director):
            self._director.join_call_center_employees(call_center)
        elif isinstance(call_center, Manager):
            self._manager.join_call_center_employees(call_center)
        elif isinstance(call_center, Respondent):
            self._respondent.join_call_center_employees(call_center)

if __name__ == "__main__":
    unittest.main()
