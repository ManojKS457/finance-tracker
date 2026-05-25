# 💰 Smart Finance Management System

A professional AI-powered personal finance management system built using Streamlit.

This application helps users:
- Track income and expenses
- Set monthly budget limits
- Monitor EMI payments
- Track savings goals
- Receive expense alerts
- Analyze financial trends
- Login securely using authentication and Google OAuth
- Receive SMTP email notifications

---

# 🚀 Features

## 🔐 Authentication
- User Login
- User Signup
- Session Management
- Google OAuth Login
- Secure Password Handling

---

## 💵 Income Management
- Add Income
- Track Salary/Freelancing/Investments
- Monthly Income Analytics

---

## 💳 Expense Tracking
- Add Expenses
- Categorized Expense Management
- Expense History Tracking

Expense categories include:
- Food
- EMI
- Shopping
- Transport
- Bills
- Medical
- Entertainment

---

## 📊 Budget Planner

Users can:
- Set Monthly Income
- Set EMI Amount
- Set Savings Goal
- Automatically Calculate Expense Limit

Formula Used:

Expense Limit = Income - (EMI + Savings Goal)

---

## 🚨 Smart Alerts

The system provides:
- Expense Limit Warnings
- Budget Exceeded Alerts
- Savings Goal Alerts
- EMI Reminder Notifications

---

## 📈 Dashboard Analytics

Interactive charts include:
- Pie Charts
- Line Charts
- Bar Charts
- Savings Analysis
- Expense Trends

Built using:
- Plotly
- Pandas
- Streamlit

---

## 📧 SMTP Email Alerts

Email alerts are sent using Gmail SMTP when:
- Expenses exceed budget
- EMI due dates approach
- Savings goals are not met

---

## 🎨 Professional Frontend

Frontend includes:
- Modern Sidebar Navigation
- Responsive Dashboard
- KPI Cards
- Custom CSS Styling
- FinTech-inspired UI

---

# 🛠️ Technologies Used

## Frontend
- Streamlit
- HTML/CSS

## Backend
- Python

## Database
- SQLite

## Data Analysis
- Pandas
- NumPy

## Charts
- Plotly
- Matplotlib

## Authentication
- Google OAuth
- Session Management

## Notifications
- SMTP Email Service

---

# 📂 Project Structure

```text
FINANCE-TRACKER/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
│
├── assets/
├── authentication/
├── dashboard/
├── pages/
├── database/
├── services/
├── charts/
├── utils/
├── dataset/
├── frontend/
├── alerts/
├── exports/
├── logs/
└── email_templates/