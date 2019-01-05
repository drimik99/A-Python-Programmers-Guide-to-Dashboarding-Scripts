html.Div([
        	html.Label("Country :"),
        	dash_core_components.Dropdown(
            	id="country",
            	options=[{"label":c, "value":c} for c in sorted(['USA','Canada'])],
            	placeholder = "Select Country...",
            	value = 'Select'
        	),
    	], style={"display":"inline-block", "textAlign":"center", "width":"12%"}),

    	html.Div([
        	html.Label("State :"),
        	dash_core_components.Dropdown(
            	id="state",
            	options=[{"label":s, "value":s} for s in region_data['State'].values],
            	placeholder = "Select State..."
        	),
    	], style={"display":"inline-block", "textAlign":"center", "width":"12%"}),

@app.callback(
	dash.dependencies.Output(component_id='state', component_property='options'),
	[dash.dependencies.Input(component_id='country', component_property='value')]
)
def update_state_values(country_input):
	St = region_data[region_data['Country']==country_input]['State'].values
	return [{'label':i,'value':i} for i in St]