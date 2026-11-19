from pyscript import document

club_members = ["Ana Reyes", "Ben Santos", "Cara Cruz", "Anne Lacuesta"]

def verify_candidate(e):
    first_name = document.getElementById("first_name").value 
    last_name = document.getElementById("last_name").value

    full_name = first_name + " " + last_name
    is_member = full_name in club_members
    
    messages = {
        True: f"Congratulations " + full_name + "! You are now part of the Communication Arts club.",
        False: f"Sorry " + full_name + ", your name is not on the list."
    }
    
    document.getElementById("result").innerText = messages.get(is_member)