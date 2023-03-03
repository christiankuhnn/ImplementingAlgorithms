from collections import defaultdict

def read_logs(filename):
    logs = defaultdict(lambda: {'scores': [], 'pages': []})
    with open(filename, 'r') as f:
        num_logs = int(f.readline().strip())
        for i in range(num_logs):
            student_id, action_code, third_element, timestamp = f.readline().strip().split()
            third_element = int(third_element)
            timestamp = int(timestamp)
            if action_code == 'S':
                logs[student_id]['scores'].append(third_element)
            elif action_code == 'P':
                logs[student_id]['pages'].append(third_element)
    return logs

def calculate_results(logs):
    results = []
    for student_id, data in logs.items():
        if len(data['scores']) == 0 or len(data['pages']) == 0:
            continue
        avg_score = sum(data['scores']) // len(data['scores'])
        results.append((student_id, min(data['pages']), max(data['pages']), avg_score))
    results.sort(key=lambda x: (x[1], x[2], x[3]))
    return results

def print_results(results):
    for student_id, min_page, max_page, avg_score in results:
        print(f"{student_id} {min_page} {max_page} {avg_score}")

if __name__ == '__main__': 
    filename = input()
    logs = read_logs(filename)
    results = calculate_results(logs)
    print_results(results)
