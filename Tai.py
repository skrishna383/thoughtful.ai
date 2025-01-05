def sort(width, height, length, mass):
    # Calculate the volume of the package
    volume = width * height * length
    
    # Determine if the package is bulky, heavy, or both
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    # Determine the stack the package belongs to
    return "REJECTED" if is_bulky and is_heavy else ("SPECIAL" if is_bulky or is_heavy else "STANDARD")

# Test cases
print(sort(200, 150, 100, 25))  # Should return "REJECTED"
print(sort(50, 50, 50, 10))     # Should return "STANDARD"
print(sort(200, 150, 100, 10))  # Should return "SPECIAL"
print(sort(50, 200, 50, 20))    # Should return "REJECTED"
