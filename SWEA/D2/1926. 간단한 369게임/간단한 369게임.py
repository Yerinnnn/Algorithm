N = int(input())
result = []
    
for i in range(1, N + 1):
    num_str = str(i)
    clap_count = num_str.count('3') + num_str.count('6') + num_str.count('9')
        
    if clap_count > 0:
        result.append('-' * clap_count)
    else:
        result.append(num_str)

print(" ".join(result))