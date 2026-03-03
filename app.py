import dash
from dash import dcc, html, dash_table, Input, Output
import plotly.express as px
import pandas as pd
from data import JOBS

# Load data
df = pd.DataFrame(JOBS)
df['date'] = pd.to_datetime(df['date'])
df['salary_display'] = df['salary'].apply(lambda x: f"${x:,}")
df['date_display'] = df['date'].dt.strftime('%b %d, %Y')

# KPI numbers
total      = len(df)
active     = len(df[df['status'].isin(['Applied', 'Screening'])])
interviews = len(df[df['status'] == 'Interview'])
offers     = len(df[df['status'] == 'Offer'])
rejections = len(df[df['status'] == 'Rejected'])
offer_rate = round((offers / total) * 100, 1)
avg_salary = int(df[df['status'] == 'Offer']['salary'].mean())

# Colors
STATUS_COLORS = {
    'Applied':   '#4a90d9',
    'Screening': '#f4a261',
    'Interview': '#2ec4b6',
    'Offer':     '#3cb371',
    'Rejected':  '#e05454',
}
BG   = '#0f1c2e'
CARD = '#162236'
BORDER = '#2a3f5c'
TEXT = '#dce6f0'
MUTED = '#8da4be'
GOLD = '#c9a84c'

# ── CHART 1: Status Donut ──────────────────────────────────
status_counts = df['status'].value_counts().reset_index()
status_counts.columns = ['status', 'count']
donut_fig = px.pie(
    status_counts, names='status', values='count',
    hole=0.65, color='status',
    color_discrete_map=STATUS_COLORS, title='Status Breakdown'
)
donut_fig.update_layout(
    paper_bgcolor=CARD, plot_bgcolor=CARD, font_color=TEXT,
    title_font_color=GOLD, title_font_size=13,
    legend=dict(font=dict(color=MUTED, size=11)),
    margin=dict(t=40, b=10, l=10, r=10), height=280
)

# ── CHART 2: Industry Bar ──────────────────────────────────
industry_counts = df['industry'].value_counts().reset_index()
industry_counts.columns = ['industry', 'count']
industry_fig = px.bar(
    industry_counts, x='count', y='industry',
    orientation='h', title='By Industry',
    color='count', color_continuous_scale=[[0,'#1d2e47'],[1, GOLD]]
)
industry_fig.update_layout(
    paper_bgcolor=CARD, plot_bgcolor=CARD, font_color=TEXT,
    title_font_color=GOLD, title_font_size=13,
    xaxis=dict(gridcolor=BORDER, color=MUTED, title=''),
    yaxis=dict(gridcolor=BORDER, color=TEXT, title=''),
    coloraxis_showscale=False,
    margin=dict(t=40, b=10, l=10, r=10), height=280
)

# ── CHART 3: Weekly Line ───────────────────────────────────
df_sorted = df.sort_values('date')
df_sorted['week'] = df_sorted['date'].dt.isocalendar().week
weekly = df_sorted.groupby('week').size().reset_index(name='applications')
weekly_fig = px.line(
    weekly, x='week', y='applications',
    title='Applications per Week', markers=True
)
weekly_fig.update_traces(
    line_color=GOLD, marker=dict(color=GOLD, size=8),
    fill='tozeroy', fillcolor='rgba(201,168,76,0.08)'
)
weekly_fig.update_layout(
    paper_bgcolor=CARD, plot_bgcolor=CARD, font_color=TEXT,
    title_font_color=GOLD, title_font_size=13,
    xaxis=dict(gridcolor=BORDER, color=MUTED, title='Week #'),
    yaxis=dict(gridcolor=BORDER, color=MUTED, title='Count'),
    margin=dict(t=40, b=10, l=10, r=10), height=280
)

