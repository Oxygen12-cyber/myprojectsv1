from nicegui import ui

ui.add_head_html("""
<style>
html, body {
    height: 100%;
    width: 100%;
    margin: 0;
    padding: 0;
    min-height: 100vh;
    min-width: 100vw;
    box-sizing: border-box;
}
body {
    /* fallback background if you want */
    background: #dbeafe;
}
</style>
""")

with ui.element('div').classes("flex flex-col justify-center items-center bg-gradient-to-br from-blue-100 to-indigo-200 px-4 min-h-screen w-screen"):
    with ui.element('div').classes("bg-white p-8 rounded-2xl shadow-xl w-full max-w-sm"):
        ui.label('Log-In to your Account').classes("text-xl font-bold font-mono text-center text-indigo-600 mb-5")
        ui.label('📧Email')
        ui.input(placeholder='you@mail.com').classes("w-full px-2 py-0.5 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500").props("borderless")
        ui.label('🔑Password').classes('mt-4 mb-0')
        ui.input(password=True, placeholder='your password').classes("w-full px-2 py-0.5 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500").props("borderless")
        with ui.element('div').classes("mt-4 flex flex-row gap-2"):
            ui.button(text='SIGN IN').classes("font-sans font-bold flex-1 rounded-md p-1 shadow-sm bg-indigo-400 text-white hover:bg-indigo-500")
            ui.button(text='SIGN UP').classes("font-mono flex-1 rounded-md p-1 shadow-sm bg-white text-black ")


ui.run()