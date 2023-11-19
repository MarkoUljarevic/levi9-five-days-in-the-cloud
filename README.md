<h1 align="center">
  <a href="https://github.com/MarkoUljarevic/levi9-five-days-in-the-cloud">
    Basketball Player Statistics Processing
  </a>
</h1>

<details open="open">
<summary id="table-of-contents">Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

</details>

---

## About

This project utilizes FastAPI, a modern, fast (high-performance), web framework for building APIs with Python. The server processes basketball player statistics sourced from a CSV file, offering advanced insights through a single REST endpoint. The choice of Python and FastAPI ensures simplicity and rapid development.


### Built With

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
<div align="right">[ <a href="#table-of-contents">↑ Back to top ↑</a> ]</div>

## Getting Started

### Prerequisites

- **Python Programming Language**: You will need Python installed to run this program. If you haven't installed Python, you can download it [here](https://www.python.org/downloads/)
- **Pip Package Installer**: You will use pip to install packages from the Python Package Index and other indexes. Usually, pip is automatically installed if you downloaded Python from [python.org](https://www.python.org/)
- **Uvicorn and FastAPI**: They are needed to successfully run Python server. They will be installed with pip from requirements.txt 


### Installation

First, open shell and clone repository by using `git clone`
```
git clone https://github.com/MarkoUljarevic/levi9-five-days-in-the-cloud
```
Reposition in the `levi9-five-days-in-the-cloud`
```
cd levi9-five-days-in-the-cloud
```
And then install all the requirements

*For Python 3*
```
pip3 install -r requirements.txt
```
*For Python version less than 3*
```
pip install -r requirements.txt
```
<div align="right">[ <a href="#table-of-contents">↑ Back to top ↑</a> ]</div>

## Usage

**Run the FastAPI server:**

*For Python 3*
```
python3 main.py <csv_file_path> [--csv_encoding <encoding>] [-p <port>]
```
*For Python version less than 3*
```
python main.py <csv_file_path> [--csv_encoding <encoding>] [-p <port>]
```
Default encoding is *utf-8-sig*, and default port is *8000*

**Get player statistics:**
```
curl http://localhost:8000/stats/player/{player_name}
```

**Run unit tests:**
```
python test.py
```

<div align="right">[ <a href="#table-of-contents">↑ Back to top ↑</a> ]</div>

## Acknowledgements

The project idea and specification are provided by [Levi9](https://www.levi9.com/)
<div align="right">[ <a href="#table-of-contents">↑ Back to top ↑</a> ]</div>
