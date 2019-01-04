# app layout element
html.Div([
    	html.A(html.Button('Download Graph Data'), href='/dash/data_download')
	],style={"textAlign":"left","font-size":"20"})


# callback function
@app.server.route("/dash/data_download")
def download_data():
	return flask.send_file(directory + 'raw_graph_data.csv',
                    	mimetype='text/csv',
                    	attachment_filename='raw_graph_data.csv',
                    	as_attachment=True
    	)