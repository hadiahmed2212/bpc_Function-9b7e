
import os
import threading
import urllib.request
import urllib.parse
import tkinter as tk
from io import BytesIO
from pathlib import Path

import customtkinter as ctk
from PIL import Image, ImageTk
from openai import OpenAI
from dotenv import load_dotenv


# =========================
# CONFIGURATION
# =========================

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

GROQ_KEY = os.getenv("GROQ_API_KEY")
POLLINATIONS_KEY = os.getenv("POLLINATIONS_API_KEY")

if not GROQ_KEY:
    raise SystemExit(
        "GROQ_API_KEY is missing. Check your .env file."
    )

if not POLLINATIONS_KEY:
    print("WARNING: POLLINATIONS_API_KEY is missing. Image generation will not work.")

client = OpenAI(
    api_key=GROQ_KEY,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-120b"
IMAGE_MODEL = "flux"


INSTRUCTIONS = """
You are GOOFED AI, a helpful and intelligent AI assistant.

Your abilities:
- Answer general questions.
- Solve maths equations.
- Explain algebra and fractions.
- Help with Python programming.
- Debug and explain code.
- Explain science and technology.
- Help with creative projects.
- Help with homework and learning.

Instructions:
- Give clear, accurate and useful answers.
- Explain maths step by step.
- Write clean and properly formatted code.
- Be friendly and conversational.
- Remember the context of the conversation.
- If unsure about something, say so.
- Never pretend to have performed an action you cannot perform.
"""


# =========================
# MAIN APPLICATION
# =========================

class GoofedAI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("GOOFED AI")
        self.geometry("1100x750")
        self.minsize(750, 550)

        self.busy = False
        self.image_references = []

        self.conversation = [
            {
                "role": "system",
                "content": INSTRUCTIONS
            }
        ]

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_chat_area()

        self.add_message(
            "GOOFED AI",
            "Welcome to GOOFED AI! Ask me anything. 🚀"
        )

    # =========================
    # SIDEBAR
    # =========================

    def create_sidebar(self):

        sidebar = ctk.CTkFrame(
            self,
            width=230,
            corner_radius=0
        )

        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)

        ctk.CTkLabel(
            sidebar,
            text="GOOFED AI",
            font=("Arial", 28, "bold"),
            text_color="#168cff"
        ).pack(pady=(35, 5))

        ctk.CTkLabel(
            sidebar,
            text="YOUR PERSONAL AI",
            font=("Arial", 12)
        ).pack(pady=(0, 35))

        ctk.CTkButton(
            sidebar,
            text="+ New Chat",
            height=42,
            command=self.new_chat
        ).pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(
            sidebar,
            text="FEATURES",
            font=("Arial", 13, "bold"),
            text_color="gray"
        ).pack(anchor="w", padx=22, pady=(30, 10))

        features = [
            "💬 AI Chat",
            "🧮 Math Solver",
            "💻 Python Helper",
            "🧠 AI Reasoning",
            "🎨 Image Generation"
        ]

        for feature in features:

            ctk.CTkLabel(
                sidebar,
                text=feature,
                font=("Arial", 15),
                anchor="w"
            ).pack(fill="x", padx=25, pady=12)

        ctk.CTkLabel(
            sidebar,
            text="GOOFED AI v3.0",
            text_color="gray"
        ).pack(side="bottom", pady=20)

    # =========================
    # CHAT AREA
    # =========================

    def create_chat_area(self):

        main_area = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        main_area.grid(row=0, column=1, sticky="nsew")

        main_area.grid_columnconfigure(0, weight=1)
        main_area.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(
            main_area,
            fg_color="transparent"
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=25,
            pady=20
        )

        ctk.CTkLabel(
            header,
            text="Chat with Goofed AI",
            font=("Arial", 24, "bold")
        ).pack(side="left")

        self.status = ctk.CTkLabel(
            header,
            text="● Online",
            text_color="#35c978"
        )

        self.status.pack(side="right")

        self.chat_box = ctk.CTkTextbox(
            main_area,
            corner_radius=12,
            font=("Arial", 15),
            wrap="word"
        )

        self.chat_box.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=25,
            pady=10
        )

        self.chat_box.configure(state="disabled")

        bottom = ctk.CTkFrame(
            main_area,
            fg_color="transparent"
        )

        bottom.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=25,
            pady=20
        )

        bottom.grid_columnconfigure(0, weight=1)

        self.input_box = ctk.CTkEntry(
            bottom,
            height=50,
            font=("Arial", 15),
            placeholder_text="Ask Goofed AI anything..."
        )

        self.input_box.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 10)
        )

        self.input_box.bind(
            "<Return>",
            self.send_message
        )

        self.send_button = ctk.CTkButton(
            bottom,
            text="SEND",
            width=85,
            height=50,
            command=self.send_message
        )

        self.send_button.grid(
            row=0,
            column=1,
            padx=(0, 8)
        )

        self.image_button = ctk.CTkButton(
            bottom,
            text="🎨 IMAGE",
            width=105,
            height=50,
            fg_color="#7045c5",
            hover_color="#5835a0",
            command=self.generate_image
        )

        self.image_button.grid(
            row=0,
            column=2
        )

    # =========================
    # MESSAGE DISPLAY
    # =========================

    def add_message(self, sender, message):

        self.chat_box.configure(state="normal")

        self.chat_box.insert(
            "end",
            f"\n{sender}\n"
        )

        self.chat_box.insert(
            "end",
            message + "\n"
        )

        self.chat_box.insert(
            "end",
            "\n" + "-" * 45 + "\n"
        )

        self.chat_box.configure(state="disabled")
        self.chat_box.see("end")

    # =========================
    # IMAGE WINDOW
    # =========================

    def add_generated_image(self, image_data):

        try:

            image = Image.open(
                BytesIO(image_data)
            ).convert("RGB")

            image.thumbnail((700, 700))

            photo = ImageTk.PhotoImage(image)

            image_window = ctk.CTkToplevel(self)

            image_window.title(
                "GOOFED AI - Generated Image"
            )

            image_window.geometry("750x780")

            image_label = ctk.CTkLabel(
                image_window,
                text="",
                image=photo
            )

            image_label.pack(
                expand=True,
                padx=15,
                pady=15
            )

            # Keep image alive while window is open
            image_label.image = photo

        except Exception as error:

            self.add_message(
                "GOOFED AI",
                "Couldn't display image:\n" + str(error)
            )

    # =========================
    # BUSY STATUS
    # =========================

    def set_busy(self, busy, status_text=None):

        self.busy = busy

        self.send_button.configure(
            state="disabled" if busy else "normal",
            text="WAIT..." if busy else "SEND"
        )

        self.image_button.configure(
            state="disabled" if busy else "normal",
            text="WAIT..." if busy else "🎨 IMAGE"
        )

        if status_text:

            self.status.configure(
                text=status_text,
                text_color="#f0ad4e"
            )

        else:

            self.status.configure(
                text="● Online",
                text_color="#35c978"
            )

    # =========================
    # NORMAL AI CHAT
    # =========================

    def send_message(self, event=None):

        if self.busy:
            return

        message = self.input_box.get().strip()

        if not message:
            return

        self.input_box.delete(0, "end")

        self.add_message("YOU", message)

        self.conversation.append({
            "role": "user",
            "content": message
        })

        self.set_busy(
            True,
            "● Thinking..."
        )

        threading.Thread(
            target=self.get_ai_response,
            args=(self.conversation.copy(),),
            daemon=True
        ).start()

    def get_ai_response(self, messages):

        try:

            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                max_completion_tokens=2048
            )

            answer = response.choices[0].message.content

            if not answer:

                answer = (
                    "I couldn't generate a response. "
                    "Please try again."
                )

            self.after(
                0,
                self.finish_response,
                answer,
                True
            )

        except Exception as error:

            self.after(
                0,
                self.finish_response,
                "Something went wrong:\n" + str(error),
                False
            )

    def finish_response(self, answer, success):

        if success:

            self.conversation.append({
                "role": "assistant",
                "content": answer
            })

        else:

            if (
                len(self.conversation) > 1
                and self.conversation[-1]["role"] == "user"
            ):

                self.conversation.pop()

        self.add_message(
            "GOOFED AI",
            answer
        )

        self.set_busy(False)

        if not success:

            self.status.configure(
                text="● Error",
                text_color="#ff5555"
            )

    # =========================
    # IMAGE GENERATION
    # =========================

    def generate_image(self):

        if self.busy:
            return

        if not POLLINATIONS_KEY:

            self.add_message(
                "GOOFED AI",
                "Image generation needs a POLLINATIONS_API_KEY. "
                "Add it to your .env file."
            )

            return

        prompt = self.input_box.get().strip()

        if not prompt:

            self.add_message(
                "GOOFED AI",
                "Please type an image description first."
            )

            return

        self.input_box.delete(0, "end")

        self.add_message(
            "YOU - IMAGE PROMPT",
            prompt
        )

        self.add_message(
            "GOOFED AI",
            "🎨 Generating your image. Please wait..."
        )

        self.set_busy(
            True,
            "● Creating image..."
        )

        threading.Thread(
            target=self.image_worker,
            args=(prompt,),
            daemon=True
        ).start()

    def image_worker(self, prompt):

        try:

            encoded_prompt = urllib.parse.quote(
                prompt,
                safe=""
            )

            url = (
                "https://gen.pollinations.ai/image/"
                + encoded_prompt
                + "?model="
                + urllib.parse.quote(IMAGE_MODEL, safe="")
                + "&width=1024&height=1024&n=1"
            )

            request = urllib.request.Request(
                url,
                headers={
                    "Authorization": "Bearer " + POLLINATIONS_KEY,
                    "Accept": "image/*",
                    "User-Agent": "GoofedAI/3.0"
                }
            )

            with urllib.request.urlopen(
                request,
                timeout=300
            ) as response:

                image_data = response.read()

            if not image_data:

                raise RuntimeError(
                    "The image service returned an empty image."
                )

            output_folder = BASE_DIR / "generated_images"
            output_folder.mkdir(exist_ok=True)

            image = Image.open(
                BytesIO(image_data)
            ).convert("RGB")

            import time

            filename = output_folder / (
                "goofed_image_" + str(int(time.time() * 1000)) + ".png"
            )

            image.save(
                filename,
                format="PNG"
            )

            self.after(
                0,
                self.finish_image,
                image_data,
                str(filename)
            )

        except Exception as error:

            self.after(
                0,
                self.finish_image_error,
                str(error)
            )

    def finish_image(self, image_data, filename):

        self.add_message(
            "GOOFED AI",
            "✅ Image generated successfully!\n"
            "Saved to:\n" + filename
        )

        self.add_generated_image(image_data)

        self.set_busy(False)

    def finish_image_error(self, error):

        self.add_message(
            "GOOFED AI",
            "Image generation failed:\n" + error
        )

        self.set_busy(False)

        self.status.configure(
            text="● Image Error",
            text_color="#ff5555"
        )

    # =========================
    # NEW CHAT
    # =========================

    def new_chat(self):

        if self.busy:
            return

        self.conversation = [
            {
                "role": "system",
                "content": INSTRUCTIONS
            }
        ]

        self.image_references.clear()

        self.chat_box.configure(state="normal")

        self.chat_box.delete(
            "1.0",
            "end"
        )

        self.chat_box.configure(state="disabled")

        self.add_message(
            "GOOFED AI",
            "New chat started! What can I help you with?"
        )


# =========================
# START APPLICATION
# =========================

if __name__ == "__main__":

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = GoofedAI()
    app.mainloop()
