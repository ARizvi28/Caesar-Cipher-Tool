# Caesar Cipher Tool
A simple, yet effective encryption tool that uses the classic Caesar Cipher algorithm to shift characters in a given text by a specified number of positions.

## What is a Caesar Cipher?
A Caesar Cipher is a type of substitution cipher where each letter in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on.

## How to Use the Tool
Clone the repository or download the caesar_cipher.py script.
Run the script using Python  
```python caesarcipher.py```<br /> 
Follow the prompts to enter the text you want to encrypt or decrypt, the mode (encryption or decryption), and the shift value.
# Example Use Cases
### Encrypt a message:
Enter the text "HELLO", select encryption mode, and choose a shift of 3. The output will be "KHOOR".
### Decrypt a message:
Enter the text "KHOOR", select decryption mode, and choose a shift of 3. The output will be "HELLO".
### Code Explanation
The script uses a simple and efficient algorithm to perform the Caesar Cipher encryption and decryption. It works by iterating over each character in the input text, checking if it's an uppercase or lowercase letter, and applying the shift accordingly.

## Contributing
Feel free to contribute to this repository by submitting pull requests or issues. You can also use this tool as a starting point for your own projects and experiments with encryption algorithms.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code as you see fit.