# ── CHART 4: Salary Box ────────────────────────────────────
salary_fig = px.box(
    df[df['status'] != 'Rejected'],
    x='status', y='salary', color='status',
    color_discrete_map=STATUS_COLORS, title='Salary by Stage'
)
salary_fig.update_layout(
    paper_bgcolor=CARD, plot_bgcolor=CARD, font_color=TEXT,
    title_font_color=GOLD, title_font_size=13,
    xaxis=dict(gridcolor=BORDER, color=TEXT, title=''),
    yaxis=dict(gridcolor=BORDER, color=MUTED,
               tickformat='$,.0f', title='Salary'),
    showlegend=False,
    margin=dict(t=40, b=10, l=10, r=10), height=280
)

# ── HELPERS ────────────────────────────────────────────────
def kpi_card(emoji, number, label, color):
    return html.Div([
        html.Div(emoji, style={'fontSize':'26px','marginBottom':'8px'}),
        html.Div(str(number), style={'fontSize':'36px','fontWeight':'700','color':'white','lineHeight':'1'}),
        html.Div(label, style={'fontSize':'11px','color':MUTED,'textTransform':'uppercase','letterSpacing':'1px','marginTop':'6px'}),
    ], style={
        'background':CARD,'border':f'1px solid {BORDER}',
        'borderBottom':f'3px solid {color}','borderRadius':'10px',
        'padding':'20px','textAlign':'center','flex':'1'
    })

def panel(title, tag, children):
    return html.Div([
        html.Div([
            html.Span(title, style={'fontSize':'11px','fontWeight':'600','color':MUTED,'textTransform':'uppercase','letterSpacing':'1px'}),
            html.Span(tag,   style={'fontSize':'10px','background':'rgba(201,168,76,0.15)','color':GOLD,'padding':'3px 9px','borderRadius':'4px'}),
        ], style={'display':'flex','justifyContent':'space-between','alignItems':'center','padding':'12px 18px','borderBottom':f'1px solid {BORDER}'}),
        html.Div(children, style={'padding':'16px 18px'})
    ], style={'background':CARD,'border':f'1px solid {BORDER}','borderRadius':'10px','overflow':'hidden','flex':'1'})

# ── APP LAYOUT ─────────────────────────────────────────────
app = dash.Dash(__name__)

