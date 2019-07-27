import dash
import dash_core_components as dcc
import dash_html_components as html

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': '//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'id':'bootstrap-css'
    },
    {
         'href': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm',
        'crossorigin': 'anonymous'
    }
    
]
# external JavaScript files
external_scripts = [
    
    {'src': '//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js'},
    {'src': '//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js'}
    
]

app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)
app = dash.Dash(meta_tags=[
    # A description of the app, used by e.g.
    # search engines when displaying search results.
    {
        'name': 'description',
        'content': 'My description'
    },
    # A tag that tells Internet Explorer (IE)
    # to use the latest renderer version available
    # to that browser (e.g. Edge)
    {
        'http-equiv': 'X-UA-Compatible',
        'content': 'IE=edge'
    },
    # A tag that tells the browser not to scale
    # desktop widths to fit mobile screens.
    # Sets the width of the viewport (browser)
    # to the width of the device, and the zoom level
    # (initial scale) to 1.
    #
    # Necessary for "true" mobile support.
    {
      'name': 'viewport',
      'content': 'width=device-width, initial-scale=1.0'
    },
    {
        'charset':'utf-8'
    }
])
             

app.layout = html.Div(children=[
    # html.Div(
    #     className="app-header",
    #     children=[
    #         html.Div('Plotly Dash', className="app-header--title")
    #     ]
    # ),
    # html.Div(
    #     children=html.Div([
    #         html.H5('Overview'),
    #         html.Div('''
    #             This is an example of a simple Dash app with
    #             local, customized CSS.
    #         ''')
    #     ])
    # ),
    html.Div(
        className="page-wrapper chiller-theme toggled",
        children=[
                 html.A(
                    html.I(
                        className="fas fa-bars"
                        ),
                    id="show-sidebar",
                    className="btn btn-sm btn-dark",
                    href="#")
                ],
        Children=[
                html.Nav(
                    html.Div(
                        className="sidebar-content",
                        Children=[
                            html.Div(
                                html.A("pro sidebar",href="#"),
                                className="sidebar-brand"
                            ),
                        ],
                    ),
                    id="sidebar" ,
                    className="sidebar-wrapper"),
        ],
        
    ),
    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)