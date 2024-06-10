from django.shortcuts import render
import pandas as pd
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def home(request):
    return render(request, 'analytics/home.html', {'title': 'JOSSA Analysis Portal'})

def analytics(request):
    return render(request, 'analytics/charts.html', {'title': 'JOSSA Analytics'})

def about(request):
    return render(request, 'analytics/about.html', {'title': 'About Us'})














def get_graph_as_base64(fig):
    buffer = io.BytesIO()
    FigureCanvas(fig).print_png(buffer)
    buffer.seek(0)
    plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    return plot_base64





def analytics(request):
    df = pd.read_csv('ORCR_16_22_all.csv')
    df = df[~(df['Opening_Rank'].str.endswith('P') | df['Closing_Rank'].str.endswith('P'))]

    filtered_data_1 = df[(df['Round'] == 6) & (df['Academic'] == 'Computer Science and Engineering (4 Years, Bachelor of Technology)') & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 2500) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]
    filtered_data_1['Closing_Rank'] = pd.to_numeric(filtered_data_1['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_1 = filtered_data_1.sort_values('Closing_Rank')
    if filtered_data_1.empty:
        error_message = 'No data available for the selected conditions.'
        context = {'error_message': error_message}
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_1['Closing_Rank'], filtered_data_1['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in CSE')
        graph1 = get_graph_as_base64(fig)
        context = {'graph1': graph1}

    filtered_data_2 = df[(df['Round'] == 6) & (df['Gender'] == 'Gender-Neutral') & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022) & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 8000)
                         & (df['Academic']=='Civil Engineering (4 Years, Bachelor of Technology)')]
    
    filtered_data_2['Closing_Rank'] = pd.to_numeric(filtered_data_2['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_2 = filtered_data_2.sort_values('Closing_Rank')

    if filtered_data_2.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_2['Closing_Rank'], filtered_data_2['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Institutes with closing rank less than 8000')
        graph2 = get_graph_as_base64(fig)
        context.update({'graph2': graph2})

    filtered_data_3 = df[(df['Round'] == 6) & (df['Gender'] == 'Gender-Neutral') & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022) & (pd.to_numeric(df['Closing_Rank'], errors='coerce') >= 8000)
                         & (df['Academic']=='Civil Engineering (4 Years, Bachelor of Technology)')]
    
    filtered_data_3['Closing_Rank'] = pd.to_numeric(filtered_data_3['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_3 = filtered_data_3.sort_values('Closing_Rank')

    if filtered_data_3.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_3['Closing_Rank'], filtered_data_3['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Institutes with closing rank greater than 8000')
        graph3 = get_graph_as_base64(fig)
        context.update({'graph3': graph3})

    filtered_data_4 = df[(df['Round'] == 6) & ((df['Academic'] == 'Mathematics and Computing (4 Years, Bachelor of Technology)') | (df['Academic'] == 'Mathematics and Computing (4 Years, Bachelor of Science)')) & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 7000) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]
    filtered_data_4['Closing_Rank'] = pd.to_numeric(filtered_data_4['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_4 = filtered_data_4.sort_values('Closing_Rank')

    if filtered_data_4.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_4['Closing_Rank'], filtered_data_4['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in MNC')
        graph4 = get_graph_as_base64(fig)
        context.update({'graph4': graph4})

    filtered_data_5 = df[(df['Round'] == 6) & (df['Academic'] == 'Electrical Engineering (4 Years, Bachelor of Technology)') & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 9000) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]

    filtered_data_5['Closing_Rank'] = pd.to_numeric(filtered_data_5['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_5 = filtered_data_5.sort_values('Closing_Rank')
    if filtered_data_5.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_5['Closing_Rank'], filtered_data_5['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in EE')
        graph5 = get_graph_as_base64(fig)
        context.update({'graph5': graph5})

    filtered_data_6 = df[(df['Round'] == 6) & (df['Academic'] == 'Mechanical Engineering (4 Years, Bachelor of Technology)') & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 9000) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]

    filtered_data_6['Closing_Rank'] = pd.to_numeric(filtered_data_6['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_6 = filtered_data_6.sort_values('Closing_Rank')
    if filtered_data_6.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_6['Closing_Rank'], filtered_data_6['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in Mech')
        graph6 = get_graph_as_base64(fig)
        context.update({'graph6': graph6})

    filtered_data_7 = df[(df['Round'] == 6) & (df['Academic'] == 'Chemical Engineering (4 Years, Bachelor of Technology)') & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 9000) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]

    filtered_data_7['Closing_Rank'] = pd.to_numeric(filtered_data_7['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_7 = filtered_data_7.sort_values('Closing_Rank')
    if filtered_data_7.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_7['Closing_Rank'], filtered_data_7['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in Chemical')
        graph7 = get_graph_as_base64(fig)
        context.update({'graph7': graph7})

    filtered_data_8 = df[(df['Round'] == 6) & (df['Academic'] == 'Civil Engineering (4 Years, Bachelor of Technology)') & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 9000) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]

    filtered_data_8['Closing_Rank'] = pd.to_numeric(filtered_data_8['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_8 = filtered_data_8.sort_values('Closing_Rank')
    if filtered_data_8.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_8['Closing_Rank'], filtered_data_8['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in Civil')
        graph8 = get_graph_as_base64(fig)
        context.update({'graph8': graph8})

    return render(request, 'analytics/charts.html', context)
