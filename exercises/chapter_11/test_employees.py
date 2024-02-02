import pytest
from exercise_11_3_employees import Employee

@pytest.fixture
def employee_james():
    '''Returns an employee names James.'''
    employee_james = Employee('james', 'buchanan', 30_000)
    return employee_james
                          
def test_give_default_raise(employee_james):
    '''Test that default raise works correctly.'''
    employee_james.give_raise()
    assert employee_james.salary == 35_000
    
def test_give_custom_raise(employee_james):
    '''Test that default raise works correctly.'''
    employee_james.give_raise(10_000)
    assert employee_james.salary == 40_000