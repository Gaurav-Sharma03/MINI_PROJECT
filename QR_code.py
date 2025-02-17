import qrcode

def generate_qr_code(data, filename='qrcode.png'):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code object
    img = qr.make_image(fill='black', back_color='red')

    # Save the image to a file
    img.save(filename)
    print(f'QR code generated and saved as {filename}')

# Example usage
data = 'https://www.example.com'
generate_qr_code(data)

'''import qrcode
import tkinter as tk
from tkinter import simpledialog, messagebox


def generate_qr_code(data, filename='qrcode.png'):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code object
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file
    img.save(filename)
    messagebox.showinfo('Success', f'QR code generated and saved as {filename}')


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    data = simpledialog.askstring('Input', 'Enter the data for the QR code:')
    if data:
        generate_qr_code(data)
    else:
        messagebox.showwarning('Input Error', 'No data provided for QR code generation.')


if __name__ == '__main__':
    main()
    '''