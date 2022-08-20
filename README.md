<h1 align="center">
  <br>
  <a href="https://github.com/haidargit/Python_Experiment-Salary_Conversion"><img src="https://images.unsplash.com/photo-1534951009808-766178b47a4f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="Salary Conversion" style="width:400px;height:266.67px;"></a>
</h1>
<h4 align="center">Python Experiment - Salary Conversion</h4>
<p align="center">
    <a href="https://github.com/haidargit/Python_Experiment-Salary_Conversion/commits/main">
    <img src="https://img.shields.io/github/last-commit/haidargit/Python_Experiment-Salary_Conversion.svg?style=flat-square&logo=github&logoColor=white"
         alt="GitHub last commit">
    <a href="https://github.com/haidargit/Python_Experiment-Salary_Conversion/issues">
    <img src="https://img.shields.io/github/issues-raw/haidargit/Python_Experiment-Salary_Conversion.svg?style=flat-square&logo=github&logoColor=white"
         alt="GitHub issues">
    <a href="https://github.com/haidargit/Python_Experiment-Salary_Conversion/pulls">
    <img src="https://img.shields.io/github/issues-pr-raw/haidargit/Python_Experiment-Salary_Conversion.svg?style=flat-square&logo=github&logoColor=white"
         alt="GitHub pull requests">
    <a href="https://twitter.com/intent/tweet?text=Try this Salary Conversion:&url=https%3A%2F%2Fgithub.com%2Fhaidargit%2FPython_Experiment-Salary_Conversion">
    <img src="https://img.shields.io/twitter/url/https/github.com/haidargit/Python_Experiment-Salary_Conversion.svg?style=flat-square&logo=twitter"
         alt="GitHub tweet">
</p>
<p align="center">
  <a href="#about">About</a> •
  <a href="#installation">Installation</a> •
  <a href="#updating">Updating</a> •
  <a href="#features">Features</a> •
  <a href="#credits">Credits</a> •
</p>

---

## About

<table>
<tr>
<td>
o We can fetch the example data from http://jsonplaceholder.typicode.com/users  
o Join the fetched data with the salary data from JSON file by using their ids  
o Add one field to represent salary in USD (salary in JSON file is in IDR) using currency converter (such as https://free.currencyconverterapi.com).  
Try to be efficient with the resource by not making a get request to endpoint after every conversion  
o Output from the endpoint should be: id, name, username, email, address, phone, salary in IDR, and salary in USD
</td>
</tr>
</table>

## Installation

##### Steps:
* Clone **[This Repo](https://github.com/haidargit/Python_Experiment-Salary_Conversion.git)**.

* Of course, make sure `you have Python on your machine`. You can download Python from this **[>>Link<<](https://www.python.org/)**.

* Register the free currency API on https://free.currencyconverterapi.com. (**Hmm**, per 20 Aug 2022 the website says: `due to abuse of this service, please send an` [email to the author](https://www.currencyconverterapi.com/contact) `with the subject: Request for Free Currency Converter API Key`)
  * Get your API key.

* Open the project/repo with any IDE/text editor that you desire to view the code and its resources.
  * The folder structure:
    * `./problem1.py`
    * `./salary_data.json`
`
* **Notes:** this repo requires additional module that you need to install. even on python per this version. 3.10. Because `requests` is not a built in module (does not come with the default python installation), so you will have to install it
  * if you use **Python 2**: run `sudo pip install requests`
  * or, if you use **Python 3**: run `sudo pip3 install requests`
  
* You can run the code by typing one of these command in the cmd/termnal. But you need to go the _problem3.py_ directory,
  * if you use **python 3**: run `python3 problem3.py`
  * if you use **python 2**: run `python problem3.py`

* You can see the result of currency converter in the terminal/console.