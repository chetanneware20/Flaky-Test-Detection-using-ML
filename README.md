# 🧪 Flaky Test Detection Using Machine Learning

## 📌 Overview
Flaky tests are automated test cases that pass and fail inconsistently without any change in the application code.  
They increase CI/CD noise, slow down pipelines, and reduce confidence in automation results.

This project uses **Machine Learning (Unsupervised Clustering)** and **Time-Series Analysis** to automatically identify flaky test cases using historical execution data and integrates the results into a CI/CD pipeline.

---

## 🎯 Project Goals
- Automatically identify flaky (unstable) test cases
- Reduce false failures in CI/CD pipelines
- Improve reliability and trust in automation testing
- Apply Data Science concepts to real-world QA problems

---

## 🏗️ System Architecture

Automation Test Execution  
↓  
Test Execution Logs (Pass/Fail, Duration, Date)  
↓  
Feature Engineering  
↓  
ML Clustering Model (DBSCAN)  
↓  
Flaky / Stable Test Classification  
↓  
Dashboard + CI/CD Integration  

---

## 🧠 Machine Learning Approach

### 1️⃣ Feature Engineering
Each test case is converted into numerical features such as:
- **Failure Rate** – Percentage of failed executions
- **Status Switching Count** – How often test status changes (Pass ↔ Fail)
- **Average Execution Time**
- **Execution Time Variance**

Flaky tests typically show:
- Medium failure rate (not always failing)
- High status switching
- High execution time variance

---

### 2️⃣ Clustering (Unsupervised Learning)
Since flaky test labels are usually unavailable, **unsupervised learning** is used.

- **DBSCAN** clustering algorithm
- Automatically detects outliers and unstable patterns
- No need to predefine the number of clusters

Flaky tests usually appear as **outliers or noise points**.

---

### 3️⃣ Time-Series Analysis
Flakiness is time-dependent, so historical trends are analyzed using:
- Rolling failure rate
- Trend detection across executions
- Sudden behavior changes after commits

This helps identify newly flaky tests early.

---

## 🛠️ Technology Stack

| Category | Tools |
|--------|------|
| Programming Language | Python |
| Data Processing | Pandas |
| Machine Learning | Scikit-learn |
| Visualization | Streamlit |
| CI/CD Integration | :contentReference[oaicite:0]{index=0} |

---

## 📁 Project Structure
