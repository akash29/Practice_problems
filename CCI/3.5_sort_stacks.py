def sort_stack(stack):
    temp_stack = []

    while stack:
        stack_val = stack.pop()
        len_temp = len(temp_stack)
        if len(temp_stack) < 1:
            temp_stack.append(stack_val)
        else:
            if stack_val < temp_stack[len_temp-1]:
                temp_stack.append(stack_val)
            else:
                while temp_stack and temp_stack[len(temp_stack)-1] <  stack_val:
                    temp_val = temp_stack.pop()
                    stack.append(temp_val)
                temp_stack.append(stack_val)

    print (temp_stack)



test_list = [3,2,1,5,7,6]
print (test_list)
sort_stack(test_list)