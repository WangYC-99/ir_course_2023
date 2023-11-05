import json

# inverted_index = {
#     'word1': ['doc1', 'doc2'],
#     'word2': ['doc1', 'doc3'],
#     'word3': ['doc1', 'doc2'],
#     'word4': ['doc2', 'doc3'],
#     'word5': ['doc3'],
# }

with open('cleared_dataset/inverted_index.json', 'r') as f:
    inverted_index = json.load(f)

def infix_to_rpn(query):
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
    output_queue = []
    operator_stack = []

    for item in query:
        if item in inverted_index or item not in precedence:
            output_queue.append(item)
        elif item in precedence:
            while (operator_stack and operator_stack[-1] in precedence and
                   precedence[item] <= precedence[operator_stack[-1]]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(item)
        elif item == '(':
            operator_stack.append(item)
        elif item == ')':
            while operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue

def boolean_query(query):
    stack = []
    for item in query:
        if item == 'AND':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = list(set(operand1) & set(operand2))
            stack.append(result)
        elif item == 'OR':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = list(set(operand1) | set(operand2))
            stack.append(result)
        elif item == 'NOT':
            operand = stack.pop()
            all_docs = set(doc for docs in inverted_index.values() for doc in docs)
            result = list(all_docs - set(operand))
            stack.append(result)
        else:
            stack.append(inverted_index.get(item, []))
    return stack.pop()


query = ['中国', 'AND', '赢得', 'NOT', '成立']
rpn_query = infix_to_rpn(query)
print(boolean_query(rpn_query))