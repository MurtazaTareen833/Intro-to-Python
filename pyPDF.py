from PyPDF2 import PdfFileMerger

def merge_pdfs(input_files, output_file):
    merger = PdfFileMerger()

    for file in input_files:
        merger.append(file)

    merger.write(output_file)
    merger.close()

# Example usage
input_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']  # Replace with the actual input file names
output_file = 'merged.pdf'  # Replace with the desired output file name

merge_pdfs(input_files, output_file)
