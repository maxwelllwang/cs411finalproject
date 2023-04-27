from dash import Dash, html


# https://github.com/ucg8j/awesome-dash
app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World')
])

if __name__ == '__main__':
    app.run_server(debug=True)

