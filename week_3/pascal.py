def pascal(n):
    if n == 1:
        return [[1]]
    elif n >= 2:
        new_value = [1]
        result = pascal(n-1)
        last_value = result[-1]
        for i in range(len(last_value)-1):
            new_value.append(last_value[i] + last_value[i+1])
        new_value += [1]
        result.append(new_value)
    return result

print(pascal(8))