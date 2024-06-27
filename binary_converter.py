# binary_converter.py

import sys, os, json
import logging
import pandas as pd

"""
    # # Example usage:
    # binary_to_hex_string(r"D:\97_learning\python\111.zip", r"D:\97_learning\python\111.zip.txt")
    # hex_string_to_binary(r"D:\97_learning\python\111.zip.txt", r"D:\97_learning\python\111.zip_recover")
"""

def setup_logging(log_fpath='', format='', level=logging.INFO):
    """Configuration for logging"""
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(format if format else '%(message)s -- %(pathname)s:%(lineno)d'))
    stream_handler.setLevel(level)

    file_handler = logging.FileHandler(log_fpath if log_fpath else 'log.txt', mode='w')
    file_handler.setFormatter(logging.Formatter(format if format else '%(asctime)s %(message)s -- %(pathname)s:%(lineno)d', datefmt='%Y/%m/%d %H:%M:%S'))
    file_handler.setLevel(level)

    logging.basicConfig(handlers=[file_handler, stream_handler], level=level)

def binary_to_hex_string(binary_file_path, hex_string_file_path):
    with open(binary_file_path, 'rb') as binary_file:
        binary_data = binary_file.read()
        hex_string = binary_data.hex()

    with open(hex_string_file_path, 'w') as hex_string_file:
        hex_string_file.write(hex_string)

def hex_string_to_binary(hex_string_file_path, output_binary_file_path):
    with open(hex_string_file_path, 'r') as hex_string_file:
        hex_string = hex_string_file.read().strip()

    binary_data = bytes.fromhex(hex_string)

    with open(output_binary_file_path, 'wb') as binary_file:
        binary_file.write(binary_data)

def main():
    setup_logging()
    os.system('mkdir out')
    os.system('rm -rf out/*')
    
    try:
        bin_conv_conf = pd.read_csv("binary_converter.conf.csv")
        
        for idx, conf in bin_conv_conf.iterrows():
            fpath = conf['fpath']
            binary_to_hex_string(fpath, f'out/{os.path.basename(fpath)}.txt')
            
    except Exception as ex:
        logging.exception(ex)
    

if __name__ == "__main__":
    main()
