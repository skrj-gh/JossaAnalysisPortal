from django.shortcuts import render
import pandas as pd

def predictor(request):
    if request.method == "POST":
        # Get the user inputs from the form
        Seat_Type = request.POST.get("Seat_Type")
        Rank = float(request.POST.get("Rank"))
        College = request.POST.get("College")

        # Load the cleaned data from the CSV file
        df = pd.read_csv('ORCR_16_22_all.csv')
        df = df[~(df['Opening_Rank'].str.endswith('P') | df['Closing_Rank'].str.endswith('P'))]

        if College != "All":
            df = df[~(df['Institute'] != College)]
        
        df['Opening_Rank'] = df['Opening_Rank'].astype(float)

        # Filter the data based on user inputs
        filtered_data = df[(df['Seat_Type'] == Seat_Type) & (df['Opening_Rank'] >= Rank ) & (df['Round'] == 6)]

        # Sort the filtered data by Opening Rank
        filtered_data = filtered_data.sort_values('Opening_Rank')

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

