html.Div([
    dash_core_components.Location(id="url"),
    html.Div([
        dash_core_components.Link('Performance', href="/Performance", style=tab_style),
        dash_core_components.Link('Marketing', href="/Marketing", style=tab_style),
        dash_core_components.Link('Finance', href="/Finance", style=tab_style)
    ]),
    html.Div(id='content-field-in-app-layout')
])