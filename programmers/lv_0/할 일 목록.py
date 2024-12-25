def solution(todo_list, finished):
    return [todo for idx, todo in enumerate(todo_list) if not finished[idx]]
