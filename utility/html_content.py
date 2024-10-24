
from utility.niche_details import *

style = """
            <style>
                
                p{
                color: black;
                }
                table, th, td {
                            border: 2px solid rgb(8, 7, 7);
                            border-collapse: collapse;
                            text-align: center;
                            padding: 10px;
                            color: black;
                            }
            th {
            background-color: rgb(128, 128, 128);
            font-size: 25px;
            text-transform: uppercase;
            color: white;
            border: 1px solid rgb(8, 7, 7);
            }
            td {
            font-size: 18px;
            background-color: rgb(255, 255, 255);
            border: 1px solid rgb(8, 7, 7);
            }
            h2{
            text-align: center;
            }
            </style>
        """

style2 = """
            <style>
                
                p{
                color: black;
                }
                table, th, td {
                            border: 2px solid rgb(8, 7, 7);
                            border-collapse: collapse;
                            text-align: center;
                            padding: 10px;
                            color: black;
                            }
            th {
            background-color: rgb(128, 128, 128);
            font-size: 12px;
            text-transform: uppercase;
            color: white;
            border: 1px solid rgb(8, 7, 7);
            }
            td {
            font-size: 15px;
            background-color: rgb(255, 255, 255);
            border: 1px solid rgb(8, 7, 7);
            }
            h2{
            text-align: center;
            }
            </style>
        """

style3 = """
            <style>
                
                p{
                color: black;
                }
                table, th, td {
                            border: 2px solid rgb(8, 7, 7);
                            border-collapse: collapse;
                            text-align: center;
                            padding: 10px;
                            color: black;
                            }
            th {
            background-color: rgb(128, 128, 128);
            font-size: 12px;
            text-transform: uppercase;
            color: white;
            border: 1px solid rgb(8, 7, 7);
            }
            td {
            font-size: 12px;
            background-color: rgb(255, 255, 255);
            border: 1px solid rgb(8, 7, 7);
            }
            h2{
            text-align: center;
            }
            </style>
        """

def all_niche_data_html(dict,style):
    html_final_content = f"""
                            <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                {style}
                                </head>
                                <body>
        <table style= "border:none;">
        <tr style = "border:none">
            <td style="display: inline-block;align-items: center; border:none;">
        <h2 style = "text-align:center; text-transform: uppercase;">All Niche Report</h2>
        {dict}
        </td>
        </tr>
        </table>
        """
    return html_final_content

def html_content_generator_with_all_data(Data,dict,style):
    html_final_content = f"""
                            <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                {style}
                                </head>
                                <body>
                                <p>Hi Team</p>
                                <p>Please find the all database report below</p><br><br>
                                {Data}
                            """
    for niche, table in dict.items():
        html_final_content += f"""
        <table style= "border:none;">
        <tr style = "border:none">
            <td style="display: inline-block;align-items: center; border:none;">
        <h2 style = "text-align:center; text-transform: uppercase;">{str(niche).replace("_"," ")}</h2>
        {table}
        </td>
        </tr>
        </table>
"""
        
    html_final_content += f"""
                            <p><b>Note: This is auto generated database report.</b></p>
                            </body></html>
                        """

    # with open('testHtml.html', 'w') as f:
    #     f.write(html_final_content)

    return html_final_content


def html_content_generator(dict,style):
    html_final_content = f"""
                            <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                {style}
                                </head>
                                <body>
                                <p>Hi Team</p>
                                <p>Please find the all database report below</p><br><br>
                            """
    for niche, table in dict.items():
        html_final_content += f"""
        <table style= "border:none;">
        <tr style = "border:none">
            <td style="display: inline-block;align-items: center; border:none;">
        <h2 style = "text-align:center; text-transform: uppercase;">{str(niche).replace("_"," ")}</h2>
        {table}
        </td>
        </tr>
        </table>
"""
        
    html_final_content += f"""
                            <p><b>Note: This is auto generated database report.</b></p>
                            </body></html>
                        """

    # with open('testHtml.html', 'w') as f:
    #     f.write(html_final_content)

    return html_final_content

