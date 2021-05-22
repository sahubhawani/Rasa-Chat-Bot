from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import zomatopy
import json

from email.message import EmailMessage
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

from tabulate import _table_formats, tabulate

supported_cities = pd.read_csv('data/lookup_tables/supported_cities.txt', header = None)
supported_cities.columns = ['City']
supported_cities['City'] = supported_cities['City'].str.lower()
supported_cities = supported_cities['City'].tolist()

unsupported_cities = pd.read_csv('data/lookup_tables/unsupported_cities.txt', header = None)
unsupported_cities.columns = ['City']
unsupported_cities['City'] = unsupported_cities['City'].str.lower()
unsupported_cities = unsupported_cities['City'].tolist()



def send_email(subject, message,destination):
    # important, you need to send it to a server that knows how to send e-mails for you
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # don't know how to do it without cleartexting the password and not relying on some json file that you dont git control...
    server.login('zomatobotapi@gmail.com', 'qazwsxEDCRFV@1234')
    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = subject
    msg['From'] = 'zomatobotapi@gmail.com'
    msg['To'] = destination
    server.send_message(msg)

	

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"2fcc0e3f040819697db623bdd17dfe44"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('supported_city')
		cuisine = tracker.get_slot('cuisine')
		min_budget = tracker.get_slot('min_budget')
		max_budget = tracker.get_slot('max_budget')
		if min_budget == None:
			min_budget = "0"
		if max_budget == None:
			max_budget = "10000"
		print(loc, cuisine, min_budget, max_budget)
		try:
			location_detail=zomato.get_location(loc, 1)
			d1 = json.loads(location_detail)
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			print('Successfully extracted location details !!')
		except Exception as e:
			print('Error in getting location details: ' + str(e))
		
		try:
			cuisines_dict={'Chinese':25,'Mexican':73,'Italian':55,'American':1,'Thai':95,'South Indian':85,'North Indian':50}
			results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 10000)
			d = json.loads(results)
			print('Successfully extracted Restaurant details !!')
		except Exception as e:
			print('Error in getting restaurant details: ' + str(e))
		response = ""
		try:
			if d['results_found'] == 0:
				response = "No Results"
			else:
				count = 1
				for restaurant in d['restaurants']:
					if count > 5:
						break
					if restaurant['restaurant']["average_cost_for_two"] > int(max_budget) or restaurant['restaurant']["average_cost_for_two"] <= int(min_budget):
						continue
					response += restaurant['restaurant']['name'] + "  in "
					response += restaurant['restaurant']['location']['locality_verbose']
					response += " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']+ ".\n"
					count += 1
				if count == 1:
					response = "No Results"	
					
		except Exception as e:
			print('Error:' + str(e))
			response = "No Results"
		
		dispatcher.utter_message(response)
		return [SlotSet('supported_city',loc)]


class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"2fcc0e3f040819697db623bdd17dfe44"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('supported_city')
		cuisine = tracker.get_slot('cuisine')
		email = tracker.get_slot('email')
		
		min_budget = tracker.get_slot('min_budget')
		max_budget = tracker.get_slot('max_budget')

		if min_budget == None or min_budget not in ["0", "300", "700", "10000"]:
			min_budget = "0"
		if max_budget == None or min_budget not in ["0", "300", "700", "10000"]:
			max_budget = "10000"
		print(loc, cuisine, email, min_budget, max_budget)

		if email.startswith("mailto:"):
			email = email.split('|')[1]
		try:
			location_detail=zomato.get_location(loc, 1)
			d1 = json.loads(location_detail)
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			print('Successfully extracted location details !!')
		except Exception as e:
			print('Error in getting location details: ' + str(e))
		
		try:
			cuisines_dict={'Chinese':25,'Mexican':73,'Italian':55,'American':1,'Thai':95,'South Indian':85,'North Indian':50}
			results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 10000)
			d = json.loads(results)
			print('Successfully extracted Restaurant details !!')
		except Exception as e:
			print('Error in getting restaurant details: ' + str(e))
		response = ""
		try:
			if d['results_found'] == 0:
				response = "No Results"
			else:
				count = 1
				result = []
				for restaurant in d['restaurants']:
					res_result = []
					if count > 10:
						break
					if restaurant['restaurant']["average_cost_for_two"] > int(max_budget) or restaurant['restaurant']["average_cost_for_two"] <= int(min_budget):
						continue
					res_result.append(str(restaurant['restaurant']['name']))
					res_result.append(str(restaurant['restaurant']['location']['locality_verbose']))
					res_result.append(str(restaurant['restaurant']["average_cost_for_two"]))
					res_result.append(str(restaurant['restaurant']['user_rating']['aggregate_rating']))
					#result.append(','.join(res_result))
					result.append(res_result)
					count += 1
				if count == 1:
					response = "No Results"	
					
		except Exception as e:
			print('Error:' + str(e))
			response = "No Results"

		msg = MIMEMultipart('alternative')
		msg = "Dear " + email.split('@')[0] + ", \n"
		msg += "Please find details of restaurants below: \n\n"


		format_list = list(_table_formats.keys())

		# Each element in the table list is a row in the generated table
		table = result
		headers = ["Restaurant Name", "Restaurant locality Address", "Average budget for two people", "Zomato user rating"]

		table_data = ''
				
		table_data = str(tabulate(table, headers, tablefmt='fancy_grid'))
		print(table_data)
		msg += table_data + "\n\n"
		msg += "\n\nThanks,\nZomato BOT"

		subject = 'Top 10 ' + str(cuisine) + ' restaurants in ' + str(loc) + " " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " !!"

		send_email(subject, msg, email)
		response = "Email sent to " + str(email)
		
		dispatcher.utter_message(response)
		return [SlotSet('email',email)]		

class CheckLocation(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		loc_lower = loc.lower()
		if loc_lower in supported_cities:
			return [SlotSet('supported_city',loc), SlotSet('unsupported_city',None), SlotSet('unknown_city',None)]
		elif loc_lower in unsupported_cities:
			return [SlotSet('unsupported_city',loc), SlotSet('supported_city',None), SlotSet('unknown_city',None)]
		return [SlotSet('unknown_city',loc), SlotSet('supported_city',None), SlotSet('unsupported_city',None)]			


