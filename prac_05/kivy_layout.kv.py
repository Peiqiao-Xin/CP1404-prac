# This is a Kv file declaring the GUI layout.
BoxLayout:
    orientation: 'vertical'

    # Status label at top (20% of height)
    Label:
        text: app.status_text
        font_size: 60
        size_hint_y: 0.2

    # Buttons for increment/decrement
    BoxLayout:
        orientation: 'horizontal'
        Button:
            text: "Up"
            on_press: app.handle_press(1)
        Button:
            text: "Down"
            on_press: app.handle_press(-1)

    # Dynamically added name buttons appear here
    BoxLayout:
        id: names_box

    # New label added at bottom (10% of height)
    Label:
        text: "I did this :)"
        size_hint_y: 0.1
        font_size: 24
        halign: 'center'
        valign: 'middle'