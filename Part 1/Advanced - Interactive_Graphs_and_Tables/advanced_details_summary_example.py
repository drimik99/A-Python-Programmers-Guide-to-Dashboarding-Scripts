html.Details([
	html.Summary('Display sales quantity',style={"font-size":"22"}),
	html.Div([
    	dash_core_components.Graph(
        	id='example-graph1',
        	figure={
            	'data': [ {'x': Xaxis,'y': Yaxis,'type': 'line'} ],
            	'layout': go.Layout(
                	xaxis={"title":"Time"}, yaxis={"title":"Sales Qty"}) } )
        	], style={"display":"inline-block", "width":"33%", "font-size":"12"})
   ]),

html.Div([
	dash_core_components.Graph(
    	id='example-graph2',
    	figure={
        	'data': [ {'x': Xaxis,'y': Yaxis_revenue,'type': 'bar'} ],
        	'layout': go.Layout(
            	xaxis={"title":"Time"}, yaxis={"title":"Sales Revenue"}, width=150) } )
	], style={"display":"inline-block", "width":"33%", "font-size":"12"})
