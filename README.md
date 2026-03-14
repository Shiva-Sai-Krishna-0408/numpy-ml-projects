# NumPy & Pandas ML Projects

A collection of Data Science and Machine Learning projects built from scratch using NumPy and Pandas.

## Projects

### 1. Search Engine
A semantic search engine that finds the most relevant topics for any query using cosine similarity and confidence scoring.

**Concepts used:**
- Cosine similarity
- Vector embeddings
- Sum normalization
- Confidence distribution
```python
python search_engine.py
```

### 2. Student Score Analyzer
Normalizes student exam scores across 5 subjects and categorizes them into High, Mid, and Low performance groups.

**Concepts used:**
- Min-Max normalization
- Array operations
- Performance categorization
```python
python student_score_analyzer.py
```

### 3. Movie Recommender
Recommends the top 2 movies for each user based on their preference vectors using cosine similarity.

**Concepts used:**
- Cosine similarity
- Dot product
- Vector normalization
- Sorting by similarity score
```python
python movie_recommender.py
```

### 4. Regional Sales Analysis
Analyzes regional sales performance across quarters, tracking revenue achievement, target completion, and revenue efficiency per headcount.

**Concepts used:**
- Achievement rate calculation
- Pivot tables
- Dynamic tie handling
- Banker's rounding vs arithmetic rounding
- GroupBy aggregation with status filtering
```python
python regional_sales_analysis.py
```

### 5. Climate Data Analyzer
Analyzes climate data across Indian cities, normalizing temperatures, scoring air quality, and classifying climate risk levels.

**Concepts used:**
- Min-Max normalization
- Z-score calculation
- GroupBy aggregation
- Row-wise apply with axis=1
- Multi-condition risk classification
```python
python climate_data_analyzer.py
```

### 6. Employee Performance Tracker
Tracks employee sales performance across departments and months, identifying top performers and consistently exceeding departments.

**Concepts used:**
- Achievement rate calculation
- Multi-condition performance classification
- Cumulative sales with GroupBy
- Top performer identification per department
- Boolean filtering with .all()
```python
python employee_performance_tracker.py
```

### 7. Stock Market Analyzer
Analyzes stock price movements for AAPL and GOOGL, calculating daily returns, rolling averages, volatility and generating buy/sell signals.

**Concepts used:**
- Percentage change with pct_change()
- Rolling window averages with GroupBy
- Volatility via standard deviation
- Datetime conversion and formatting
- Buy/Sell/Hold signal classification
```python
python stock_risk_analyzer.py
```

## About
Built as part of my AI/ML learning journey. All projects implemented from scratch without high-level ML libraries to demonstrate core understanding.
