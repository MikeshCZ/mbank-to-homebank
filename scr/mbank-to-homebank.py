import pandas as pd
import re
from io import StringIO
import tkinter as tk
from tkinter import filedialog, messagebox

__version__ = "1.0.1"

def extract_transactions_from_mbank_csv(filepath):
    with open(filepath, 'r', encoding='cp1250') as file:
        lines = file.readlines()

    try:
        start_index = next(i for i, line in enumerate(lines) if line.startswith('#Datum operace'))
    except StopIteration:
        raise ValueError("Nepodařilo se najít začátek seznamu operací.")

    transaction_lines = [
        line for line in lines[start_index + 1:]
        if re.match(r'^\d{4}-\d{2}-\d{2};', line) and 'CZK' in line
    ]

    if not transaction_lines:
        raise ValueError("Nebyly nalezeny žádné transakce.")

    data = ''.join(transaction_lines)
    df = pd.read_csv(StringIO(data), delimiter=';', encoding='cp1250', header=None)
    df.columns = ['date', 'description', 'account', 'category', 'amount', 'empty1', 'empty2']
    df = df[['date', 'description', 'category', 'amount']]
    df['amount'] = df['amount'].astype(str).str.replace(' CZK', '', regex=False).str.replace(',', '.')
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df = df.dropna(subset=['amount'])
    return df

def convert_to_homebank_format(df):
    output = pd.DataFrame()
    output['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')
    output['payment'] = 4 # Bank transfer
    output['number'] = ''
    output['payee'] = ''
    output['memo'] = df['description'].str.replace(r'\s+', ' ', regex=True).str.strip().str.capitalize()
    output['amount'] = df['amount']
    output['category'] = df['category'].fillna('')
    output['tags'] = ''
    return output

def main():
    root = tk.Tk()
    root.withdraw()
    
    width = 400
    height = 100
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = 50
    root.geometry(f"{width}x{height}+{x}+{y}")

    root.title("mBank to HomeBank CSV Converter | v"+__version__)
    root.deiconify()
    root.lift()
    
    label = tk.Label(
        root,
        text="Vyberte CSV výpis z mBank pro převod do formátu HomeBank.",
        font=("Arial", 12),
        wraplength=350,
        justify="center"
    )
    label.pack(expand=True)

    input_path = filedialog.askopenfilename(
        title="Vyber CSV výpis z mBank",
        filetypes=[("CSV soubory", "*.csv")]
    )

    if not input_path:
        messagebox.showinfo("Zrušeno", "Nebyl vybrán vstupní soubor.")
        return

    try:
        df_raw = extract_transactions_from_mbank_csv(input_path)
        df_homebank = convert_to_homebank_format(df_raw)
    except Exception as e:
        messagebox.showerror("Chyba", f"Nastala chyba při zpracování: {e}")
        return

    output_path = filedialog.asksaveasfilename(
        title="Ulož výstupní CSV pro HomeBank",
        defaultextension=".csv",
        filetypes=[("CSV soubory", "*.csv")]
    )

    if not output_path:
        messagebox.showinfo("Zrušeno", "Nebyl zvolen výstupní soubor.")
        return
    
    try:
        df_homebank.to_csv(output_path, sep=';', index=False)
        messagebox.showinfo("Hotovo", f"Soubor byl uložen jako:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Chyba", f"Soubor se nepodařilo uložit:\n{e}")

if __name__ == "__main__":
    main()