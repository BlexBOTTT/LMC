import tkinter as tk

class LittleManComputer:
    def __init__(self, root):
        self.root = root
        self.root.title("Little Man Computer")

        self.memory = [0] * 100
        self.accumulator = 0
        self.instruction_counter = 0

        self.create_widgets()

    def create_widgets(self):
        # Left Input Area
        self.input_label = tk.Label(self.root, text="Input Instructions:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.input_area = tk.Text(self.root, height=15, width=40)
        self.input_area.grid(row=1, column=0, padx=5, pady=5, rowspan=8, sticky="w")

        self.load_button = tk.Button(self.root, text="Load Program", command=self.load_program)
        self.load_button.grid(row=9, column=0, padx=5, pady=5, sticky="w")

        # Middle CPU Information Display
        self.cpu_label = tk.Label(self.root, text="CPU Information:")
        self.cpu_label.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

        self.ic_label = tk.Label(self.root, text="Program Counter (IC):")
        self.ic_label.grid(row=1, column=1, padx=5, pady=5)
        self.ic_value = tk.Label(self.root, text=str(self.instruction_counter))
        self.ic_value.grid(row=1, column=2, padx=5, pady=5)

        self.acc_label = tk.Label(self.root, text="Accumulator (ACC):")
        self.acc_label.grid(row=2, column=1, padx=5, pady=5)
        self.acc_value = tk.Label(self.root, text=str(self.accumulator))
        self.acc_value.grid(row=2, column=2, padx=5, pady=5)

        # Input Box
        self.input_instruction_label = tk.Label(self.root, text="Select Instruction:")
        self.input_instruction_label.grid(row=3, column=1, padx=5, pady=5)

        # Define instructions and their corresponding codes
        instructions = {
            "Add Two Numbers": "INP\nSTA 99\nINP\nADD 99\nOUT\nHLT",
            "Halt": ""
        }

        self.instruction_var = tk.StringVar(self.root)
        self.instruction_var.set("Add Two Numbers")  # default value

        self.instruction_dropdown = tk.OptionMenu(self.root, self.instruction_var, *instructions.keys(), command=self.update_instruction_box)
        self.instruction_dropdown.grid(row=3, column=2, padx=5, pady=5)

        self.input_number_label = tk.Label(self.root, text="Input Number:")
        self.input_number_label.grid(row=4, column=1, padx=5, pady=5)

        self.input_number_entry = tk.Entry(self.root)
        self.input_number_entry.grid(row=4, column=2, padx=5, pady=5)

        # Output Box
        self.output_label = tk.Label(self.root, text="Output:")
        self.output_label.grid(row=5, column=1, padx=5, pady=5)

        self.output_value = tk.Label(self.root, text="")
        self.output_value.grid(row=5, column=2, padx=5, pady=5)

        # Right Memory Display
        self.memory_label = tk.Label(self.root, text="Memory:")
        self.memory_label.grid(row=0, column=3, padx=5, pady=5)

        self.memory_display = tk.Frame(self.root)
        self.memory_display.grid(row=1, column=3, padx=5, pady=5, rowspan=8)

        self.update_memory_display()

        # Buttons
        self.step_button = tk.Button(self.root, text="Step", command=self.step)
        self.step_button.grid(row=9, column=1, padx=5, pady=5)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.grid(row=9, column=2, padx=5, pady=5)

    def update_instruction_box(self, selected_instruction):
        # Update the instruction box based on the selected instruction
        instructions = {
            "Add Two Numbers": "INP\nSTA 99\nINP\nADD 99\nOUT\nHLT",
            "Halt": ""
        }

        # Set the instruction code in the input box
        self.input_area.delete("1.0", tk.END)
        self.input_area.insert(tk.END, instructions[selected_instruction])

    def update_memory_display(self):
        for i in range(10):
            for j in range(10):
                memory_value = self.memory[i * 10 + j]
                label = tk.Label(self.memory_display, text=f"{memory_value:03d}", borderwidth=2, relief="solid", width=4, height=1)
                label.grid(row=i, column=j, padx=1, pady=1)

    def load_program(self):
        program_text = self.input_area.get("1.0", tk.END)
        instructions = []

        for line in program_text.split("\n"):
            line = line.strip()
            if line:
                # Assuming that instructions are space-separated
                instructions.extend(map(int, line.split()))

        # Load the instructions into memory starting from address 0
        self.memory[:len(instructions)] = instructions
        self.update_memory_display()

    def step(self):
        # Implement your LMC step logic here
        # Update instruction counter, accumulator, and memory
        # You can use self.memory, self.accumulator, and self.instruction_counter

        if self.instruction_counter < len(self.memory):
            instruction = self.memory[self.instruction_counter]

            opcode = instruction // 100
            operand = instruction % 100

            if opcode == 9:  # Add
                self.accumulator += self.memory[operand]

            # Update the program counter
            self.instruction_counter += 1
            self.ic_value.config(text=str(self.instruction_counter))
            self.acc_value.config(text=str(self.accumulator))

    def reset(self):
        # Implement your LMC reset logic here
        # Reset instruction counter, accumulator, and memory
        # You can use self.memory, self.accumulator, and self.instruction_counter

        self.instruction_counter = 0
        self.accumulator = 0
        self.ic_value.config(text=str(self.instruction_counter))
        self.acc_value.config(text=str(self.accumulator))

        # Clear the input instructions
        self.input_area.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LittleManComputer(root)
    root.mainloop()
