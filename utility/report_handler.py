
from .niche_details import *
import multiprocessing
import pandas as pd
from .html_content import *
from .email_sender import *
from datetime import date
from .data_base_handler import *

def niche_wise_data(niche):
    nice_data = {}
    bind_country_code = [(country_code,niche) for country_code in country_code_list]
  
    with multiprocessing.Pool() as pool:
        result = pool.map(get_country_wise_data, bind_country_code)

    final_niche_dict = {}
    for item in result:
        if item is not None:
            for key, value in item.items():
                final_niche_dict['Items'] = list(value.keys())
                final_niche_dict[key] = list(value.values())
    # print(final_niche_dict)
    return final_niche_dict

def all_data(final_niche_dict):
    totalList = list(final_niche_dict.values())[1:]
    total_count = [sum(totalCount) for totalCount in zip(*totalList)]

    total_business_count = total_count[0]
    # print(f"total_business_count...........",total_business_count)
    total_percentage = [f"{int(((totalCount/total_business_count)*100))} %"for totalCount in total_count[1:]]
    total_percentage.insert(0," ")

    final_niche_dict['Total Count'] =  total_count
    final_niche_dict['Percentage'] = total_percentage
    desired_order_of_final_report = list(final_niche_dict.keys())[:-2]
    desired_order_of_final_report.insert(1,'Total Count')
    desired_order_of_final_report.insert(2,'Percentage')

    First_email = {key: final_niche_dict[key] for key in desired_order_of_final_report if key in final_niche_dict}
    return First_email

def basic_database_report(final_niche_dict):
    # Extract totalList excluding the first element (assumed to be 'Items')
    totalList = list(final_niche_dict.values())[1:]
    
    # Summing corresponding values from each sublist
    total_count = [sum(totalCount) for totalCount in zip(*totalList)]

    # Calculate percentage for all items except the first (total business count)
    total_business_count = total_count[0]
    total_percentage = [f"{int(((totalCount / total_business_count) * 100))} %" for totalCount in total_count[1:]]
    total_percentage.insert(0, " ")

    # Add Total Count and Percentage back to the dictionary
    final_niche_dict['Total Count'] = total_count
    final_niche_dict['Percentage'] = total_percentage
    
    # Re-order the dictionary keys
    desired_order_of_final_report = list(final_niche_dict.keys())[:-2]
    desired_order_of_final_report.insert(1, 'Total Count')
    desired_order_of_final_report.insert(2, 'Percentage')

    # Create a new dictionary preserving the desired order
    First_email = {key: final_niche_dict[key] for key in desired_order_of_final_report if key in final_niche_dict}
    
    # Format numbers in 'Total Count' only
    if 'Total Count' in First_email:
        First_email['Total Count'] = ['{:,}'.format(value) for value in First_email['Total Count']]
    
    # Create DataFrame and convert to HTML
    df = pd.DataFrame(First_email)
    html = df.to_html(index=False)

    # Print the formatted dictionary
    # print(First_email)
    
    return html


def database_report_country_by_usa(final_niche_dict):
    usa = final_niche_dict['usa']
    
    for country in country_code_list:
        try:
            country_report = final_niche_dict[country]
            # Calculate percentage for each country based on the USA report
            usa_country_per = [(f"{round(((country_report_l / (usa_l if usa_l != 0 else 1)) * 100), 1)} %") 
                            for usa_l, country_report_l in zip(usa, country_report)]
            final_niche_dict[f'{country}_usp'] = usa_country_per
        except Exception as e:
            country_report = 0

    # Format the 'Total Count' values with commas
    final_niche_dict['Total Count'] = ['{:,}'.format(value) for value in final_niche_dict['Total Count']]
    
    # Create a dictionary preserving only the keys from 'desired_list'
    second_email = {key: final_niche_dict[key] for key in desired_list if key in final_niche_dict}
    
    # print(second_email)
    
    # Convert the dictionary to a DataFrame and then to HTML
    df = pd.DataFrame(second_email)
    html1 = df.to_html(index=False)
    
    return html1

def database_report_business_every_10k_people(final_niche_dict):
    total_counts_of_country = {}

    for c in [country for country in final_niche_dict.keys() if country != "Items"]:
      
        total_counts_of_country[c] = final_niche_dict[c][0]

    niche_total_count_list = []
    usa_total_count = 0
    for country_code in country_code_list:
        total_count = total_counts_of_country.get(country_code)
        if total_count != None:
            if country_code == "usa":
                usa_total_count = round(((total_count/population_list.get(country_code))*10000),3)
            niche_total_count_list.append({country_code:{'total_count': total_count,"business_per_10k":round(((total_count/population_list.get(country_code))*10000),3),f"{country_code}/usa":f"{round((((-(usa_total_count - ((total_count/population_list.get(country_code))*10000)))/usa_total_count)*100),0)} % "}})
        else:
            niche_total_count_list.append({country_code:{'total_count': 0,"business_per_10k":0,f"{country_code}/usa":0}})
    # print(niche_total_count_list)
    return niche_total_count_list

