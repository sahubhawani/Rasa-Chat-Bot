## happy_path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"supported_city": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "0", "max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path3
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - utter_please_info
    - utter_greet
* restaurant_search    
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"supported_city": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "0", "max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_goodbye
    - action_restart  

## happy_path4
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}   
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"supported_city": "bengaluru"}
    - utter_ask_price_category
* restaurant_search{"max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_goodbye
    - action_restart  

## happy_path5
* restaurant_search{"location": "bengaluru", "cuisine": "Italian"}
    - slot{"location": "bengaluru"}
    - slot{"cuisine": "Italian"}
    - action_check_location
    - slot{"supported_city": "bengaluru"}
    - utter_ask_price_category
* restaurant_search{"max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_goodbye
    - action_restart 

## happy_path6
* restaurant_search{"location": "bengaluru", "cuisine": "Italian", "max_budget": "300"}
    - slot{"location": "bengaluru"}
    - slot{"cuisine": "Italian"}
    - action_check_location
    - slot{"supported_city": "bengaluru"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_goodbye
    - action_restart  

## happy_path7
* restaurant_search{"location": "bengaluru", "cuisine": "Italian", "min_budget": "0", "max_budget": "300"}
    - slot{"location": "bengaluru"}
    - slot{"cuisine": "Italian"}
    - action_check_location
    - slot{"supported_city": "bengaluru"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_goodbye
    - action_restart 

## happy_path8
* restaurant_search{"location": "bengaluru", "cuisine": "Italian", "min_budget": "0"}
    - slot{"location": "bengaluru"}
    - slot{"cuisine": "Italian"}
    - action_check_location
    - slot{"supported_city": "bengaluru"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_goodbye
    - action_restart                    

## happy_path2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"supported_city": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price_category
* restaurant_search{"max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_goodbye
    - action_restart    

## not_support_location
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"unsupported_city": "Rishikesh"}
    - utter_no_support
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"supported_city": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "700", "max_budget": "10000"}
    - slot{"min_budget": "700", "max_budget": "10000"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - slot{"email": "xyz@sth.edu"}
    - utter_goodbye
    - action_restart

## not_support_location2
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"unsupported_city": "Rishikesh"}
    - utter_no_support
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"supported_city": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "700"}
    - slot{"min_budget": "700", "max_budget": "10000"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - slot{"email": "xyz@sth.edu"}
    - utter_goodbye
    - action_restart    

## ask_for_email
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"supported_city": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "300", "max_budget": "700"}
    - slot{"min_budget": "300", "max_budget": "700"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_give_email
* send_email{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - utter_goodbye
    - action_restart

## no_email
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"supported_city": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "300", "max_budget": "700"}
    - slot{"min_budget": "300", "max_budget": "700"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## unknown_city
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengalooru"}
    - slot{"location": "bengalooru"}
    - action_check_location
    - slot{"unknown_city": "bengalooru"}
    - utter_unknown_city
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"supported_city": "kolkata"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "0", "max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## unknown_city2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengalooru"}
    - slot{"location": "bengalooru"}
    - action_check_location
    - slot{"unknown_city": "bengalooru"}
    - utter_unknown_city
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"supported_city": "kolkata"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price_category
* restaurant_search{"max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_goodbye
    - action_restart    

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"supported_city": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "0", "max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - slot{"supported_city": "kolkata"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"supported_city": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_category
* restaurant_search{"max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - slot{"supported_city": "kolkata"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart    

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}
    - action_check_location
    - slot{"unknown_city": "kolkatta"}
    - utter_unknown_city
* restaurant_search{"location": "kolkat"}
    - slot{"location": "kolkat"}
    - action_check_location
    - slot{"unknown_city": "kolkat"}
    - utter_unknown_city
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"supported_city": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "0", "max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - slot{"supported_city": "kolkata"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}
    - action_check_location
    - slot{"unknown_city": "kolkatta"}
    - utter_unknown_city
* restaurant_search{"location": "kolkat"}
    - slot{"location": "kolkat"}
    - action_check_location
    - slot{"unknown_city": "kolkat"}
    - utter_unknown_city
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"supported_city": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_category
* restaurant_search{"max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - slot{"supported_city": "kolkata"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart    

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "thane"}
    - slot{"location": "thane"}
    - action_check_location
    - slot{"unsupported_city": "thane"}
    - utter_no_support
* restaurant_search{"location": "Agartala"}
    - slot{"location": "Agartala"}
    - action_check_location
    - slot{"unsupported_city": "Agartala"}
    - utter_no_support
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"unsupported_city": "Rishikesh"}
    - utter_no_support
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"supported_city": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "0", "max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - slot{"supported_city": "Delhi"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_32
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "thane"}
    - slot{"location": "thane"}
    - action_check_location
    - slot{"unsupported_city": "thane"}
    - utter_no_support
* restaurant_search{"location": "Agartala"}
    - slot{"location": "Agartala"}
    - action_check_location
    - slot{"unsupported_city": "Agartala"}
    - utter_no_support
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"unsupported_city": "Rishikesh"}
    - utter_no_support
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"supported_city": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_category
* restaurant_search{"max_budget": "300"}
    - slot{"min_budget": "0", "max_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - slot{"supported_city": "Delhi"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart    

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"location": "Gaya"}
    - slot{"location": "Gaya"}
    - action_check_location
    - slot{"unsupported_city": "Gaya"}
    - utter_no_support
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"unknown_city": "mubaim"}
    - utter_unknown_city
* restaurant_search{"location": "Allahabada"}
    - slot{"location": "Allahabada"}
    - action_check_location
    - slot{"unknown_city": "Allahabada"}
    - utter_unknown_city
* restaurant_search{"location": "kolkkata"}
    - slot{"location": "kolkkata"}
    - action_check_location
    - slot{"unknown_city": "kolkkata"}
    - utter_unknown_city
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"supported_city": "chandigarh"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "700", "max_budget": "10000"}
    - slot{"min_budget": "700", "max_budget": "10000"}
    - utter_showing_results
    - action_search_restaurants
    - slot{"supported_city": "chandigarh"}
    - utter_ask_email
