# sentence screen fitting

# row_num = 0, col_num = 0; Row = 3; Col = 8; avaialble_space = len(Col)
# screen = [['-']*len(col_num)]*row_num
#
# for i in sentence_str:
#     word_len = len(i)
#     while row_num < Row:
#         if word_len < available_space:
#             for j in i:
#                 screen[row_num][col_num] = j
#
#             available_space -= word_len - 1
#             col_num+=word_len+1
#
#     row_num+=1
