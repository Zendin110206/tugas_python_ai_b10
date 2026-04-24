def square_root_bisection(square_target, tolerance=0.01, max_iterations=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target
    
    low = 0
    high = max(1, square_target) # edge cases: square root of 0.25 is 0.5 
    iterations = 0

    while low <= high and iterations < max_iterations:
        
        mid = (low + high) / 2
        mid_squared = mid * mid
        difference = abs(high - low)

        if difference <= tolerance:
            print(f"The square root of {square_target} is approximately {mid}")
            return mid
        
        elif mid_squared > square_target:  
            high = mid
        
        else:
            low = mid

        iterations += 1
    
    print(f"Failed to converge within {max_iterations} iterations")
    return None