* send_email{"email": "hdfks@cdsld.hcs"}
    - slot{"email": "hdfks@cdsld.hcs"}
    - action_send_email
    - slot{"email": "hdfks@cdsld.hcs"}
    - utter_goodbye
    - action_restart

## interactive_story_42
* greet
    - utter_greet
* restaurant_search{"location": "Gaya"}
    - slot{"location": "Gaya"}
    - action_check_location
    - slot{"unsupported_city": "Gaya"}
    - utter_no_support
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"unknown_city": "mubaim"}
    - utter_unknown_city
* restaurant_search{"location": "Allahabada"}
    - slot{"location": "Allahabada"}
    - action_check_location
    - slot{"unknown_city": "Allahabada"}
    - utter_unknown_city
* restaurant_search{"location": "kolkkata"}
    - slot{"location": "kolkkata"}
    - action_check_location
    - slot{"unknown_city": "kolkkata"}
    - utter_unknown_city
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"supported_city": "chandigarh"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "700"}
    - slot{"min_budget": "700", "max_budget": "10000"}
    - utter_showing_results
    - action_search_restaurants
    - slot{"supported_city": "chandigarh"}
    - utter_ask_email
* send_email{"email": "hdfks@cdsld.hcs"}
    - slot{"email": "hdfks@cdsld.hcs"}
    - action_send_email
    - slot{"email": "hdfks@cdsld.hcs"}
    - utter_goodbye
    - action_restart    

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigrh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigrh"}
    - action_check_location
    - slot{"unknown_city": "chandigrh"}
    - slot{"supported_city": null}
    - slot{"unsupported_city": null}
    - utter_unknown_city
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"unsupported_city": "Rishikesh"}
    - slot{"supported_city": null}
    - slot{"unknown_city": null}
    - utter_no_support
* restaurant_search{"location": "udaipur"}
    - slot{"location": "udaipur"}
    - action_check_location
    - slot{"unsupported_city": "udaipur"}
    - slot{"supported_city": null}
    - slot{"unknown_city": null}
    - utter_no_support
* restaurant_search{"location": "mubai"}
    - slot{"location": "mubai"}
    - action_check_location
    - slot{"unknown_city": "mubai"}
    - slot{"supported_city": null}
    - slot{"unsupported_city": null}
    - utter_unknown_city
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"supported_city": "chandigarh"}
    - slot{"unsupported_city": null}
    - slot{"unknown_city": null}
    - utter_ask_price_category
* restaurant_search{"min_budget": "300", "max_budget": "700"}
    - slot{"min_budget": "300", "max_budget": "700"}
    - utter_showing_results
    - action_search_restaurants
    - slot{"supported_city": "chandigarh"}
    - utter_ask_email
* send_email{"email": "dhksk@jjvx.com"}
    - slot{"email": "dhksk@jjvx.com"}
    - action_send_email
    - slot{"email": "dhksk@jjvx.com"}
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"supported_city": "Bangalore"}
    - slot{"unsupported_city": null}
    - slot{"unknown_city": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "300, max_budget:700"}
    - slot{"min_budget": "300, max_budget:700"}
    - utter_showing_results
    - action_search_restaurants
    - slot{"supported_city": "Bangalore"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"supported_city": "Bangalore"}
    - slot{"unsupported_city": null}
    - slot{"unknown_city": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price_category
* restaurant_search{"min_budget": "300", "max_budget": "700"}
    - slot{"max_budget": "700"}
    - slot{"min_budget": "300"}
    - utter_showing_results
    - action_search_restaurants
    - slot{"supported_city": "Bangalore"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart
