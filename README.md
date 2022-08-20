<h1 align="center">
  <br>
  <a href="https://github.com/haidargit/Python_Experiment-Salary_Conversion"><img src="https://images.unsplash.com/photo-1534951009808-766178b47a4f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="Salary Conversion" style="width:200px;height:133.33px;"></a>
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
  <a href="#credits">Credits</a> 
</p>

---

## About

<table>
<tr>
<td>
o We can fetch the example data of Employee from http://jsonplaceholder.typicode.com/users

<br />o Join the fetched data with the salary data from JSON file by using their ids  

o Add one field to represent salary in USD (salary in JSON file is in IDR) using currency converter (such as https://free.currencyconverterapi.com).  
Try to be efficient with the resource by not making a get request to endpoint after every conversion  

o Output from the endpoint:  
_id, name, username, email, address, phone, salary in IDR, and salary in USD_
</td>
</tr>
</table>

## Installation

##### Steps:
* Clone **[This Repo](https://github.com/haidargit/Python_Experiment-Salary_Conversion.git)**.

* Of course, we need to make sure that `you have Python on your machine`.  
  You can download Python from this <a href="https://www.python.org/" target="_blank"> >>**Link**<< </a>.

* Register the free currency API on https://free.currencyconverterapi.com.  
  (🤔 &nbsp; **Hmm**, per August 2022 the website says:  
  `"due to abuse of this service, please send an` [email to the author](https://www.currencyconverterapi.com/contact) `with the subject:`  
  `Request for Free Currency Converter API Key"`)
  * No worries, here's the alternative api.
  * Register and get your API key.

* Open the project/repo with any IDE/text editor that you desire to view the code and its resources.
  * The folder structure:
    * `./currencyconv.py`
    * `./salary_data.json`
`
* **Notes:** this repo requires additional module that you need to install. even on python per this version. 3.10. Because `requests` is not a built in module (does not come with the default python installation), so you will have to install it
  * if you use **Python 2**: run `sudo pip install requests`
  * or, if you use **Python 3**: run `sudo pip3 install requests`
  
* You can run the code by typing one of these command in the cmd/termnal. But you need to navigate to the _currencyconv.py_ directory,
  * if you use **python 3**: run `python3 currencyconv.py`
  * if you use **python 2**: run `python currencyconv.py`

* Voila, you can immediately see the result of currency converter in the terminal/console.

## Credits
| [![fixer.io](https://fixer.io/fixer_images/fixer_money.png)](https://fixer.io/) |
|:------------------------------------------------------------------------------------------------------------------------:	|
|                                                    **Fixer**                                                    | 
