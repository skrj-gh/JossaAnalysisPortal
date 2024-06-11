from django.shortcuts import render
import pandas as pd

def predictor(request):
    if request.method == "POST":
        # Get the user inputs from the form
        Seat_Type = request.POST.get("Seat_Type")
        Rank = float(request.POST.get("Rank"))
        College = request.POST.get("College")
        Gender = request.POST.get("Gender")

        # Load the cleaned data from the CSV file
        df = pd.read_csv('JOSSA_data.csv')
        df = df[~(df['Closing_Rank'].str.endswith('P') | df['Closing_Rank'].str.endswith('P'))]

        if College != "All":
            df = df[~(df['Institute'] != College)]
        
        df['Closing_Rank'] = df['Closing_Rank'].astype(float)

        # Filter the data based on user inputs
        if(Gender=='All'):
            filtered_data = df[(df['Seat_Type'] == Seat_Type) & (df['Institute'].str.startswith('Indian Institute of Technology')) & (df['Closing_Rank'] >= Rank ) & (df['Year'] == 2023) & (df['Round'] == 6)]
        else:
            filtered_data = df[(df['Seat_Type'] == Seat_Type) & (df['Gender'] == Gender) & (df['Institute'].str.startswith('Indian Institute of Technology')) & (df['Closing_Rank'] >= Rank ) & (df['Year'] == 2023) & (df['Round'] == 6)]

        # Sort the filtered data by Opening Rank
        filtered_data = filtered_data.sort_values('Closing_Rank')

        # Convert the filtered data to a list of dictionaries
        data_list = filtered_data.to_dict(orient='records')

        # Pass the filtered data to the template
        context = {
            'Seat_Type': Seat_Type,
            'Rank': Rank,
            'filtered_data': data_list,
            'title': 'JOSSA Predictor'
        }
        return render(request, 'predictor/predictor.html', context)

    return render(request, 'predictor/predictor.html')

