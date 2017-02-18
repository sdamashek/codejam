def get_unique(s):
    s_set = set(s)
    return len(list(s_set))

def attempt_base(s, base):
    available = list(range(base))
    result = 0
    mapping = dict()

    ind = len(s)-1 # base is zero indexed

    sl = list(s)
    # Assign first character
    first = sl.pop(0)
    available.remove(1)
    result += base**ind 
    mapping[first] = 1
    ind -= 1
    
    for char in sl:
        if char in mapping:
            result += mapping[char] * base**ind
        else:
            val = available.pop(0)
            mapping[char] = val
            result += val * base**ind
            
        ind -= 1

    return result

def process_sample(s):
    unique_letters = max([2, get_unique(s)])
    return attempt_base(s, unique_letters)

def main():
    n = int(input())
    for i in range(1, n+1):
        print('Case #{}: {}'.format(i, process_sample(input())))

if __name__ == '__main__':  main()
    
