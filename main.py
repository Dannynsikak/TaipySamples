import taipy.gui.builder as tgb
from taipy.gui import Gui
import pandas as pd

# Sample data for visual componentss
data = pd.DataFrame({"x": [1, 2, 2], "y": [10, 20, 30]})
metric_value = 75
progress_value = 50
indicator_value = 70

show_dialog = False

def dialog_action(state, _, payload):
    if payload["args"][0] == 0:
        print("Good to hear!")
    elif payload ["args"][0] == 1:
        print("Sorry to hear that.")
    else:
        print("Ok bye.")
    state.show_dialog = False


# define the page 
with tgb.Page() as page:
    with tgb.dialog("{show_dialog}", title="Welcome!", on_action=dialog_action, labels="Couldn't be better;but it's my day"):
        tgb.html("h2", "Hello!")
        tgb.button("Show", on_action=lambda s: s.assign("show_dialog", True))
    # components will be added here soon
    # Chart: Displays a bar chart of data with customizable properties
    tgb.chart("{data}", x="x", y="y", type="bar", title="Bar Chart Example")

    # Table: Displays tabular data with sorting and filtering options
    tgb.table("{data}", filter=True, number_format="%.0f") # Use editable=True to allow user modifications
    # Metric: Highlights a specific numeric value with a title
    tgb.metric("{metric_value}", title="Completion", min=0, max=100) # Add delta=5 to show changes type="linear" for linear metric
    # Progress: Display progress with value and optional title
    tgb.progress("{progress_value}", title="Loading Progress", show_value=True) # Use linear=True fora linear bar
    # Indicator: shows a value on a red-to-green scale 
    tgb.indicator("{indicator_value}", min=0, max=100, display="Perf", width="50vw") # Use orientation="vertical" or "v" for a vertical layout 
    # Expandable: Creates a collapsible section to group content
    with tgb.expandable("Expandle Section"):
        tgb.text("This is an example section. Click to open or close.")
    # Part: Groups elements and can be conditionally displayed
    with tgb.part(render="{False}"):  # Use render="{False}" to hide this part
        tgb.text("This text is inside a part.")
        tgb.button("Click Me")
    # Layout: Arranges elements in a column-based layout, 2:1 ratio
    with tgb.layout(columns="2 1"):
        with tgb.part():
            tgb.text("Column 1")
        with tgb.part():
            tgb.text("Column 2")
            tgb.text("Some text here")
    # Combining layouts
    with tgb.layout(columns="1 2"):
        with tgb.part():
            tgb.text("Column 1: Nested Layout")
        with tgb.expandable("Column 2: Expandable"):
            tgb.text("This expandable is inside a column layout.")
    
    if __name__ == "__main__":
        Gui(page).run(debug=True,title="Dialog - Labels")




