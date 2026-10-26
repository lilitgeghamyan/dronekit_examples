import tkinter as tk
from tkinter import messagebox

class GCSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GCS Station")
        self.root.geometry("400x500")

        self.lbl_conn = tk.Label(root, text="Connection String:")
        self.lbl_conn.pack(pady = 5)

        self.entry_conn = tk.Entry(root, width = 30)
        self.entry_conn.insert(0, "udp:127.0.0.1:14550")
        self.entry_conn.pack(pady = 5)

        self.btn_connect = tk.Button(root, text = "Connect", bg = "lightgreen", width = 20, command = self.connect_drone)
        self.btn_connect.pack(pady = 10)

        tk.Label(root, text = "-- Flight Modes --", fg = "gray").pack(pady = 5)

        modes = ["Guided", "Stabilize", "Loiter", "Land", "RTL"]
        for mode in modes:
            btn = tk.Button(root, text = mode, width = 20, command = lambda m = mode: self.set_mode(m))
            btn.pack(pady = 3)

        self.btn_arm = tk.Button(root, text = "Arm", bg = "orange", width= 20, command = self.arm_drone)
        self.btn_arm.pack(pady = 10)

        self.btn_close = tk.Button(root, text = "Close Connection", bg = "lightcoral", width = 20, command = self.close_connection)
        self.btn_close.pack(pady = 10)

    def connect_drone(self):
        conn_str = self.entry_conn.get()
        messagebox.showinfo("Status", f"Connecting to {conn_str}...")

    def set_mode(self, mode):
        messagebox.showinfo("Status", f"Mode changed to {mode}")

    def arm_drone(self):
        messagebox.showwarning("Status", "Drone armed successfully!")

    def close_connection(self):
        messagebox.showinfo("Status", "Connection closed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GCSApp(root)
    root.mainloop()
