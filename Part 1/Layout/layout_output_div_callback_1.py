@app.callback(
    dash.dependencies.Output(component_id='example-graph', component_property='figure'),
    [dash.dependencies.Input(component_id='date-picker-range', component_property='start_date'),
    dash.dependencies.Input(component_id='date-picker-range', component_property='end_date')]
)

def update_output_div(start_date,end_date):
    return {
    'data': [go.Scatter(
                x=data[(data['date']>=start_date)&(data['date']<=end_date)]['date'],
                y=data[(data['date']>=start_date)&(data['date']<=end_date)]['Sales'])]
            ,
    "layout": go.Layout(
               xaxis={"title":"Time"}, yaxis={"title":"Sales"}
             )
        }