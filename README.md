# 📖 **Loggers for Python**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🌐 **Project Overview**

This repository demonstrates various configurations of a Python logger for the purpose of self-study. There is no general introduction to loggers contained. If you are interested in understanding the concept of loggers in particular how you do it in Pyhton you may visit the official Python documentation for the logging module:

https://docs.python.org/3/library/logging.html

## 🗂️ Structure

There are eleven folders each containing one configuration for a Python logger. Each folder has the following structure:

```text
xx-logger-example/
├── main.py
├── firstChild.py
└── secondChild.py
```

The logger configurations are set in the `main.py` file. In addition there is a function defined named `log_messages` to demonstrate log messages for all logging levels. The other two files have functions `first_logs` and `second_logs` which also create log messages for all logging levels but both functions are called from `main.py`.

Choose an example, switch to the corresponding folder and then run the file `main.py` to see the output of the logs.