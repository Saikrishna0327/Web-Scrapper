import requests
import json
menulist=['Work From Home Jobs','Part Time Jobs','Freshers Jobs','Women Jobs','Full Time Jobs', 'Night Shift Jobs','International Jobs']

def get_api_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the response
        return response.json()  # Parse the JSON data and return it as a Python dictionary
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if _name_ == "_main_":
    api_key = 'jJZ7iSTHujDZ9BjY1GTZQ'
    Jobtype = 'work_from_home-jobs'
    pageindex = 0

    all_data_list = []  # Initialize an empty list to store all the data

    while True:
        api_url = "https://apna.co/_next/data/" + api_key + "/jobs/" + Jobtype + ".json?page=" + str(pageindex) + "&work_from_home=1&paths=" + Jobtype
        api_response = get_api_response(api_url)
        print(api_url)

        print("Page Index : ",pageindex)
        if api_response:
            data_list = api_response.get('pageProps', {}).get('jobs', [])
            if not data_list:  # If the data list is empty, break out of the loop
                break

            all_data_list.extend(data_list)  # Append the data to the main list

        else:
            print(f"Failed to get a response from the API for page {pageindex}.")
            break

        pageindex += 1  # Move to the next page for the next iteration

    # Save all the data as a single JSON file
    with open('api_data_all.json', 'w') as json_file:
        json.dump(all_data_list, json_file, indent=4)

    print("Data saved as api_data_all.json")
