#!/usr/bin/env python3

#!/usr/bin/env python3

from myhdl import bin
from bits import vm_test
import os.path

import pytest
import yaml
import math

try:
    from telemetry import telemetryMark

    pytestmark = telemetryMark()
except ImportError as err:
    print("Telemetry não importado")


def source(name):
    dir = os.path.dirname(__file__)
    src_dir = os.path.join(dir, ".")
    return os.path.join(src_dir, name)


SP = 0
STACK = 256
TEMP = {0: 5, 1: 6, 2: 7, 3: 8, 4: 9, 5: 10, 6: 11, 7: 12}


def init_ram():
    ram = {0: STACK}
    return ram



@pytest.mark.telemetry_files(source("mult/mult.vm"))
def test_mult_0():
    ram = init_ram()
    a = 0
    b = 2
    ram[TEMP[0]] = a
    ram[TEMP[1]] = b
    tst = {SP: STACK, TEMP[2]: a*b}
    assert vm_test("mult", ram, tst, 50000)


@pytest.mark.telemetry_files(source("1-mult/mult.vm"))
def test_mult_1():
    ram = init_ram()
    a = 2
    b = 0
    ram[TEMP[0]] = a
    ram[TEMP[1]] = b
    tst = {SP: STACK, TEMP[2]: a*b}
    assert vm_test("1-mult", ram, tst, 50000)


@pytest.mark.telemetry_files(source("1-mult/mult.vm"))
def test_mult_2():
    ram = init_ram()
    a = 4
    b = 5
    ram[TEMP[0]] = a
    ram[TEMP[1]] = b
    tst = {SP: STACK, TEMP[2]: a*b}
    assert vm_test("1-mult", ram, tst, 50000)


@pytest.mark.telemetry_files(source("2-div/div.vm"))
def test_div_0():
    ram = init_ram()

    val = 0 // 5
    tst = {SP: STACK, TEMP[1]: val}
    assert vm_test("2-div", ram, tst, 50000)


@pytest.mark.telemetry_files(source("2-div/div.vm"))
def test_div_15_5():
    ram = init_ram()

    val = 15 // 5
    tst = {SP: STACK, TEMP[1]: val}
    assert vm_test("2-div", ram, tst, 50000)


@pytest.mark.telemetry_files(source("3-pow/pow.vm"))
def test_pow_0():
    ram = init_ram()
    x = 2
    y = 0
    ram[TEMP[0]] = x
    ram[TEMP[1]] = y
    tst = {SP: STACK, TEMP[2]: x**y}
    assert vm_test("3-pow", ram, tst, 500000)


@pytest.mark.telemetry_files(source("3-pow/pow.vm"))
def test_pow_1():
    ram = init_ram()
    x = 5
    y = 1
    ram[TEMP[0]] = x
    ram[TEMP[1]] = y
    tst = {SP: STACK, TEMP[2]: x**y}
    assert vm_test("3-pow", ram, tst, 500000)

@pytest.mark.telemetry_files(source("3-pow/pow.vm"))
def test_pow_tres():
    ram = init_ram()
    x = 3
    y = 3
    ram[TEMP[0]] = x
    ram[TEMP[1]] = y
    tst = {SP: STACK, TEMP[2]: x**y}
    assert vm_test("3-pow", ram, tst, 100000)



@pytest.mark.telemetry_files(source("4-isqrt/isqrt.vm"))
def test_isqrt_quatro():
    ram = init_ram()
    ram[TEMP[0]] = 4
    ram[TEMP[1]] = 0
    tst = {TEMP[1]: math.sqrt(ram[TEMP[0]])}
    assert vm_test(os.path.join("4-isqrt"), ram, tst, 50000)


@pytest.mark.telemetry_files(source("4-isqrt/isqrt.vm"))
def test_isqrt_nove():
    ram = init_ram()
    ram[TEMP[0]] = 9
    ram[TEMP[1]] = 0
    tst = {TEMP[1]: math.sqrt(ram[TEMP[0]])}
    assert vm_test(os.path.join("4-isqrt"), ram, tst, 50000)
