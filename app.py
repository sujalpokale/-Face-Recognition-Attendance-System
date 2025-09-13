from register import register_user
from attendance import mark_attendance
import threading
import gradio as gr

def run_register():
    threading.Thread(target=register_user).start()
    return "Registration process started. Please check the camera window."
def run_attendance():
    threading.Thread(target=mark_attendance).start()
    return "Attendance marking process started. Please check the camera window."

with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center; color: #4CAF50;'> Face Recognition Attendance System")
    with gr.Row():
        with gr.Column():
             register_btn = gr.Button("Register User", elem_id="register_btn")
             register_output = gr.Textbox(label="Status", interactive=False)
             attendance_btn = gr.Button("Mark Attendance", elem_id="attendance_btn")
             attendance_output = gr.Textbox(label="Status", interactive=False)
    
    register_btn.click(fn=run_register, inputs=[], outputs=register_output)
    attendance_btn.click(fn=run_attendance, inputs=[], outputs=attendance_output)
    
    gr.Markdown("<h3 style='text-align: center; color: #888;'> Developed by Your Name")
    
demo.launch(share=True)