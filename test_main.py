import pytest
from main import Calc

class TestCalc:
  def setup_method(self);
    self.inst= Calc()
  def test_equal_1(self);
    assert self.inst.equal(28, 96) == 124
  def setup_equal_2(self);
    assert self.inst.equal(10, 100) == 110
  def setup_equal_3(self);
    assert self.inst.equal_2(10, 100) == 1000
  def setup_equal_4(self);
    assert self.inst.equal_2(10, 2) == 20
