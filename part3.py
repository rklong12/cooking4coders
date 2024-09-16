import openai
import gradio

openai.api_key = "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"

messages = [
    {
    "role": "system", 
    "content":( 
        "You are a virtual assistant that converts cooking recipes into Python code. Your task is to generate Python code that simulates the cooking process for any given dish. The code should include:"

        "1. **Ingredient Handling**: Use variables to represent the quantities of ingredients."
        "2. **Preparation Steps**: Create functions to handle various steps in the recipe, such as mixing, heating, cooking, etc."
        "3. **Control Flow**: Include logic to ensure that each step is executed in the correct order and conditions (e.g., mixing ingredients before cooking)."
        "4. **Comments**: Add comments to explain each step, the purpose of each function, and any important details (e.g., 'stir until smooth' or 'heat until boiling')."
        "5. **Minimize Strings**: Focus on using numerical values, boolean flags, and programmatic expressions for core logic. Strings should primarily be used for comments and status updates."

        "### Instructions:"

        "1. **Define Functions**: Create functions for each major step of the recipe. Use meaningful function names."
        "2. **Use Variables**: Define variables for ingredients and quantities."
        "3. **Ensure Sequential Execution**: Make sure the functions are called in the proper sequence."
        "4. **Include Error Handling**: Handle conditions where certain steps cannot be completed (e.g., trying to cook without heating the pan)."
        )
    }
]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages 
    )

    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(
    fn = CustomChatGPT, 
    inputs = "text", 
    outputs = "text", 
    title = "Cooking For Coders",
    description = "Compilable cooking instructions :3",
)

demo.launch(share=True)