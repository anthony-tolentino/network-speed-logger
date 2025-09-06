# Network Speed Logger

A Python project that tests and logs internet speed over time using [speedtest-cli](https://github.com/sivel/speedtest-cli).

## Features
- Logs download, upload, and ping results
- Saves results into a CSV file
- Can be automated with cron jobs
- Designed for lightweight data analysis

## Folder Structure
```
network-speed-logger/
├── logs/                    # Cron and deub logs from speed tests
│   └── cron.log
│   └── debug.log
├── data/                    # CSV with data from speed tests
│   └── speed_data.csv
├── .env/                    # Virtual environment (ignored by git)
├── src                      # Main script
│   └── speedtest_logger.csv 
├── requirements.txt         # Project dependencies
├── .gitignore               # Git ignore file
└── README.md                # Project documentation
```

## Installation

Clone the repository:

```
git clone https://github.com/anthony-tolentino/network-speed-logger
cd network-speed-logger
```

Set up a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

## Usage
Run the logger manually:
```
python speedtest_logger.py
```

Automate with a cron job (example: every hour):
```
0 * * * * /path/to/python /path/to/speedtest_logger.py
```

Results are stored in:
```
data/speedtest_results.csv
```

## Example Output
| Timestamp           | Download (Mbps) | Upload (Mbps) | Ping (ms) |
|---------------------|-----------------|---------------|-----------|
| 2025-08-17 10:00:01 | 95.32           | 12.45         | 18.4      |
| 2025-08-17 11:00:01 | 88.11           | 11.92         | 20.1      |

## Future Improvements
- Add a dashboard to visualize trends
- Store results in a SQLite or PostgreSQL database instead of CSV
- Add alerting (send email/Slack/Discord if speed drops below threshold)
