
def find_runner_up_score():

    n = int (input().strip())

    scores = list(map(int,input().strip().split()))

    max_score = max(scores)

    while max_score in scores:
        scores.remove(max_score)

    runner_up_score = max(scores)

    return runner_up_score

if __name__ == "__main__":
    print(find_runner_up_score())