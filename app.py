import streamlit as st
import google.generativeai as genai

import os
from dotenv import load_dotenv

load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini AI
genai.configure(api_key=api_key)
# Streamlit UI
st.title("🚀 LinkedIn Post Writer Agent with AI")
st.write("Generate a professional LinkedIn post based on your topic!")

# User Input
topic = st.text_input("Enter your topic", placeholder="Example: AI in Healthcare")

if st.button("Generate Post"):
    if topic:
        model = genai.GenerativeModel("gemini-1.5-pro")
        
        # Structured prompt for better LinkedIn posts
        prompt = f"""
I want you to act as a **🔥 𝗟𝗶𝗻𝗸𝗲𝗱𝗜𝗻 𝗣𝗼𝘀𝘁 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿 🔥** that creates engaging and professional posts on various topics. Your task is to:  

- 🅰️ **𝗕𝗜𝗚 𝗜𝗻𝘁𝗿𝗼𝗱𝘂𝗰𝘁𝗶𝗼𝗻:** Start with a **bold and eye-catching headline** with emojis.  
- 🅱️ **𝗕𝗜𝗚 𝗞𝗲𝘆 𝗣𝗼𝗶𝗻𝘁𝘀:** Highlight 2-4 key points with emojis, making them **clear, bold, and easy to read**.  
- 🅾️ **𝗕𝗜𝗚 𝗖𝗼𝗻𝗰𝗹𝘂𝘀𝗶𝗼𝗻:** End with a **bold call to action** or a question to boost engagement.  
- 🅿️ **𝗕𝗜𝗚 𝗛𝗮𝘀𝗵𝘁𝗮𝗴𝘀:** Include 5-8 **relevant and trending hashtags** for maximum reach.  



### 🏆 **𝗧𝗲𝗺𝗽𝗹𝗮𝘁𝗲 𝗘𝘅𝗮𝗺𝗽𝗹𝗲:**  
🚀 **🌟 𝗨𝗻𝗹𝗼𝗰𝗸𝗶𝗻𝗴 𝘁𝗵𝗲 𝗣𝗼𝘄𝗲𝗿 𝗼𝗳 {topic}! 🌟** 🤖  
In today's world, **{topic}** is transforming industries with its **unmatched potential and creativity**! From generating realistic images 🖼️ to crafting human-like text ✍️, it's **revolutionizing how we innovate**.  



### 💡 **🌟 𝗪𝗵𝘆 {topic} 𝗠𝗮𝘁𝘁𝗲𝗿𝘀 🌟:**  
1️⃣ **🚀 Creative Content Generation:** Automates writing, design, and video editing with ease.  

2️⃣ **🎯 Personalized Experiences:** Enhances user engagement in marketing and e-commerce.  

3️⃣ **⚡ Efficient Prototyping:** Speeds up design processes in manufacturing and architecture. 
.
.
.
 



🔥 **🌟 Embracing {topic} can be a game-changer for businesses and creators alike! 🌟**  
The future isn’t just automated; it’s **boldly creative!** 


🌟 **❓ 𝗛𝗼𝘄 𝗱𝗼 𝘆𝗼𝘂 𝘀𝗲𝗲 {topic} 𝘀𝗵𝗮𝗽𝗶𝗻𝗴 𝘁𝗵𝗲 𝗳𝘂𝘁𝘂𝗿𝗲? ❓**  
**💬 Share your thoughts below! 💬**  


### 🏷️ **#GenerativeAI #ArtificialIntelligence #Innovation #AIRevolution #TechTrends #MachineLearning #FutureOfAI #AIinBusiness #DigitalTransformation**  


### 🚀 **𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗮 𝗟𝗶𝗻𝗸𝗲𝗱𝗜𝗻 𝗽𝗼𝘀𝘁 𝗼𝗻 𝘁𝗵𝗲 𝘁𝗼𝗽𝗶𝗰: {topic}.**  
"""


        response = model.generate_content(prompt)
        
        if response.text:
            st.subheader("Generated LinkedIn Post:")
            st.write(response.text)

            # Add Copy-to-Clipboard Button
        
        else:
            st.error("Failed to generate content. Try again!")
    else:
        st.warning("Please enter a topic to generate a post.")




        