# def database_report_business_for_clinic_count(final_niche_dict):
#     total_counts_of_country = {}

#     for c in [country for country in final_niche_dict.keys() if country != "Items"]:
      
#         total_counts_of_country[c] = final_niche_dict[c][0]

#     niche_total_count_list = []
#     usa_total_count = 0
#     for country_code in country_code_list:
#         total_count = total_counts_of_country.get(country_code)
#         # print(f"total_count...............",total_count)
#         if total_count != None:
#             if country_code == "usa":
#                 usa_total_count = total_count
#                 print(f"usa_count................",usa_total_count)
#             # niche_total_count_list.append({country_code:{'total_count': total_count,"business_per_clinic":round(((population_list.get(country_code))/total_count),2),f"{country_code}/usa":f"{round(((((usa_total_count - ((population_list.get(country_code))/total_count)))/usa_total_count)*100),0)} %"}})
            
#             niche_total_count_list.append({country_code:{'total_count': total_count,"business_per_clinic":int(round(((population_list.get(country_code))/total_count),0)),f"{country_code}/usa":f"{int(round((((total_count/usa_total_count))*100),0))} %"}})
#         else:
#             niche_total_count_list.append({country_code:{'total_count': 0,"business_per_clinic":0,f"{country_code}/usa":0}})
#     print(niche_total_count_list)
#     return niche_total_count_list

def all_niche_data():
    All_data = []
    for niche in niche_list:
        data = niche_wise_data(niche)
        All_data.append(all_data(data))
    
    # Extract items from the first element of All_data
    if All_data:
        items_list = All_data[0]['Items']
    else:
        items_list = []

    result = {
        'Items': items_list,
        'Total Count': [0] * len(items_list),  
        'Percentage': [' '] * len(items_list)  
    }
    
    # Initialize lists to store the sum of percentages and count of valid entries
    percentage_sums = [0] * len(items_list)
    percentage_counts = [0] * len(items_list)

    # Sum Total Count and handle Percentage
    for value in All_data:
        counts = value['Total Count']
        percentages = value['Percentage']

        # Sum Total Count
        for i in range(len(counts)):
            result['Total Count'][i] += counts[i]
        
        # Accumulate Percentage and count valid percentage entries
        for i in range(len(percentages)):
            percentage_value = percentages[i].strip()

            if percentage_value and percentage_value != ' ':
                try:
                    percent_value = float(percentage_value.replace('%', '').strip())
                    percentage_sums[i] += percent_value
                    percentage_counts[i] += 1
                except ValueError:
                    print(f"Warning: Could not convert percentage {percentages[i]} at index {i}")

    # Calculate the average percentages
    for i in range(len(percentage_sums)):
        if percentage_counts[i] > 0:  # Avoid division by zero
            avg_percentage = percentage_sums[i] / percentage_counts[i]
            result['Percentage'][i] = f"{int(avg_percentage)}%"

    # Format the Total Count values with commas
    result['Total Count'] = ['{:,}'.format(count) for count in result['Total Count']]

    # print(result)
    
    # Create DataFrame and convert to HTML
    df = pd.DataFrame(result)
    html = df.to_html(index=False)
    
    return html

def report_generator():
    Data = all_niche_data()
    basic_database_report_dict = {}
    database_report_country_by_usa_dict = {}
    database_report_business_every_10k_people_dict = {}
    # database_report_business_clinic_count_dict = {}

    for niche in niche_list:
        data = niche_wise_data(niche)
        basic_database_report_dict[niche]= basic_database_report(data)
        database_report_country_by_usa_dict[niche] = database_report_country_by_usa(data)
        database_report_business_every_10k_people_dict[niche] = database_report_business_every_10k_people(data)
        # database_report_business_clinic_count_dict[niche] = database_report_business_for_clinic_count(data)
        
    for key, value in database_report_business_every_10k_people_dict.items():
        merged_dict = {}
        for item in value:
            merged_dict.update(item)
        database_report_business_every_10k_people_dict[key]= merged_dict

    all_data_html = all_niche_data_html(Data,style=style)

    html = html_content_generator_with_all_data(Data=all_data_html,dict=basic_database_report_dict,style=style)
    email_sender(html_content=html,subject_as_per_mail=subject)

    html1 = html_content_generator(dict=database_report_country_by_usa_dict,style=style2)
    email_sender(html_content=html1,subject_as_per_mail=subject_usa_per)
    
    html_10k = html_content_generator_10k(master_data_dict=database_report_business_every_10k_people_dict,style=style3)
    email_sender(html_content=html_10k,subject_as_per_mail=subject_10k,is_business_10k=True)  

    # html_10k = html_content_generator_clinic(master_data_dict=database_report_business_clinic_count_dict,style=style3)
    # email_sender(html_content=html_10k,subject_as_per_mail=subject_10k,is_business_10k=True) 
    # print(database_report_business_clinic_count_dict)
