from math import sqrt
from nicegui import ui
from simpleeval import simple_eval


class Calculator:
    """A graphical calculator application built using NiceGUI and simpleeval."""

    def __init__(self):
        # Current mathematical expression displayed on the calculator input
        self.data = '0'
        
        # Holds the stored value for memory operations (MC, MR, M+, M-)
        self.memory = ''
        
        # Flag indicating whether the display is showing the default initial '0' state
        self.default = True
        
        # Build and render the user interface
        self.setup_gui()

    def add_data(self, data_to_add: str) -> None:
        """Appends a number, symbol, or operator to the current display string.
        
        Prevents consecutive operator inputs and replaces the default '0'.
        """
        # Guard clause: Prevents entering two consecutive operators from ['*', '/', '%']
        if all(x in ['*', '/', '%'] for x in [self.data[-1], data_to_add]):
            return
        
        # Replace the initial '0' with the first pressed key instead of appending to it
        elif self.default:
            self.data = self.data.replace('0', data_to_add)
            self.default = False
            
        # Append incoming digit or operator to the existing expression
        else:
            self.data += data_to_add

    def remove_data(self, remove_all: bool) -> None:
        """Handles clearing input.

        :param remove_all: If True (CE), resets the whole display to '0'.
                           If False (C), acts as a backspace deleting the last character.
        """
        if remove_all or len(self.data) <= 1:
            self.data = '0'
            self.default = True
        else:
            self.data = self.data[:-1]

    def calculate(self) -> None:
        """Evaluates the mathematical expression currently in self.data safely."""
        try:
            # Safely evaluate string math expression and round result to 7 decimal places
            self.data = str(round(simple_eval(self.data), 7))
        except SyntaxError:
            # Triggered on incomplete or invalid expressions (e.g., '5+')
            ui.notify('The operation is not possible')
        except Exception as error:
            # Displays any runtime math errors (e.g., Division by Zero)
            ui.notify(f'error {error}')

    def calculate_sqrt(self) -> None:
        """Evaluates the current expression first, then calculates its square root."""
        # Note: Passes float value of self.data into math.sqrt after evaluation
        self.calculate()
        self.data = str(round(sqrt(float(self.data)), 7))

    def memory_clear(self) -> None:
        """Clears stored memory value (MC button)."""
        self.memory = ''

    def memory_recall(self) -> None:
        """Appends stored memory value back onto the screen expression (MR button)."""
        if self.memory:
            self.add_data(self.memory)

    def memory_modify(self, operation: str) -> None:
        """Adds to or subtracts from stored memory value (M+ / M- buttons)."""
        if self.memory:
            self.memory = str(simple_eval(
                f'{self.memory} {operation} {self.data}'))
        else:
            self.memory = str(simple_eval(f'0 {operation} {self.data}'))
            
        # Reset memory string to empty if the net result is zero
        if self.memory == '0':
            self.memory = ''

    def setup_gui(self) -> None:
        """Constructs the visual UI layout, buttons, grid, and data bindings."""

        # Outer UI Container Card centered horizontally with top margin
        with ui.card().classes('flex mx-auto mt-40'):
            
            # Memory Indicator Icon: visible only when self.memory holds a value
            ui.icon('sim_card', color='primary').bind_visibility_from(
                self, 'memory')
            
            # Display Screen: bound to two-way state update with self.data
            ui.input().bind_value(self, 'data').props(
                'outlined input-style="text-align:right"'
            )

            # 5-Column Grid for Calculator Keypad
            with ui.grid(columns=5):
                # Row 1: Square Root & Memory Functions
                ui.button('\u221A', on_click=self.calculate_sqrt)
                ui.button('MC', on_click=self.memory_clear)
                ui.button('MR', on_click=self.memory_recall)
                ui.button('M-', on_click=lambda: self.memory_modify('-'))
                ui.button('M+', on_click=lambda: self.memory_modify('+'))

                # Row 2: Percent, Numbers (7-9), Division
                ui.button('%', on_click=lambda: self.add_data('%'))
                ui.button('7', on_click=lambda: self.add_data('7'))
                ui.button('8', on_click=lambda: self.add_data('8'))
                ui.button('9', on_click=lambda: self.add_data('9'))
                ui.button('/', on_click=lambda: self.add_data('/'))

                # Row 3: Plus/Minus Toggle (Appends hyphen), Numbers (4-6), Multiplication
                ui.button('\u00B1', on_click=lambda: self.add_data('-'))
                ui.button('4', on_click=lambda: self.add_data('4'))
                ui.button('5', on_click=lambda: self.add_data('5'))
                ui.button('6', on_click=lambda: self.add_data('6'))
                ui.button('*', on_click=lambda: self.add_data('*'))

                # Row 4: Single-character Backspace (C), Numbers (1-3), Subtraction
                ui.button('C', on_click=lambda: self.remove_data(False))
                ui.button('1', on_click=lambda: self.add_data('1'))
                ui.button('2', on_click=lambda: self.add_data('2'))
                ui.button('3', on_click=lambda: self.add_data('3'))
                ui.button('-', on_click=lambda: self.add_data('-'))

                # Row 5: Clear All (CE), Zero, Decimal point, Equals, Addition
                ui.button('CE', on_click=lambda: self.remove_data(True))
                ui.button('0', on_click=lambda: self.add_data('0'))
                ui.button('\u00B7', on_click=lambda: self.add_data('.'))
                ui.button('=', on_click=self.calculate)
                ui.button('+', on_click=lambda: self.add_data('+'))


# Inititate calculator object
calculator = Calculator()

# Launch local Web Application via NiceGUI
ui.run(title='Calculator', dark=False)