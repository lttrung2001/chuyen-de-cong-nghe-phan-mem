import numpy as np

def cosine_similarity(x1, x2):
    """
    Tính độ tương đồng cosine giữa hai vector x1 và x2.
    """
    dot_product = np.dot(x1, x2)
    norm_x1 = np.linalg.norm(x1)
    norm_x2 = np.linalg.norm(x2)
    return dot_product / (norm_x1 * norm_x2)

def classify(x, y, theta):
    """
    Phân loại x và y dựa trên ngưỡng theta.
    """
    similarity = cosine_similarity(x, y)
    if similarity >= theta:
        return "Phù hợp"
    else:
        return "Không phù hợp"

# Tạo hai vector đặc trưng nhị phân cho hai tài liệu
x = np.array([1, 1, 0, 1, 0, 0])
y = np.array([1, 0, 1, 0, 1, 0])

# Phân loại x và y dựa trên ngưỡng theta
theta = 0.5
result = classify(x, y, theta)
print(result)

# Tính xác suất của x và y phù hợp
prob = cosine_similarity(x, y)
print("Xác suất phù hợp:", prob)