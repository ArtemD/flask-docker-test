from datetime import date

# Plugin structure

# Custom style if needed
css = """
<style>
.date {
    color:red;
}
</style>
"""

# Function action
def action():
    return date.today().strftime("%d/%m/%Y")