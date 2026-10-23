import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from fpdf import FPDF
import whisper

class TranscriberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Audio & Video Transcriber")
        self.root.geometry("800x650")
        self.root.minsize(600, 500)

        # Apply a clean theme
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.selected_file_path = ""
        self.model = None

        self._build_ui()

    def _build_ui(self):
        # Configure main responsive grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)

        # --- Top Section: File Selection ---
        top_frame = ttk.LabelFrame(self.root, text=" 1. Select Media File ", padding=15)
        top_frame.grid(row=0, column=0, sticky="ew", padx=15, pady=(15, 5))
        top_frame.columnconfigure(1, weight=1)

        self.btn_browse = ttk.Button(top_frame, text="Browse File (MP3/MP4)", command=self.browse_file)
        self.btn_browse.grid(row=0, column=0, padx=(0, 10))

        self.lbl_filepath = ttk.Label(top_frame, text="No file selected...", foreground="gray")
        self.lbl_filepath.grid(row=0, column=1, sticky="w")

        # --- Middle Section: Actions & Progress ---
        mid_frame = ttk.Frame(self.root, padding=15)
        mid_frame.grid(row=1, column=0, sticky="ew", padx=15)
        mid_frame.columnconfigure(1, weight=1)

        self.btn_transcribe = ttk.Button(mid_frame, text="▶ Start Transcription", command=self.start_transcription_thread)
        self.btn_transcribe.grid(row=0, column=0, padx=(0, 10))

        self.progress_bar = ttk.Progressbar(mid_frame, mode="indeterminate")
        self.progress_bar.grid(row=0, column=1, sticky="ew", padx=(0, 10))

        self.lbl_status = ttk.Label(mid_frame, text="Status: Ready", font=("Helvetica", 9, "italic"))
        self.lbl_status.grid(row=1, column=0, columnspan=2, sticky="w", pady=(5, 0))

        # --- Bottom Panel: Output Display & Export ---
        bottom_frame = ttk.LabelFrame(self.root, text=" 2. Transcription Output ", padding=15)
        bottom_frame.grid(row=2, column=0, sticky="nsew", padx=15, pady=(5, 15))
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.rowconfigure(0, weight=1)

        # Text Widget + Scrollbar
        self.txt_output = tk.Text(bottom_frame, wrap="word", font=("Consolas", 10), bg="#fafafa")
        self.txt_output.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(bottom_frame, orient="vertical", command=self.txt_output.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.txt_output["yscrollcommand"] = scrollbar.set

        # Buttons Panel (Copy & PDF Export)
        btn_panel = ttk.Frame(bottom_frame)
        btn_panel.grid(row=1, column=0, columnspan=2, sticky="e", pady=(10, 0))

        self.btn_copy = ttk.Button(btn_panel, text="📋 Copy Text", command=self.copy_to_clipboard)
        self.btn_copy.pack(side="left", padx=(0, 10))

        self.btn_export_pdf = ttk.Button(btn_panel, text="📄 Download as PDF", command=self.export_to_pdf)
        self.btn_export_pdf.pack(side="left")

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Audio or Video File",
            filetypes=[("Media Files", "*.mp3 *.mp4 *.wav *.m4a *.mpeg *.mkv"), ("All Files", "*.*")]
        )
        if file_path:
            self.selected_file_path = file_path
            self.lbl_filepath.config(text=os.path.basename(file_path), foreground="black")
            self.lbl_status.config(text="Status: File loaded. Click 'Start Transcription'.")

    def start_transcription_thread(self):
        if not self.selected_file_path:
            messagebox.showwarning("No File Selected", "Please select an MP3 or MP4 file first.")
            return

        # Run transcription in a background thread to keep UI responsive
        self.btn_transcribe.config(state="disabled")
        self.btn_browse.config(state="disabled")
        self.progress_bar.start(10)
        self.lbl_status.config(text="Status: Loading AI model & processing audio...")

        threading.Thread(target=self.run_transcription, daemon=True).start()

    def run_transcription(self):
        try:
            if self.model is None:
                # Load OpenAI Whisper base model
                self.model = whisper.load_model("base")

            result = self.model.transcribe(self.selected_file_path)
            transcription_text = result.get("text", "").strip()

            # Update UI on main thread
            self.root.after(0, self.on_transcription_complete, transcription_text)
        except Exception as e:
            self.root.after(0, self.on_transcription_error, str(e))

    def on_transcription_complete(self, text):
        self.progress_bar.stop()
        self.btn_transcribe.config(state="normal")
        self.btn_browse.config(state="normal")
        self.lbl_status.config(text="Status: Transcription finished successfully!")

        self.txt_output.delete("1.0", tk.END)
        self.txt_output.insert(tk.END, text)

    def on_transcription_error(self, error_msg):
        self.progress_bar.stop()
        self.btn_transcribe.config(state="normal")
        self.btn_browse.config(state="normal")
        self.lbl_status.config(text="Status: Transcription failed.")
        messagebox.showerror("Error", f"Failed to transcribe media file:\n{error_msg}")

    def copy_to_clipboard(self):
        text = self.txt_output.get("1.0", tk.END).strip()
        if not text:
            messagebox.showinfo("Empty Text", "There is no transcription text to copy.")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        messagebox.showinfo("Success", "Transcription copied to clipboard!")

    def export_to_pdf(self):
        text = self.txt_output.get("1.0", tk.END).strip()
        if not text:
            messagebox.showinfo("Empty Text", "There is no transcription text to export.")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Documents", "*.pdf")],
            title="Save Transcription as PDF"
        )

        if save_path:
            try:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Helvetica", size=12)

                # Write title
                pdf.set_font("Helvetica", style="B", size=14)
                pdf.cell(0, 10, "Transcription Document", ln=True, align="C")
                pdf.ln(5)

                # Write content text
                pdf.set_font("Helvetica", size=11)
                # Encode text to latin-1 clean format for standard FPDF compatibility
                safe_text = text.encode("latin-1", "replace").decode("latin-1")
                pdf.multi_cell(0, 8, safe_text)

                pdf.output(save_path)
                messagebox.showinfo("Export Successful", f"File saved as:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Export Failed", f"Could not generate PDF:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranscriberApp(root)
    root.mainloop()