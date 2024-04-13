def binary_32reverse(num):
    if num == 0:
        return 0
    
    count = 0 
    result = 0
    while num != 0:
        # Extract the least significant bit (LSB) of num
        lsb = num & 1
        
        # Add the LSB to the result (left shift result by 1 and bitwise OR with lsb)
        result = (result << 1) | lsb
        count += 1
        
        # Right shift num to process the next bit
        num = num >> 1
    
    result = result << (32-count)

    return result

# Test the function
print(binary_32reverse(1))
print(binary_32reverse(5))
