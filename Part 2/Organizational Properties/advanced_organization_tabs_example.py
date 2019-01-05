html.Div(children=[
	dash_core_components.Tabs(
    	id="tabsID",
    	children=[
		dash_core_components.Tab(label='Time-wise Sales', 
					 children=[time_wise_layout ]),	
		dash_core_components.Tab(label='Region-wise Sales', 
					 children=[region_wise_layout]),
		dash_core_components.Tab(label='Category-wise Sales', 
					 children=[category_wise_layout]),
		],
    	value="Time-wise Sales" ## Specifies the tab to be displayed by default
	) 
])