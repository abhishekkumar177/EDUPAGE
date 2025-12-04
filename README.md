# Student Risk Analyzer 🎓

> A comprehensive, spreadsheet-first early-warning system that empowers students and mentors to proactively manage academic and financial risks through intelligent automation and transparent analytics.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Dash](https://img.shields.io/badge/Dash-Latest-brightgreen.svg)](https://dash.plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Usage Guide](#usage-guide)
- [Data Model](#data-model)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **Student Risk Analyzer** is a modern, data-driven platform designed to identify and address student challenges before they become critical. By combining automated data processing, rule-based risk assessment, and interactive visualizations, this system provides educators and students with actionable insights to improve academic outcomes and retention rates.

### Why Student Risk Analyzer?

- **Early Intervention**: Detect at-risk students before issues escalate
- **Transparency**: Clear, rule-based risk scoring that everyone can understand
- **Efficiency**: Automated data processing saves hours of manual work
- **Accessibility**: Web-based dashboards accessible from anywhere
- **Cost-Effective**: Built with open-source technologies, minimal infrastructure required

---

## ✨ Key Features

### 🎛️ Consolidated Dashboards

**Student Dashboard**
- Personalized view of academic performance metrics
- Real-time attendance tracking and visualization
- Fee payment status and financial overview
- Individual risk profile with actionable recommendations
- Secure login with student ID authentication

**Mentor Dashboard**
- Multi-student overview with sortable metrics
- At-risk student identification and filtering
- Comprehensive student data aggregation
- Alert notification system for urgent cases
- Batch monitoring capabilities

### 🔄 Automated Data Pipeline

- **Multi-Source Integration**: Seamlessly processes data from attendance, assessments, fees, and student records
- **Data Fusion**: Merges disparate CSV files into a unified student ledger
- **Error Handling**: Robust validation and error reporting
- **Performance Optimized**: Separate processing pipeline for data-heavy operations

### 📊 Transparent Risk Scoring Engine

The risk assessment system uses a clear, configurable rule-based approach:

- **Academic Performance**: Test scores, subject-wise performance tracking
- **Attendance Patterns**: Daily attendance monitoring and trend analysis
- **Financial Status**: Fee payment tracking and overdue monitoring
- **Risk Bands**: 
  - 🟢 **Green Zone**: Low risk, performing well
  - 🟡 **Amber Zone**: Moderate risk, requires monitoring
  - 🔴 **Red Zone**: High risk, immediate intervention needed

### 🔔 Smart Alert System

- Real-time notification bell for mentors
- Modal pop-ups highlighting critical student cases
- Detailed risk reasons and recommended actions
- Priority-based student sorting

### 💬 Integrated AI Counseling

- Floating chatbot button on student dashboard
- Immediate access to AI-powered counseling support
- Proactive mental health and academic guidance
- 24/7 availability for student queries

---

## 🏗️ System Architecture

### Technical Approach

The platform is built on a modular, Python-based architecture optimized for maintainability and scalability:

```
┌─────────────────────────────────────────────────────────┐
│                   Data Sources (CSV)                    │
│  students.csv │ attendance.csv │ assessments.csv │ fees.csv │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│              Data Pipeline (Pandas)                     │
│  • Data Ingestion  • Validation  • Transformation       │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│           Risk Scoring Engine (Rule-Based)              │
│  • KPI Calculation  • Rule Application  • Band Assignment│
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│              Web Application (Dash/Flask)               │
│  Student Dashboard          │        Mentor Dashboard   │
└─────────────────────────────────────────────────────────┘
```

### Core Components

1. **Data Pipeline** (`university_data_generator.py`)
   - CSV file ingestion and parsing
   - Data cleaning and normalization
   - Student ledger generation
   - Pandas-based transformations

2. **Risk Engine** (Embedded in processing logic)
   - Conditional logic-based scoring
   - Configurable thresholds
   - Transparent calculation methodology
   - Reason tracking and documentation

3. **Web Applications**
   - `app_student.py`: Student-facing interface
   - `app_mentor.py`: Mentor-facing interface
   - `app_manager.py`: Application orchestration

4. **Authentication System**
   - Secure credential validation
   - Session management
   - Role-based access control

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Backend** | Python 3.7+ | Core application logic |
| **Data Processing** | Pandas, NumPy | Data manipulation and analysis |
| **Web Framework** | Dash (Flask) | Interactive web dashboards |
| **Visualization** | Plotly | Charts and graphs |
| **Process Management** | psutil | Application control |
| **Data Generation** | Faker | Test data creation |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git (for cloning the repository)
- Modern web browser (Chrome, Firefox, Edge, Safari)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/abhishekkumar177/sih_idearepo.git
   cd sih_idearepo
   ```

2. **Create a Virtual Environment** (Recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install packages individually:
   ```bash
   pip install pandas numpy dash plotly Flask psutil Faker
   ```

4. **Generate Initial Data**
   ```bash
   python university_data_generator.py
   ```
   
   This creates:
   - `students.csv`
   - `attendance.csv`
   - `assessments.csv`
   - `fees.csv`
   - `mentors.csv`
   - `student_ledger.csv`

5. **Launch the Application Manager**
   ```bash
   python app_manager.py
   ```
   
   Navigate to `http://127.0.0.1:5000` in your browser.

---

## 📖 Usage Guide

### Starting the Applications

#### Option 1: Using the Application Manager (Recommended)

1. Run `python app_manager.py`
2. Open `http://127.0.0.1:5000`
3. Click "Start Mentor Dashboard" or "Start Student Dashboard"
4. Access the running application via the provided links

#### Option 2: Direct Execution

```bash
# For Student Dashboard
python app_student.py
# Access at http://127.0.0.1:8050

# For Mentor Dashboard
python app_mentor.py
# Access at http://127.0.0.1:8051
```

### Login Credentials

#### Student Login
- **Username**: Student ID (e.g., `2000`, `2001`, `2002`)
- **Password**: `password123`
- **Dashboard Port**: 8050

#### Mentor Login
- **Username**: Mentor ID (e.g., `mentor0`, `mentor1`, `mentor2`)
- **Password**: `password123`
- **Dashboard Port**: 8051

### Navigating the Student Dashboard

1. **Overview Panel**: View your risk status, attendance rate, and average scores
2. **Performance Metrics**: Track subject-wise test scores and trends
3. **Attendance Calendar**: Visual representation of attendance patterns
4. **Financial Status**: Current fee status and payment history
5. **Risk Analysis**: Detailed breakdown of your risk factors
6. **Counseling Bot**: Click the floating button for AI assistance

### Navigating the Mentor Dashboard

1. **Student List**: Sortable table of all assigned students
2. **Notification Bell**: Alerts for students in the Red Zone
3. **Risk Filters**: Quick filters to view students by risk band
4. **Detailed Views**: Click any student for comprehensive information
5. **Batch Actions**: Export reports or send notifications

---

## 📊 Data Model

### CSV File Structure

#### `students.csv`
| Column | Type | Description |
|--------|------|-------------|
| student_id | Integer | Unique student identifier |
| name | String | Student full name |
| branch | String | Academic branch/department |
| guardian_contact | String | Emergency contact number |
| mentor_id | String | Assigned mentor identifier |

#### `attendance.csv`
| Column | Type | Description |
|--------|------|-------------|
| student_id | Integer | Student identifier |
| date | Date | Attendance date |
| status | String | Present/Absent/Late |

#### `assessments.csv`
| Column | Type | Description |
|--------|------|-------------|
| student_id | Integer | Student identifier |
| subject | String | Subject name |
| test_name | String | Assessment identifier |
| score | Float | Test score (0-100) |
| max_score | Float | Maximum possible score |
| attempt | Integer | Attempt number |

#### `fees.csv`
| Column | Type | Description |
|--------|------|-------------|
| student_id | Integer | Student identifier |
| amount_due | Float | Outstanding amount |
| amount_paid | Float | Amount paid |
| due_date | Date | Payment deadline |
| payment_date | Date | Actual payment date |

#### `mentors.csv`
| Column | Type | Description |
|--------|------|-------------|
| login_id | String | Mentor username |
| name | String | Mentor full name |
| password | String | Hashed password |

### Generated Output

#### `student_ledger.csv`
Comprehensive view combining all data sources with computed metrics:
- All student demographic information
- Aggregated attendance percentage
- Average test scores by subject
- Fee payment status and overdue days
- **Risk score** and **risk band**
- **Risk reasons** (comma-separated list)

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. File Not Found Errors

**Symptom**: `FileNotFoundError: student_ledger.csv not found`

**Solution**:
```bash
# Generate all required data files
python university_data_generator.py
```

The data generator must be run at least once before starting any application.

---

#### 2. Module Import Errors

**Symptom**: `ModuleNotFoundError: No module named 'dash'`

**Solution**:
```bash
# Install all dependencies
pip install pandas numpy dash plotly Flask psutil Faker

# Or use requirements.txt if available
pip install -r requirements.txt
```

---

#### 3. Port Already in Use

**Symptom**: `OSError: [Errno 48] Address already in use`

**Solution**:
```bash
# Find and kill the process using the port
# macOS/Linux
lsof -ti:8050 | xargs kill -9

# Windows
netstat -ano | findstr :8050
taskkill /PID <process_id> /F
```

Or change the port in the application:
```python
app.run(debug=True, port=8052)
```

---

#### 4. Deprecated Method Warnings

**Symptom**: `app.run_server has been replaced by app.run`

**Solution**: Update your code to use the new method:
```python
# Old (deprecated)
app.run_server(debug=True)

# New (correct)
app.run(debug=True)
```

---

#### 5. Layout Display Issues

**Symptom**: Dashboard elements overflow or display incorrectly

**Solution**: Clear browser cache and ensure you're using the latest version of the application. The CSS has been updated with proper overflow handling:
```css
overflow-wrap: break-word;
word-wrap: break-word;
max-width: 100%;
```

---

#### 6. Login Failures

**Symptom**: Correct credentials rejected

**Common Causes**:
- Running wrong application (student credentials on mentor app)
- Data files not generated
- Credentials case sensitivity

**Solution**:
1. Verify you're on the correct dashboard (check page title)
2. Ensure `university_data_generator.py` has been run
3. Check credentials are lowercase (e.g., `2000`, not `Student_2000`)
4. Stop the application (`Ctrl + C`) and restart it

---

#### 7. Process Management Errors

**Symptom**: `OSError: [WinError 10038]` when stopping applications

**Solution**: Install and use the process manager:
```bash
pip install psutil
python app_manager.py
```

The app manager provides graceful process termination.

---

### Still Having Issues?

1. **Check Python Version**: Ensure you're using Python 3.7+
   ```bash
   python --version
   ```

2. **Verify File Integrity**: Ensure all CSV files were generated correctly
   ```bash
   ls -la *.csv
   ```

3. **Review Logs**: Check terminal output for detailed error messages

4. **Clean Restart**: 
   ```bash
   # Delete generated files
   rm *.csv
   # Regenerate data
   python university_data_generator.py
   # Restart application
   python app_manager.py
   ```

5. **Create an Issue**: If problems persist, open an issue on GitHub with:
   - Error message (full traceback)
   - Python version
   - Operating system
   - Steps to reproduce

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and ensure code quality
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Areas for Contribution

- 🐛 Bug fixes and issue resolution
- ✨ New features and enhancements
- 📝 Documentation improvements
- 🎨 UI/UX enhancements
- 🧪 Test coverage expansion
- 🌐 Internationalization support

### Code Style

- Follow PEP 8 guidelines for Python code
- Add docstrings to functions and classes
- Include comments for complex logic
- Write descriptive commit messages

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built for the Smart India Hackathon (SIH)
- Powered by the Dash and Plotly communities
- Inspired by modern educational technology needs

---

## 📞 Contact & Support

- **Developer**: Abhishek Kumar
- **GitHub**: [@abhishekkumar177](https://github.com/abhishekkumar177)
- **Repository**: [sih_idearepo](https://github.com/abhishekkumar177/sih_idearepo)

For questions, suggestions, or support, please open an issue on GitHub.

---

## 🗺️ Roadmap

### Upcoming Features

- [ ] Email notification system for alerts
- [ ] Export functionality for reports (PDF/Excel)
- [ ] Advanced analytics and predictive modeling
- [ ] Mobile-responsive design improvements
- [ ] Integration with Learning Management Systems (LMS)
- [ ] Multi-language support
- [ ] Dark mode theme
- [ ] Real-time collaboration features
- [ ] API endpoints for third-party integrations
- [ ] Machine learning-based risk prediction

---

<div align="center">

**Made with ❤️ for better education outcomes**

⭐ Star this repository if you find it helpful!

</div>