html.Div(children=[
	dash_core_components.Graph(
    	id='example-graph',
    	figure={
        	'data': [ {'x': Xaxis,'y': Yaxis,'type': 'line','name': 'Sales'} ],
            'layout': go.Layout(
            	xaxis={"title":"Time"}, yaxis={"title":"Sales Qty"}, width=300,
            	shapes=[
                    {
                    	'type':'rect', 'xref':'x','yref':'paper',
                    	'x0':exp[0],'y0':0,'x1':exp[1],'y1':1,
                    	'fillcolor': colors[index%3],
                    	'opacity': 0.30,
                    	'line': {
                        	'width': 0,
                    	}  
	           } for index,exp in enumerate(Seasons)]
           ) 
        } 
    )
])