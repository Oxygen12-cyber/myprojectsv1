from nicegui import ui


with ui.column():
    ui.button('sign in')
    ui.button('Login in')

with ui.row():
    with ui.card().style('width: 300px; height: 150px'):
        ui.label('Temperature')
        ui.slider(min=0, max=100, value=20)

    with ui.card().style('width: 500px; height: 400px'):
        ui.label('line Chart')
        ui.echart({
            'title': {'text': 'Sample Line Chart', 'left': 'center', 'textStyle': {'fontSize': 18}},
            'xAxis': {
                'type': 'category',
                'data': ['Category A', 'Category B', 'Category C'],
                'axisLabel': {'rotate': 0}  # Ensures the labels are not rotated
            },
            'yAxis': {'type': 'value'},
            'series': [{
                'name': 'Values',
                'data': [1, 2, 3],
                'type': 'line',
                'smooth': True,  # Makes the line smoother
                'label': {'show': True}  # Shows data points on the chart
            }]
        })

ui.run(native=True)
