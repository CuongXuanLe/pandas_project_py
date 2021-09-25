import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Choose your input data: (2pts)
#    Ví dụ: trong challenge 1, có input data là 3 files csv
#              trong challenge 2, có input data là một file hình ảnh bài làm trắc nghiệm

# Create 1 problem statement and 10 questions for the input data (ranking from easy to difficult): (3pts)
#    Tạo ra 10  hỏi hợp lý giải quyết vấn đề và định nghĩa vấn đề liên quan tới dữ liệu,
#    tham khảo cách đặt câu hỏi trong challenge 1 và challenge 2
# 3. Solve your 10 questions (3pts)
# 4. Coding style (1pts)
# 5. Github (1pts)


data = pd.read_csv('chess_games.csv', low_memory=False)
data.head()

#chunksize = 50000000
#for chunk in pd.read_csv("chess_games.csv", chunksize=chunksize):
#    process(chunk)