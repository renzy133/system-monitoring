# System Monitoring Tool 🖥️

A Python-based system monitoring tool that provides real-time tracking of system performance and resources. This tool helps monitor CPU usage, memory consumption, disk space, and other critical system metrics.

## 🚀 Features

* Real-time CPU usage monitoring
* Memory (RAM) utilization tracking
* Disk space analysis
* Network usage statistics
* System temperature monitoring
* Email notifications for critical events

## 🛠️ Technologies

* Python 3.8+
* psutil - System monitoring
* pandas - Data analysis
* matplotlib - Data visualization
* smtplib - Email notifications

## 📋 Prerequisites

* Python 3.8 or higher
* pip package manager

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/renzy133/system-monitoring.git
cd system-monitoring
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the main monitoring script:
```bash
python src/monitor.py
```

## 📁 Project Structure

```
system-monitoring/
├── src/
│   ├── monitor.py      # Main monitoring script
│   ├── utils.py        # Utility functions
│   └── alerts.py       # Alert system
├── tests/              # Unit tests
├── docs/              # Documentation
├── requirements.txt   # Project dependencies
└── README.md
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
