import os'''模型的基本配置 BASE_DIR 本地路径train_path 训练路径test_path 测试路径'''BASE_DIR = os.path.dirname(os.path.abspath(__file__))train_path = os.path.join(BASE_DIR, "data/train.csv")test_path = os.path.join(BASE_DIR, "data/test.csv")print(test_path)