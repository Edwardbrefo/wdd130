import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from water_pressure import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

print("=== Debugging pressure_gain_from_water_height ===")
print(f"Result for h=0.0: {pressure_gain_from_water_height(0.0)}, Expected: 0.0")
print(f"Result for h=30.2: {pressure_gain_from_water_height(30.2)}, Expected: 295.628")
print(f"Result for h=50.0: {pressure_gain_from_water_height(50.0)}, Expected: 489.450")

print("\n=== Debugging pressure_loss_from_pipe ===")
print(f"Test 1: diameter=0.048692, length=0.00, friction=0.018, velocity=1.75")
print(f"  Result: {pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75)}, Expected: 0.0")

print(f"\nTest 2: diameter=0.048692, length=200.00, friction=0.000, velocity=1.75")
print(f"  Result: {pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75)}, Expected: 0.0")

print(f"\nTest 3: diameter=0.048692, length=200.00, friction=0.018, velocity=0.00")
print(f"  Result: {pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00)}, Expected: 0.0")

print(f"\nTest 4: diameter=0.048692, length=200.00, friction=0.018, velocity=1.75")
print(f"  Result: {pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75)}, Expected: -113.008")

print(f"\nTest 5: diameter=0.048692, length=200.00, friction=0.018, velocity=1.65")
print(f"  Result: {pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65)}, Expected: -100.462")

print(f"\nTest 6: diameter=0.286870, length=1000.00, friction=0.013, velocity=1.65")
print(f"  Result: {pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65)}, Expected: -61.576")

print(f"\nTest 7: diameter=0.286870, length=1800.75, friction=0.013, velocity=1.65")
print(f"  Result: {pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65)}, Expected: -110.884")
