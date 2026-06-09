def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(A, B):
    counts = {}
    for x in B:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
            
    to_remove = set()

    for value in counts:
        if is_prime(counts[value]):
            to_remove.add(value)

    result = []
    for x in A:
        if x not in to_remove:
            result.append(x)

    return result

if __name__ == "__main__":
    A = [2, 3, 9, 2, 5, 1, 3, 7, 10]
    B = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]

    print(solution(A, B))  # [2, 9, 2, 5, 7, 10]