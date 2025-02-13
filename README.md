# 🚀 CPU Usage Monitor

## 📌 Project Description
A Python script that continuously monitors CPU usage and alerts the user when it exceeds a predefined threshold. This can help track system performance and prevent overheating or excessive load on the processor.

## 📖 Table of Contents
1. [⚙️ Prerequisites](https://github.com/Jidendiran-coder/Monitoring_Server_Health_Python#%EF%B8%8F-prerequisites)
2. [📥 Installation Instructions](https://github.com/Jidendiran-coder/Monitoring_Server_Health_Python#-installation-instructions)
3. [📝 Usage Instructions](https://github.com/Jidendiran-coder/Monitoring_Server_Health_Python#-usage-instructions)
4. [🔧 Configuration](https://github.com/Jidendiran-coder/Monitoring_Server_Health_Python#-configuration)
5. [🚀 CI/CD Pipeline Details](https://github.com/Jidendiran-coder/Monitoring_Server_Health_Python#-cicd-pipeline-details)
6. [🔒 Security Best Practices](https://github.com/Jidendiran-coder/Monitoring_Server_Health_Python#-security-best-practices)
7. [🐞 Troubleshooting](https://github.com/Jidendiran-coder/Monitoring_Server_Health_Python#-troubleshooting)
8. [🤝 Contribution Guidelines](https://github.com/Jidendiran-coder/Monitoring_Server_Health_Python#-contribution-guidelines)
9. [📜 License](https://github.com/Jidendiran-coder/Monitoring_Server_Health_Python#-license)
10. [📸 Screenshots & Architecture Diagrams](https://github.com/Jidendiran-coder/Monitoring_Server_Health_Python#-screenshots--architecture-diagrams)
11. [📅 Changelog](https://github.com/Jidendiran-coder/Monitoring_Server_Health_Python#-changelog)

## ⚙️ Prerequisites
- 🐍 Python 3.x installed on your system
- 📦 `psutil` module installed for CPU monitoring

## 📥 Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cpu-usage-monitor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd cpu-usage-monitor
   ```
3. Install dependencies:
   ```bash
   pip install psutil
   ```

## 📝 Usage Instructions
1. Run the script:
   ```bash
   python cpu_monitor.py
   ```
2. The script will start monitoring CPU usage in real-time.
3. If CPU usage exceeds the threshold (default: 80%), an alert message will be displayed.
4. Press `Ctrl+C` to stop monitoring.

## 🔧 Configuration
- Modify the `CPU_USAGE_THRESHOLD` variable in the script to set a custom alert level.

## 🚀 CI/CD Pipeline Details
- This project can be integrated into a CI/CD pipeline to monitor CPU usage during automated testing or deployments.

## 🔒 Security Best Practices
- Ensure the script runs with minimal privileges to avoid unnecessary system access.
- Do not modify system files or execute privileged commands without proper authorization.

## 🐞 Troubleshooting
- If `psutil` is not installed, run:
  ```bash
  pip install psutil
  ```
- Ensure Python is properly installed and added to the system PATH.

## 🤝 Contribution Guidelines
- Fork the repository and submit a pull request with improvements.

## 📜 License
This project is licensed under the MIT License.

## 📸 Output Screenshot
![image](https://github.com/user-attachments/assets/8af8c8f0-857d-4092-acb2-03193cab1749)

While Interupted:

![image](https://github.com/user-attachments/assets/b4b6bd95-b5e0-45ad-b2b4-8de781c6286b)

## 📅 Changelog
- **v1.0** - Initial release with basic CPU usage monitoring.

