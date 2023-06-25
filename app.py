import openai
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# OpenAI API credentials
openai.api_key = "API KEY OPENAI"

# Instantiate the Dash app
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, 'https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = dbc.Container([
    html.H1("CHAT IN DASH", style={'text-align': 'center', 'color': 'white'}),

    dbc.Row([
        dbc.Col([
            dcc.Input(id='input-text', type='text',
                      placeholder='Type your message here',
                      style={'width': '500px', 'color': 'white'}),
            html.Button('Submit', id='submit-button', n_clicks=0, style={'margin-top': '10px', 'color': 'white'}),

        ], width=6)
    ], justify="center"),

    dbc.Row([
        dbc.Col([
            dcc.Loading(
                id='loading-output',
                type='dot',
                color='#007BFF',
                fullscreen=False,
                className='loading-spinner',
                children=[html.Div(id='output-text', style={'text-align': 'center', 'color': 'white'})]
            )
        ])
    ], justify="center", align="center")
], className='main-container', style={'color': 'white'})

# Define the callback function
@app.callback(
    Output('output-text', 'children'),
    Input('submit-button', 'n_clicks'),
    State('input-text', 'value')
)
def update_output(n_clicks, text_input):
    if n_clicks > 0:
        # Get the response from ChatGPT-3.5 Turbo
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Chat: {text_input}\nAI:",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        # Extract the generated text from the response
        generated_text = response.choices[0].text.strip()

        # Return the generated text as the output
        return generated_text

if __name__ == '__main__':
    app.run_server(debug=True)
