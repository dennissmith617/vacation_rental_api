Dennis Smith
Vacation Home Rental API Program

**Summary**:
This Program serves as a prototype for a Vacation Home Rental API. It will allow customers to reserve homes of a given type at a desired date and time for a given number of days. Customers will be able to reserve a single home for multiple, non-overlapping time frames.

Testing is included in this program to show the functionality of the API.


**Pre-program Installations/Downloads**

1. Clone the `vacation_rental_api` repo.

2. Install Python3 by following the steps available at this link: https://www.python.org/downloads/

3. You will need Python 3.7 or newer to properly run this program. Enter `python3 --version` in your terminal to confirm you are running a supported version. 

4. Check that Pip is installed by entering `pip3 --version` in your terminal.

5. If Pip is not installed, follow this link for the installation process: https://pip.pypa.io/en/stable/installation/

6. If you do not have Flask installed, enter `pip3 install Flask` into your terminal.

7. Install Pipenv by entering `pip3 install pipenv` in your terminal. Pipenv will serve as a dependency manager which isolates projects in private environments. We will therefore be able to install packages per project by using this.

- To setup pipenv, you can run `pipenv --python VERSION`, where version can be found using `python3 --version` command

8. Install marshmallow by running `pip3 install -U marshmallow`. This is a framework-agnostic library which will help us convert complex datatypes (i.e. objects) to and from Python datatypes.

9. Install requests by running `pip3 install requests`

**Running the Program**

1. Make sure that you have navigated to the folder containing the repo, and run the server by entering `./bootstrap.sh` in your terminal.

2. Use an API Testing/Debugging Tool such as Insomnia or Postman to test the `get_rentals()` GET method or the `rent_home()` POST method. 

- **GET**
	- **URL**: localhost:5000/rentals

- **POST** 
	- **URL**: localhost:5000/rent
	- Example JSON Body:
	```
		{ 
			"home_id": 1, 
			"start_date": "2024-07-1",
			"end_date": "2024-07-6" 
		}
	```


**NOTE**: If you are using the POST request, make sure that you are entering an existing home_id (1-5) and using the proper date format (YYYY-MM-DD).

**Running the Tests**

1. Open up to a new terminal window, restart API to have clean data

2. Navigate to `tests`

3. Run `python3 test_index.py`