app.layout = html.Div([

    # Top bar
    html.Div([
        html.Div([
            html.Span('JT', style={'background':GOLD,'color':BG,'borderRadius':'8px','padding':'5px 10px','fontWeight':'700','fontSize':'15px','marginRight':'12px'}),
            html.Span('JobTrack Pro', style={'fontSize':'18px','fontWeight':'700','color':'white'}),
            html.Span(' · Career Dashboard', style={'fontSize':'13px','color':MUTED,'marginLeft':'6px'}),
        ], style={'display':'flex','alignItems':'center'}),
        html.Div('● Active Search', style={'background':'rgba(60,179,113,0.15)','border':'1px solid rgba(60,179,113,0.3)','color':'#3cb371','padding':'6px 14px','borderRadius':'20px','fontSize':'12px','fontWeight':'600'}),
    ], style={'background':CARD,'borderBottom':f'1px solid {BORDER}','padding':'14px 32px','display':'flex','justifyContent':'space-between','alignItems':'center','marginBottom':'28px'}),

    # Main content
    html.Div([

        html.H1('My Job Search Command Center', style={'color':'white','fontSize':'26px','fontWeight':'700','marginBottom':'4px'}),
        html.P('Track every application, interview, and offer.', style={'color':MUTED,'marginBottom':'24px','fontSize':'14px'}),

        # KPI cards
        html.Div([
            kpi_card('📋', total,      'Total Applied',    '#4a90d9'),
            kpi_card('⚡', active,     'Active / Pending', GOLD),
            kpi_card('🎤', interviews, 'Interviews',       '#2ec4b6'),
            kpi_card('🏆', offers,     'Offers',           '#3cb371'),
            kpi_card('📭', rejections, 'Rejections',       '#e05454'),
        ], style={'display':'flex','gap':'14px','marginBottom':'16px'}),

        # Highlight bar
        html.Div([
            html.Span('🎯  Offer Rate: ', style={'color':MUTED}),
            html.Span(f'{offer_rate}%', style={'color':GOLD,'fontWeight':'700','fontSize':'15px'}),
            html.Span('     |     Avg Offer Salary: ', style={'color':MUTED,'marginLeft':'24px'}),
            html.Span(f'${avg_salary:,}', style={'color':'#3cb371','fontWeight':'700','fontSize':'15px'}),
        ], style={'background':CARD,'border':f'1px solid {BORDER}','borderRadius':'8px','padding':'13px 20px','marginBottom':'20px','fontSize':'14px'}),

        # Charts row 1
        html.Div([
            panel('Status Breakdown', 'Donut', dcc.Graph(figure=donut_fig,    config={'displayModeBar':False})),
            panel('By Industry',      'Bar',   dcc.Graph(figure=industry_fig, config={'displayModeBar':False})),
            panel('Weekly Trend',     'Line',  dcc.Graph(figure=weekly_fig,   config={'displayModeBar':False})),
        ], style={'display':'flex','gap':'16px','marginBottom':'16px'}),

        # Charts row 2
        html.Div([
            panel('Salary Range by Stage', 'Box Plot', dcc.Graph(figure=salary_fig, config={'displayModeBar':False})),
        ], style={'display':'flex','gap':'16px','marginBottom':'20px'}),

        # Filter dropdown
        html.Div([
            html.Span('Filter by Status: ', style={'color':MUTED,'fontSize':'13px','marginRight':'10px'}),
            dcc.Dropdown(
                id='status-filter',
                options=[{'label':'All Applications','value':'All'}] +
                        [{'label':s,'value':s} for s in ['Applied','Screening','Interview','Offer','Rejected']],
                value='All', clearable=False,
                style={'width':'220px','color':BG}
            ),
        ], style={'display':'flex','alignItems':'center','marginBottom':'12px'}),

        # Table
        html.Div([
            dash_table.DataTable(
                id='jobs-table',
                columns=[
                    {'name':'Company',  'id':'company'},
                    {'name':'Role',     'id':'role'},
                    {'name':'Industry', 'id':'industry'},
                    {'name':'Status',   'id':'status'},
                    {'name':'Salary',   'id':'salary_display'},
                    {'name':'Type',     'id':'type'},
                    {'name':'Applied',  'id':'date_display'},
                ],
                data=df.to_dict('records'),
                style_table={'overflowX':'auto','borderRadius':'8px'},
                style_cell={'backgroundColor':CARD,'color':TEXT,'border':f'1px solid {BORDER}','padding':'11px 14px','fontSize':'13px','fontFamily':'Arial','textAlign':'left'},
                style_header={'backgroundColor':BG,'color':MUTED,'fontWeight':'600','fontSize':'11px','textTransform':'uppercase','letterSpacing':'1px','border':f'1px solid {BORDER}'},
                style_data_conditional=[
                    {'if':{'filter_query':'{status} = "Offer"'},     'color':'#3cb371','fontWeight':'600'},
                    {'if':{'filter_query':'{status} = "Interview"'}, 'color':'#2ec4b6'},
                    {'if':{'filter_query':'{status} = "Rejected"'},  'color':'#e05454','opacity':'0.7'},
                    {'if':{'filter_query':'{status} = "Screening"'}, 'color':'#f4a261'},
                    {'if':{'filter_query':'{status} = "Applied"'},   'color':'#4a90d9'},
                    {'if':{'row_index':'odd'},                        'backgroundColor':'#1a2840'},
                ],
                page_size=8,
                sort_action='native',
            )
        ], style={'background':CARD,'border':f'1px solid {BORDER}','borderRadius':'10px','padding':'20px','marginBottom':'32px'}),

    ], style={'maxWidth':'1400px','margin':'0 auto','padding':'0 32px'}),

], style={'background':BG,'minHeight':'100vh','fontFamily':'Arial, sans-serif','color':TEXT})


# ── CALLBACK ───────────────────────────────────────────────
@app.callback(
    Output('jobs-table', 'data'),
    Input('status-filter', 'value')
)
def update_table(selected_status):
    if selected_status == 'All':
        return df.to_dict('records')
    return df[df['status'] == selected_status].to_dict('records')


# ── RUN ────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)