import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def generate_random_data(file_path, size_in_gb):
    size_in_bytes = size_in_gb * 1024 * 1024 * 1024
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size_in_bytes))


def encrypt_file(input_file_path, output_file_path, key):
    # Ensure key is 32 bytes for AES 256
    assert len(key) == 32

    # Generate a random 16-byte IV
    iv = os.urandom(16)

    # Create cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Create padding object
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    with open(input_file_path, 'rb') as f_in, open(output_file_path, 'wb') as f_out:
        # Write IV to the output file
        f_out.write(iv)

        while True:
            chunk = f_in.read(1024 * 1024)  # Read in 1 MB chunks
            if len(chunk) == 0:
                break
            if len(chunk) % algorithms.AES.block_size != 0:
                chunk = padder.update(chunk)
            encrypted_chunk = encryptor.update(chunk)
            f_out.write(encrypted_chunk)

        # Finalize padding and encryption
        final_data = padder.finalize()
        encrypted_final_data = encryptor.update(final_data) + encryptor.finalize()
        f_out.write(encrypted_final_data)


if __name__ == "__main__":
    input_file = "test_file.bin"
    encrypted_file = "encrypted_file.bin"
    key = os.urandom(32)  # 32 bytes for AES 256

    print("Generating random data...")
    start_time = time.time()
    generate_random_data(input_file, 2)  # 2 GB file
    end_time = time.time()
    print(f"Random data generation completed in {end_time - start_time:.2f} seconds.")

    print("Encrypting data...")
    start_time = time.time()
    encrypt_file(input_file, encrypted_file, key)
    end_time = time.time()
    print(f"Encryption completed in {end_time - start_time:.2f} seconds.")
