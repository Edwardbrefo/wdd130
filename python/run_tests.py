import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

def approx_equal(actual, expected, tolerance=0.001):
    return abs(actual - expected) <= tolerance

print("Running tests...\n")

# Test 1: water_column_height
print("=== test_water_column_height ===")
tests_passed = 0
try:
    assert approx_equal(water_column_height(0.0, 0.0), 0.0)
    assert approx_equal(water_column_height(0.0, 10.0), 7.5)
    assert approx_equal(water_column_height(25.0, 0.0), 25.0)
    assert approx_equal(water_column_height(48.3, 12.8), 57.9)
    print("PASSED: test_water_column_height\n")
    tests_passed += 1
except AssertionError as e:
    print(f"FAILED: test_water_column_height - {e}\n")
except Exception as e:
    print(f"ERROR: test_water_column_height - {e}\n")

# Test 2: pressure_gain_from_water_height
print("=== test_pressure_gain_from_water_height ===")
try:
    result1 = pressure_gain_from_water_height(0.0)
    result2 = pressure_gain_from_water_height(30.2)
    result3 = pressure_gain_from_water_height(50.0)
    print(f"Result 1: {result1}, Expected: 0.000")
    print(f"Result 2: {result2}, Expected: 295.729")
    print(f"Result 3: {result3}, Expected: 489.617")
    assert approx_equal(result1, 0.000, 0.001)
    assert approx_equal(result2, 295.729, 0.001)
    assert approx_equal(result3, 489.617, 0.001)
    print("PASSED: test_pressure_gain_from_water_height\n")
    tests_passed += 1
except AssertionError as e:
    print(f"FAILED: test_pressure_gain_from_water_height - {e}\n")
except Exception as e:
    print(f"ERROR: test_pressure_gain_from_water_height - {e}\n")

# Test 3: pressure_loss_from_pipe
print("=== test_pressure_loss_from_pipe ===")
try:
    assert approx_equal(pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75), 0.000, 0.001)
    assert approx_equal(pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75), 0.000, 0.001)
    assert approx_equal(pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00), 0.000, 0.001)
    assert approx_equal(pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75), -113.008, 0.001)
    assert approx_equal(pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65), -100.462, 0.001)
    assert approx_equal(pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65), -61.576, 0.001)
    assert approx_equal(pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65), -110.884, 0.001)
    print("PASSED: test_pressure_loss_from_pipe\n")
    tests_passed += 1
except AssertionError as e:
    print(f"FAILED: test_pressure_loss_from_pipe - {e}\n")
except Exception as e:
    print(f"ERROR: test_pressure_loss_from_pipe - {e}\n")

print(f"Results: {tests_passed}/3 tests passed")
