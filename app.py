import os, time
import gradio as gr
from subprocess import getoutput

def run_live(command):
  with os.popen(command) as pipe:
    for line in pipe:
      line = line.rstrip()
      print(line)
      yield line

def run_static(command):
    out = getoutput(f"{command}")
    print(out)
    return out

def timeout_test(second):
    start_time = time.time()
    while time.time() - start_time < int(second):
        pass
    msg = "🥳"
    return msg

def clear_out_text():
    return ""
   
with gr.Blocks() as terminal:
    with gr.Tab("💻 Terminal"):
        with gr.Box():
            terminal_command = gr.Textbox(show_label=False, lines=1, placeholder="command")
            terminal_out_text = gr.Textbox(show_label=False)
            btn_terminl_run_static = gr.Button("run static command")
            btn_terminl_run_static.click(run_static, inputs=terminal_command, outputs=terminal_out_text, show_progress=False)
            btn_terminl_run_live = gr.Button("run live command")
            btn_terminl_run_live.click(run_live, inputs=terminal_command, outputs=terminal_out_text, show_progress=False) 
    with gr.Tab("Tests"):
        with gr.Box():
            test_command = gr.Textbox(show_label=False, lines=1, placeholder="command")
            test_out_text = gr.Textbox(show_label=False)
            btn_timeout_test = gr.Button("timeout test")
            btn_timeout_test.click(timeout_test, inputs=test_command, outputs=test_out_text, show_progress=False)
            btn_clear = gr.Button("clear")
            btn_clear.click(clear_out_text, inputs=[], outputs=test_out_text, show_progress=False)

terminal.queue(api_open=False).launch()
