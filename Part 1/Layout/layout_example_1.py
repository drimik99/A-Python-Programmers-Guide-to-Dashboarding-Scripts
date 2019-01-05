html.Div(children=[   
	html.Div([
    	dash_core_components.Graph(
        	id='example-graph',
        	figure={
            	'data': [ {'x': data['date'],'y': data['Sales'],'type': 'line'} ],
            	'layout': go.Layout(
                        	xaxis={"title":"Time"}, yaxis={"title":"Sales"}) } )
    		], style={"display":"inline-block", "width":"35%"})
	])