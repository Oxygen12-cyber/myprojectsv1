from nicegui import ui

with ui.row():
    ui.label('Profile')
    with ui.card().classes('w-full shadow-md m-12'):
        ui.label('First Name').classes('text-blue-200')
        ui.label('LastName').classes('text-green-400')
        ui.label('Address').classes('text-red-50')
        ui.label('Location').classes('text-yellow-200')

ui.run()