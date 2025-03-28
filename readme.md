[English](#english-version) | [中文](#chinese-version)

---

## English Version

### Project Overview

This project implements a movie recommendation system based on user collaborative filtering . By analyzing users' historical rating data, it calculates the similarity between users and recommends unrated high-rated movies to target users. The system also includes data visualization features , generating charts to analyze user behavior, movie popularity, and recommendation quality.

#### Dataset

- Download dataset([source](https://grouplens.org/datasets/movielens/?spm=a2ty_o01.29997173.0.0.2e16c921YrY6qs)) and save in the `data/` directory and the original dataset includes the following files:
  - ratings.csv: User movie ratings.
  - movies.csv: Movie information (e.g., title and genre).
  - tags.csv: User-defined tags for movies (optional).
  - links.csv: External links for movies (optional).

#### Project Structure

```
demo
├── data
│ ├── README.txt
│ ├── links.csv
│ ├── movies.csv
│ ├── ratings.csv
│ └── tags.csv
├── main.py
├── requirements.txt
└── venv
```

#### Usage Instructions

1. Install Dependencies  
   Ensure Python 3.9 or higher is installed, then run the following command to install dependencies:

   ```python
   pip install -r requirements.txt
   ```

2. Run the Program  
   Execute the following command to run the recommendation system:

   ```python
   python main.py
   ```

3. Output Results
   - The program will recommend unrated movies for the target user (default user ID=1) and sort them by predicted ratings in descending order.
   - All generated charts will be saved in the `output/` folder as PNG files.

#### Core Functionality

- Data Preprocessing:
  - Merge rating and movie data.
  - Filter active users and popular movies.
  - Process duplicate rating data.
- User Similarity Calculation:  
  Use cosine similarity to calculate user similarity.
- Recommendation Generation:  
  Recommend unrated high-rated movies based on similar users.
- Data Visualization :
  - User Rating Distribution : Analyze the rating habits of the target user.
  - Similar User Ratings : Compare the target user's ratings with those of similar users.
  - Recommendation Scores : Visualize the scores of recommended movies.
  - User Activity Distribution : Analyze the number of ratings per user.
  - Movie Popularity Distribution : Analyze the number of ratings per movie.

#### Notes

- Ensure the CSV files in the data/ directory are complete and the paths are correct.
- If the dataset is large, adjust filtering conditions (e.g., thresholds for active users and popular movies).
- Generated charts are saved in the `output/` folder for further analysis.

---

## Chinese Version

#### 项目概述

本项目实现了一个基于用户协同过滤 的电影推荐系统。通过分析用户的历史评分数据，计算用户之间的相似性，并为目标用户推荐未评分的高分电影。此外，系统还包含数据可视化功能 ，生成图表以分析用户行为、电影流行度以及推荐质量。

#### 数据集

- 下载数据集([来源](https://grouplens.org/datasets/movielens/?spm=a2ty_o01.29997173.0.0.2e16c921YrY6qs))并保存于 `data/` 目录下，原始数据集包括以下文件：
  - ratings.csv: 用户对电影的评分记录。
  - movies.csv: 电影的基本信息（如电影名称和类型）。
  - tags.csv: 用户对电影的标签数据（可选）。
  - links.csv: 电影的外部链接数据（可选）。

#### 项目结构

```
demo
├── data
│ ├── README.txt
│ ├── links.csv
│ ├── movies.csv
│ ├── ratings.csv
│ └── tags.csv
├── main.py
├── requirements.txt
└── venv
```

#### 使用说明

1. 安装依赖  
   确保已安装 Python 3.9 或更高版本，并运行以下命令安装依赖：

   ```python
   pip install -r requirements.txt
   ```

2. 运行程序  
   执行以下命令运行推荐系统：

   ```python
   python main.py
   ```

3. 输出结果
   - 程序会为目标用户（默认为用户 ID=1）推荐未评分的电影，并按预测评分从高到低排序。
   - 所有生成的图表将保存在 `output/` 文件夹中，格式为 PNG 文件。

#### 核心功能

- 数据预处理:
  - 合并评分和电影数据。
  - 筛选活跃用户和热门电影。
  - 处理重复评分数据。
- 用户相似度计算:  
  使用余弦相似度算法计算用户之间的相似性。
- 推荐生成:  
  根据目标用户的相似用户，推荐未评分的高分电影。
- 数据可视化 :
  - 用户评分分布 ：分析目标用户的评分习惯。
  - 相似用户评分分布 ：对比目标用户与相似用户的评分偏好。
  - 推荐电影评分分布 ：展示推荐电影及其评分。
  - 用户活动分布 ：分析每个用户的评分数量。
  - 电影流行度分布 ：分析每部电影的评分数量。

#### 注意事项

- 请确保 data/ 目录下的 CSV 文件完整且路径正确。
- 如果数据规模较大，建议适当调整筛选条件（如活跃用户和热门电影的阈值）。
- 生成的图表保存在 `output/` 文件夹中，便于进一步分析。
