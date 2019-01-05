@app.callback(Output('content-field-in-app-layout', 'children'),
[Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/Performance":
   	 return Perform_layout
    elif pathname == "/Marketing":
   	 return Marketing_layout
    elif pathname == "/Finance":
   	 return Finance_layout
    else:
   	 return Error_display_layout