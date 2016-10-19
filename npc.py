def converse(npc):
    print("You approach %s." % npc["name"])
    do_response(npc["response"])
    
def do_response(response):
    print(response["speech"])
    if "function" in response:
        resp = response["function"]()
        if resp:
            do_response(response["responses"][resp])
            return
    if "responses" in response:
        user_resp = "";
        while True:
            print("\n".join([" - " + r for r in response["responses"].keys()]))
            user_resp = input("> ")
            if user_resp in response["responses"]:
                do_response(response["responses"][user_resp])
                return
            print("Could you repeat that? (Note: This part is case-sensitive because I'm lazy)")
        

npc_test_ghost = {
    "name": "Blinky",
    "response": {
        "speech": "Hello, I'm a ghost!",
        "responses": {
            "hello": {
                "speech": "Nice to meet you! What's your favourite colour?",
                "responses": {
                    "red": {
                        "speech": "That's a nice colour!"
                    },
                    
                    "blue": {
                        "speech": "You have poor taste."
                    }
                }
            },
            "eeeww": {
                "speech": """How dare you insult me, puny human!

*The ghost slays you with a single touch*""",
                "function": exit
            }
        }
    }
}
