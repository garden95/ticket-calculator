
import pytest
from ticket import calculate_ticket, vip_discount

def test_adult_no_dicount():
    assert calculate_ticket(25, False, False) == 15000

def test_child_no_dicount():
    assert calculate_ticket(15, False, False) == 12000

def test_adult_morning_discount():
    assert calculate_ticket(30, True, False) == 8000

def test_adult_3d_movie_no_discount():
    assert calculate_ticket(25, False, True) == 20000

def test_adult_3d_movie_morning():
    assert calculate_ticket(25, True, True) == 13000

def test_child_3d_movie_no_discount():
    assert calculate_ticket(15, False, True) == 17000

#===========

def test_adult_2D_vip():
    price = calculate_ticket(25, False, False)
    final_price = vip_discount(price, True)
    assert final_price == 13500

def test_adult_morning_3D_vip():
    price = calculate_ticket(30, True, True)
    final_price = vip_discount(price, True)
    assert final_price == 11700