def table_formate(master_data_dict):
    trs = ""
    for niche in niche_list:
        tr = ""
        tr = f"""
                <tr>
                <td>{str(niche).upper()}</td>
                <td>{master_data_dict[niche]['usa']['total_count']}</td>
                <td>{master_data_dict[niche]['usa']['business_per_10k']}</td>
                """
        for country in country_code_list:
            if country != "usa":
                tr += f"""
                        <td>{master_data_dict[niche][country]['total_count']}</td>
                        <td>{master_data_dict[niche][country]['business_per_10k']}</td>
                        <td>{master_data_dict[niche][country][f'{country}/usa']}</td>
                        """
        tr += """</tr>"""
        trs += tr
    return trs

def table_formate_clinic(master_data_dict):
    trs = ""
    for niche in niche_list:
        tr = ""
        niche_data = master_data_dict[niche]  # This is a list of dictionaries
        usa_data = next((item for item in niche_data if 'usa' in item), None)
        
        if usa_data:
            tr = f"""
                <tr>
                <td>{str(niche).upper()}</td>
                <td>{usa_data['usa']['total_count']}</td>
                <td>{usa_data['usa']['business_per_clinic']}</td>
                """
            for country in country_code_list:
                if country != "usa":
                    country_data = next((item for item in niche_data if country in item), None)
                    if country_data:
                        tr += f"""
                            <td>{country_data[country]['total_count']}</td>
                            <td>{country_data[country]['business_per_clinic']}</td>
                            <td>{country_data[country][f'{country}/usa']}</td>
                            """
            tr += """</tr>"""
            trs += tr
    return trs


def html_content_generator_10k(master_data_dict,style):

    html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {style3}
            <title>Document</title>
            </head>
            <body>
            <p>Hi Team</p>
            <p>Please find the all database report below</p><br><br>
                <table>
                <thead>
                    <tr>
                    <th>Niche</th>
                    <th>US</th>
                    <th>USA/10K</th>
                    <th>CA</th>
                    <th>CA/10K</th>
                    <th>CA/USA</th>
                    <th>UK</th>
                    <th>UK/10K</th>
                    <th>UK/USA</th>
                    <th>AU</th>
                    <th>AU/10K</th>
                    <th>AU/USA</th>
                    <th>SE</th>
                    <th>SE/10K</th>
                    <th>SE/USA</th>
                    <th>DK</th>
                    <th>DK/10K</th>
                    <th>DK/USA</th>
                    <th>NZ</th>
                    <th>NZ/10K</th>
                    <th>NZ/USA</th>
                    <th>UAE</th>
                    <th>UAE/10K</th>
                    <th>UAE/USA</th>
                    </tr>
                </thead>
                <tbody>
                {table_formate(master_data_dict)}
                </tbody>
                </table>
            </body>
            </html>
    """

    return html

# def html_content_generator_clinic(master_data_dict,style):

#     html = f"""
#             <!DOCTYPE html>
#             <html lang="en">
#             <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             {style3}
#             <title>Document</title>
#             </head>
#             <body>
#             <p>Hi Team</p>
#             <p>Please find the all database report below</p><br><br>
#                 <table>
#                 <thead>
#                     <tr>
#                     <th>Niche</th>
#                     <th>US</th>
#                     <th>USA/clinic</th>
#                     <th>CA</th>
#                     <th>CA/clinic</th>
#                     <th>CA/USA</th>
#                     <th>UK</th>
#                     <th>UK/clinic</th>
#                     <th>UK/USA</th>
#                     <th>AU</th>
#                     <th>AU/clinic</th>
#                     <th>AU/USA</th>
#                     <th>SE</th>
#                     <th>SE/clinic</th>
#                     <th>SE/USA</th>
#                     <th>DK</th>
#                     <th>DK/clinic</th>
#                     <th>DK/USA</th>
#                     <th>NZ</th>
#                     <th>NZ/clinic</th>
#                     <th>NZ/USA</th>
#                     <th>UAE</th>
#                     <th>UAE/clinic</th>
#                     <th>UAE/USA</th>
#                     </tr>
#                 </thead>
#                 <tbody>
#                 {table_formate_clinic(master_data_dict)}
#                 </tbody>
#                 </table>
#             </body>
#             </html>
#     """

#     return html