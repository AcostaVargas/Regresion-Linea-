import tkinter as tk
from tkinter import messagebox

class SimpleLinearRegression:
    def __init__(self):
        # Ejemplo de datos: Ingreso (X) y Ventas (Y)
        self.income = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.sales = [2, 4, 6, 8, 10, 12, 14, 16, 18]
        self.data_points = len(self.income)
    
    def _sum_of_products(self):
        return sum(x * y for x, y in zip(self.income, self.sales))
    
    def _sum_income(self):
        return sum(self.income)
    
    def _sum_sales(self):
        return sum(self.sales)
    
    def _sum_income_squared(self):
        return sum(x ** 2 for x in self.income)
    
    def compute_slope(self):
        numerator = (self.data_points * self._sum_of_products()) - (self._sum_income() * self._sum_sales())
        denominator = (self.data_points * self._sum_income_squared()) - (self._sum_income() ** 2)
        return numerator / denominator
    
    def compute_intercept(self, slope):
        return (self._sum_sales() - (slope * self._sum_income())) / self.data_points
    
    def fit(self):
        slope = self.compute_slope()
        intercept = self.compute_intercept(slope)
        return intercept, slope
    
    def predict(self, income_value, intercept, slope):
        return intercept + slope * income_value


# Función para crear la interfaz y realizar la predicción
def main():
    # Crear el modelo y ajustar los parámetros
    model = SimpleLinearRegression()
    intercept, slope = model.fit()

    # Configuración de la ventana de Tkinter
    root = tk.Tk()
    root.title("Predicción de Ventas")
    root.geometry("300x200")

    # Título
    title_label = tk.Label(root, text="Modelo de Regresión Lineal", font=("Helvetica", 14))
    title_label.pack(pady=10)

    # Etiqueta y campo de entrada para el ingreso
    income_label = tk.Label(root, text="Ingrese el valor de ingreso:")
    income_label.pack()
    income_entry = tk.Entry(root)
    income_entry.pack()

    # Función para manejar la predicción
    def predict_sales():
        try:
            income_value = float(income_entry.get())
            predicted_sales = model.predict(income_value, intercept, slope)
            result = f"Predicción de Ventas: {predicted_sales:.2f}"
            messagebox.showinfo("Resultado", result)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")

    # Botón para realizar la predicción
    predict_button = tk.Button(root, text="Predecir", command=predict_sales)
    predict_button.pack(pady=10)

    # Mostrar la ecuación de regresión en la interfaz
    equation_label = tk.Label(root, text=f"Ecuación: Ventas = {intercept:.2f} + {slope:.2f} * Ingreso")
    equation_label.pack(pady=10)

    # Ejecutar la interfaz gráfica
    root.mainloop()

# Ejecutar la interfaz gráfica
if __name__ == "__main__":
    main()
