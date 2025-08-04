import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class ModernDashboard(ctk.CTk):
    """Simple dashboard demonstrating a sidebar and info panels using CustomTkinter."""

    def __init__(self):
        super().__init__()

        self.title("Course Activity Dashboard")
        self.geometry("1000x600")
        self.configure(bg="#F5F6FA")

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#FFFFFF")
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(
            self.sidebar,
            text="ATTIO",
            font=("Arial", 20, "bold"),
            text_color="#2D6CDF",
        ).pack(pady=(20, 10))
        for item in ["Dashboard", "Courses", "Schedule", "Analysis", "Messages"]:
            ctk.CTkButton(
                self.sidebar,
                text=item,
                fg_color="transparent",
                text_color="#333",
                hover_color="#E5E5E5",
            ).pack(pady=5, fill="x", padx=20)

        # Main Content
        self.main = ctk.CTkFrame(self, fg_color="#F5F6FA")
        self.main.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            self.main,
            text="COURSE ACTIVITY",
            font=("Arial", 22, "bold"),
            text_color="#000000",
        ).pack(anchor="nw")

        # Progress Cards
        self.progress_frame = ctk.CTkFrame(self.main, fg_color="#FFFFFF", corner_radius=16)
        self.progress_frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            self.progress_frame,
            text="Course Progress",
            font=("Arial", 16, "bold"),
        ).pack(anchor="w", padx=20, pady=(10, 0))

        self.circles = ctk.CTkFrame(self.progress_frame, fg_color="#FFFFFF")
        self.circles.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(
            self.circles,
            text="Design Leadership - 68%",
            font=("Arial", 14),
        ).pack(side="left", padx=10)
        ctk.CTkLabel(
            self.circles,
            text="UX Design - 43%",
            font=("Arial", 14),
        ).pack(side="left", padx=10)

        # Upcoming Courses
        self.schedule_frame = ctk.CTkFrame(self.main, fg_color="#FFFFFF", corner_radius=16)
        self.schedule_frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            self.schedule_frame,
            text="Upcoming Courses",
            font=("Arial", 16, "bold"),
            text_color="#FF6B00",
        ).pack(anchor="w", padx=20, pady=(10, 0))

        ctk.CTkLabel(
            self.schedule_frame,
            text="User Interface Design - 13:00 to 14:00",
            font=("Arial", 13),
        ).pack(anchor="w", padx=20, pady=5)
        ctk.CTkLabel(
            self.schedule_frame,
            text="Design Leadership - 15:00 to 16:00",
            font=("Arial", 13),
        ).pack(anchor="w", padx=20, pady=5)

        # Messages & Goal Sidebar
        self.right_panel = ctk.CTkFrame(self.main, fg_color="#F5F6FA")
        self.right_panel.place(relx=0.75, rely=0, relheight=1, relwidth=0.25)

        msg_box = ctk.CTkFrame(self.right_panel, fg_color="#FFFFFF", corner_radius=16)
        msg_box.pack(fill="x", pady=10)
        ctk.CTkLabel(
            msg_box,
            text="Messages",
            font=("Arial", 15, "bold"),
            anchor="w",
        ).pack(anchor="w", padx=15, pady=10)
        ctk.CTkLabel(
            msg_box,
            text="You have 12 unread messages.",
            font=("Arial", 12),
        ).pack(anchor="w", padx=15)

        goal_box = ctk.CTkFrame(self.right_panel, fg_color="#FFFFFF", corner_radius=16)
        goal_box.pack(fill="x", pady=10)
        ctk.CTkLabel(
            goal_box,
            text="My Goal",
            font=("Arial", 15, "bold"),
            anchor="w",
        ).pack(anchor="w", padx=15, pady=10)
        ctk.CTkLabel(
            goal_box,
            text="Progress: 24%",
            font=("Arial", 12),
        ).pack(anchor="w", padx=15)


if __name__ == "__main__":
    app = ModernDashboard()
    app.mainloop()
